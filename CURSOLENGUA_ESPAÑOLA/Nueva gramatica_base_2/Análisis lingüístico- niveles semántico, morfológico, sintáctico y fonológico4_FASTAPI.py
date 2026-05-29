from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conlist
from typing import Dict, List, Optional
from eng_to_ipa import convert as eng_to_ipa
import uvicorn

app = FastAPI(
    title="Linguistic Analysis API",
    description="API para análisis lingüístico multinivel",
    version="1.0.0",
    openapi_tags=[{
        "name": "Semantic Analysis",
        "description": "Clasificación categorial de texto"
    }, {
        "name": "Morphological Analysis",
        "description": "Descomposición morfológica de palabras"
    }, {
        "name": "Phonological Analysis",
        "description": "Transcripción fonética (IPA)"
    }]
)

class TextInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000, example="El rápido zorro marrón salta sobre el perro perezoso")
    
class PhoneticInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, example="Hello world")
    language: str = Field("en", regex="^(en|es)$")

class SemanticResult(BaseModel):
    nouns: conlist(str, min_items=0)
    verbs: conlist(str, min_items=0)
    adjectives: conlist(str, min_items=0)

class MorphologicalResult(BaseModel):
    root: str
    morphemes: List[str]
    derivations: List[str]

@app.post("/analyze/semantic",
          response_model=SemanticResult,
          tags=["Semantic Analysis"],
          summary="Análisis semántico-categorial",
          description="Clasifica palabras en categorías gramaticales básicas")
async def analyze_semantic(data: TextInput):
    try:
        return semantic_analysis(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/morphological",
          response_model=MorphologicalResult,
          tags=["Morphological Analysis"],
          summary="Análisis morfológico",
          description="Identifica raíces y morfemas en palabras")
async def analyze_morphological(data: TextInput):
    if len(data.text.split()) > 1:
        raise HTTPException(status_code=400, detail="Solo se permite una palabra")
    
    try:
        return morphological_analysis(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/phonetic",
          tags=["Phonological Analysis"],
          summary="Transcripción fonológica",
          description="Convierte texto a notación IPA (soportes inglés y español básico)")
async def analyze_phonetic(data: PhoneticInput):
    try:
        return {"ipa": phonetic_conversion(data.text, data.language)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def semantic_analysis(text: str) -> SemanticResult:
    """Lógica de análisis semántico"""
    return SemanticResult(
        nouns=[word for word in text.split() if word.endswith(('ción', 'dad', 'ez'))],
        verbs=[word for word in text.split() if word.endswith(('ar', 'er', 'ir'))],
        adjectives=[word for word in text.split() if word.endswith(('oso', 'al', 'ivo'))]
    )

def morphological_analysis(word: str) -> MorphologicalResult:
    """Lógica de análisis morfológico"""
    return MorphologicalResult(
        root=word[:3].upper(),
        morphemes=[word[i:i+3] for i in range(0, len(word), 3)],
        derivations=[f"{word} → {word}oso"] if len(word) > 4 else []
    )

def phonetic_conversion(text: str, lang: str) -> str:
    """Conversión fonética (extender para soporte multi-idioma)"""
    if lang == "en":
        return eng_to_ipa(text)
    elif lang == "es":
        return " ".join([f"/{word}/" for word in text.split()])
    
    raise ValueError("Idioma no soportado")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
