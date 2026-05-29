from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DATABASE_URL = "sqlite:///./verbos.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(
    title="API de Verbos Irregulares",
    description="API para gestión de ejemplos de verbos con irregularidades consonánticas",
    version="1.0.0"
)

# Modelos de Base de Datos
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)

class Example(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    verb = Column(String)
    conjugation = Column(String)
    sentence = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Esquemas Pydantic
class CategoryCreate(BaseModel):
    name: str
    description: str

class ExampleCreate(BaseModel):
    verb: str
    conjugation: str
    sentence: str

class ExampleResponse(ExampleCreate):
    id: int
    category_id: int

    class Config:
        orm_mode = True

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicializar datos
@app.on_event("startup")
def startup():
    db = SessionLocal()
    try:
        if not db.query(Category).count():
            categories = [
                Category(id=1, name="Epéntesis", description="Inserción consonántica"),
                Category(id=2, name="Síncopa", description="Síncopa y Epéntesis"),
                Category(id=3, name="Alternancias", description="Alternancias consonánticas/vocálicas"),
                Category(id=4, name="Pretéritos", description="Pretéritos fuertes"),
                Category(id=5, name="Participios", description="Participios irregulares"),
                Category(id=6, name="Especiales", description="Verbos de conjugación especial"),
                Category(id=7, name="Defectivos", description="Verbos defectivos")
            ]
            db.bulk_save_objects(categories)
            db.commit()
    finally:
        db.close()

# Endpoints
@app.get("/categories", response_model=List[dict], tags=["Categorías"])
def get_categories(db: Session = Depends(get_db)):
    """Obtener lista de categorías con conteo de ejemplos"""
    categories = db.query(Category).all()
    return [{
        "id": cat.id,
        "name": cat.name,
        "description": cat.description,
        "examples_count": db.query(Example).filter(Example.category_id == cat.id).count()
    } for cat in categories]

@app.get("/categories/{category_id}/examples", response_model=List[ExampleResponse], tags=["Ejemplos"])
def get_examples(category_id: int, db: Session = Depends(get_db)):
    """Obtener ejemplos de una categoría"""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    return db.query(Example).filter(Example.category_id == category_id).all()

@app.post("/categories/{category_id}/examples", response_model=ExampleResponse, status_code=201, tags=["Ejemplos"])
def create_example(category_id: int, example: ExampleCreate, db: Session = Depends(get_db)):
    """Crear nuevo ejemplo en categoría"""
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    current_count = db.query(Example).filter(Example.category_id == category_id).count()
    if current_count >= 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Límite de 100 ejemplos alcanzado para esta categoría"
        )
    
    db_example = Example(**example.dict(), category_id=category_id)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

@app.put("/examples/{example_id}", response_model=ExampleResponse, tags=["Ejemplos"])
def update_example(example_id: int, example: ExampleCreate, db: Session = Depends(get_db)):
    """Actualizar un ejemplo existente"""
    db_example = db.query(Example).filter(Example.id == example_id).first()
    if not db_example:
        raise HTTPException(status_code=404, detail="Ejemplo no encontrado")
    
    for key, value in example.dict().items():
        setattr(db_example, key, value)
    
    db.commit()
    db.refresh(db_example)
    return db_example

@app.delete("/examples/{example_id}", status_code=204, tags=["Ejemplos"])
def delete_example(example_id: int, db: Session = Depends(get_db)):
    """Eliminar un ejemplo"""
    example = db.query(Example).filter(Example.id == example_id).first()
    if not example:
        raise HTTPException(status_code=404, detail="Ejemplo no encontrado")
    
    db.delete(example)
    db.commit()

@app.get("/progress", tags=["Progreso"])
def get_progress(db: Session = Depends(get_db)):
    """Obtener progreso general"""
    categories = db.query(Category).all()
    total = 0
    progress = []
    
    for cat in categories:
        count = db.query(Example).filter(Example.category_id == cat.id).count()
        total += count
        progress.append({
            "category_id": cat.id,
            "category_name": cat.name,
            "count": count,
            "percentage": f"{(count / 100) * 100:.0f}%"
        })
    
    return {
        "total": total,
        "max_total": 700,
        "percentage": f"{(total / 700) * 100:.0f}%",
        "categories": progress
    }
