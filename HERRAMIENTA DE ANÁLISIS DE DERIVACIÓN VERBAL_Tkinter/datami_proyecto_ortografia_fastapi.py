# main.py (Adaptado para FastAPI)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(title="Ortografía y AFI API")

DATA_FILE = "datos_ortografia.json"

# ----------------------------
# Modelos
# ----------------------------
class Ejemplo(BaseModel):
    palabra: str
    afi: str
    regla: str
    tema: str

class Progreso(BaseModel):
    palabra: str
    correcta: bool

# ----------------------------
# Funciones auxiliares
# ----------------------------

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

# ----------------------------
# Rutas API
# ----------------------------

@app.get("/ejemplos", response_model=List[Ejemplo])
def obtener_ejemplos(tema: Optional[str] = None):
    datos = cargar_datos()
    if tema:
        return [ej for ej in datos if ej["tema"].lower() == tema.lower()]
    return datos

@app.post("/ejemplos", response_model=Ejemplo)
def agregar_ejemplo(ejemplo: Ejemplo):
    datos = cargar_datos()
    datos.append(ejemplo.dict())
    guardar_datos(datos)
    return ejemplo

@app.get("/ejemplos/{palabra}", response_model=Ejemplo)
def buscar_por_palabra(palabra: str):
    datos = cargar_datos()
    for ej in datos:
        if ej["palabra"].lower() == palabra.lower():
            return ej
    raise HTTPException(status_code=404, detail="Palabra no encontrada")

@app.put("/ejemplos/{palabra}", response_model=Ejemplo)
def editar_ejemplo(palabra: str, nuevo: Ejemplo):
    datos = cargar_datos()
    for i, ej in enumerate(datos):
        if ej["palabra"].lower() == palabra.lower():
            datos[i] = nuevo.dict()
            guardar_datos(datos)
            return nuevo
    raise HTTPException(status_code=404, detail="Palabra no encontrada")

@app.delete("/ejemplos/{palabra}")
def eliminar_ejemplo(palabra: str):
    datos = cargar_datos()
    nuevo_datos = [ej for ej in datos if ej["palabra"].lower() != palabra.lower()]
    if len(datos) == len(nuevo_datos):
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    guardar_datos(nuevo_datos)
    return {"mensaje": "Ejemplo eliminado correctamente"}

# ----------------------------
# Progreso (archivo aparte)
# ----------------------------
PROGRESO_FILE = "progreso.json"

@app.post("/progreso")
def guardar_progreso(item: Progreso):
    if os.path.exists(PROGRESO_FILE):
        with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
            progreso = json.load(f)
    else:
        progreso = []
    progreso.append(item.dict())
    with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
        json.dump(progreso, f, ensure_ascii=False, indent=2)
    return {"mensaje": "Progreso guardado"}

@app.get("/progreso")
def obtener_progreso():
    if os.path.exists(PROGRESO_FILE):
        with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
