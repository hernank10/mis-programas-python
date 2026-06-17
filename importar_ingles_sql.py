#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE INGLES A SQL
Importa todos los programas y ejercicios de inglés a la base de datos SQL
Autor: @Hernank10
"""

import os
import sys
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorInglesSQL:
    def __init__(self):
        self.base_path = Path("INGLES/tutores")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para inglés"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS programas_ingles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            tipo TEXT,
            descripcion TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecciones_ingles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            nivel INTEGER DEFAULT 1,
            categoria TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_ingles_completos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT NOT NULL,
            respuesta_correcta TEXT NOT NULL,
            explicacion TEXT,
            categoria TEXT,
            dificultad INTEGER DEFAULT 1
        )
        ''')
        
        print("✅ Tablas de inglés creadas")
    
    def importar_programas(self):
        """Importar todos los programas de inglés"""
        print("📥 Importando programas de inglés...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count = 0
        for archivo in self.base_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:5000]
            except:
                pass
            
            # Clasificar por tipo
            categoria = self._clasificar_ingles(nombre, contenido)
            tipo = self._detectar_tipo(contenido)
            
            db.ejecutar('''
            INSERT INTO programas_ingles (nombre, categoria, tipo, descripcion, contenido, archivo_original)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', [nombre, categoria, tipo, f"Programa de inglés: {nombre}", contenido, str(archivo)])
            
            count += 1
            print(f"  ✅ Importado: {nombre}")
        
        print(f"\n📊 Total importados: {count} programas")
    
    def _clasificar_ingles(self, nombre, contenido):
        """Clasificar el programa por categoría"""
        nombre_lower = nombre.lower()
        contenido_lower = contenido.lower()
        
        if "entrenador" in nombre_lower or "tutor" in nombre_lower:
            return "entrenador"
        elif "juego" in nombre_lower or "game" in nombre_lower or "identifying" in nombre_lower:
            return "juego"
        elif "diccionario" in nombre_lower or "lecciones" in nombre_lower:
            return "diccionario"
        elif "practica" in nombre_lower or "practice" in nombre_lower or "ejercicios" in nombre_lower:
            return "ejercicios"
        elif "declinacion" in nombre_lower or "latin" in nombre_lower:
            return "latin"
        elif "conectores" in nombre_lower:
            return "conectores"
        elif "preguntas" in nombre_lower or "questions" in nombre_lower:
            return "preguntas"
        else:
            return "general"
    
    def _detectar_tipo(self, contenido):
        """Detectar tipo de interfaz"""
        contenido_lower = contenido.lower()
        if "tkinter" in contenido_lower:
            return "Tkinter"
        elif "kivy" in contenido_lower:
            return "Kivy"
        elif "pygame" in contenido_lower:
            return "Pygame"
        else:
            return "consola"

if __name__ == '__main__':
    importador = ImportadorInglesSQL()
    importador.importar_programas()
