# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import random
import os
from pathlib import Path

app = FastAPI()

# Configuración de archivos
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
EXAMPLES_FILE = DATA_DIR / "ejemplos.json"
PROGRESS_FILE = DATA_DIR / "progreso.json"

# Modelos Pydantic
class Example(BaseModel):
    palabra: str
    AFI: str
    categoria: str
    regla: str
    significado: str

class ExampleResponse(Example):
    id: int

class PracticeSession(BaseModel):
    categoria: str
    current_question: int = 0
    correct_answers: int = 0
    questions: List[int]

class ProgressEntry(BaseModel):
    session_id: str
    categoria: str
    total: int
    correctos: int
    fecha: datetime

# Funciones de utilidad para datos
def load_data(file: Path, default=[]):
    try:
        return json.loads(file.read_text())
    except FileNotFoundError:
        return default

def save_data(file: Path, data):
    file.write_text(json.dumps(data, indent=2, ensure_ascii=False))

# Endpoints principales
@app.post("/ejemplos/", response_model=ExampleResponse)
async def crear_ejemplo(ejemplo: Example):
    ejemplos = load_data(EXAMPLES_FILE)
    nuevo_id = len(ejemplos)
    ejemplo_dict = ejemplo.dict()
    ejemplo_dict["id"] = nuevo_id
    ejemplos.append(ejemplo_dict)
    save_data(EXAMPLES_FILE, ejemplos)
    return ejemplo_dict

@app.get("/ejemplos/", response_model=List[ExampleResponse])
async def obtener_ejemplos(categoria: Optional[str] = None):
    ejemplos = load_data(EXAMPLES_FILE)
    if categoria:
        return [e for e in ejemplos if e["categoria"] == categoria]
    return ejemplos

@app.post("/practica/iniciar/")
async def iniciar_practica(categoria: str):
    ejemplos = load_data(EXAMPLES_FILE)
    categoria_ejemplos = [e["id"] for e in ejemplos if e["categoria"] == categoria]
    
    if not categoria_ejemplos:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    random.shuffle(categoria_ejemplos)
    session_id = os.urandom(16).hex()
    
    session = {
        "session_id": session_id,
        "categoria": categoria,
        "current_question": 0,
        "correct_answers": 0,
        "questions": categoria_ejemplos
    }
    
    return session

@app.get("/practica/pregunta/")
async def obtener_pregunta(session_id: str):
    progreso = load_data(PROGRESS_FILE)
    session = next((s for s in progreso if s["session_id"] == session_id), None)
    
    if not session or session["current_question"] >= len(session["questions"]):
        raise HTTPException(status_code=404, detail="Sesión no válida")
    
    ejemplos = load_data(EXAMPLES_FILE)
    ejemplo_id = session["questions"][session["current_question"]]
    ejemplo = next(e for e in ejemplos if e["id"] == ejemplo_id)
    
    return {
        "pregunta_actual": session["current_question"] + 1,
        "total_preguntas": len(session["questions"]),
        "AFI": ejemplo["AFI"],
        "regla": ejemplo["regla"]
    }

@app.post("/practica/verificar/")
async def verificar_respuesta(session_id: str, respuesta: str):
    progreso = load_data(PROGRESS_FILE)
    session = next((s for s in progreso if s["session_id"] == session_id), None)
    
    if not session:
        raise HTTPException(status_code=404, detail="Sesión no válida")
    
    ejemplos = load_data(EXAMPLES_FILE)
    ejemplo_id = session["questions"][session["current_question"]]
    ejemplo = next(e for e in ejemplos if e["id"] == ejemplo_id)
    
    correcto = respuesta.lower() == ejemplo["palabra"].lower()
    
    if correcto:
        session["correct_answers"] += 1
    
    session["current_question"] += 1
    
    if session["current_question"] >= len(session["questions"]):
        session["fecha"] = datetime.now().isoformat()
    
    save_data(PROGRESS_FILE, progreso)
    
    return {
        "correcto": correcto,
        "respuesta_correcta": ejemplo["palabra"],
        "explicacion": ejemplo["significado"],
        "progreso_actual": f"{session['correct_answers']}/{len(session['questions'])}"
    }

@app.get("/estadisticas/")
async def obtener_estadisticas(categoria: Optional[str] = None):
    progreso = load_data(PROGRESS_FILE)
    ejemplos = load_data(EXAMPLES_FILE)
    
    stats = {}
    for session in progreso:
        if categoria and session["categoria"] != categoria:
            continue
        
        if session["categoria"] not in stats:
            stats[session["categoria"]] = {
                "total_sesiones": 0,
                "total_preguntas": 0,
                "aciertos": 0
            }
        
        stats[session["categoria"]]["total_sesiones"] += 1
        stats[session["categoria"]]["total_preguntas"] += len(session["questions"])
        stats[session["categoria"]]["aciertos"] += session["correct_answers"]
    
    for cat, datos in stats.items():
        datos["porcentaje_acierto"] = (datos["aciertos"] / datos["total_preguntas"]) * 100 if datos["total_preguntas"] > 0 else 0
    
    return stats if not categoria else stats.get(categoria, {})
