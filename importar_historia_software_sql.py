#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE HISTORIA DEL SOFTWARE EDUCATIVO A SQL
Autor: @Hernank10
"""

import os
import sys
import json
import sqlite3
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorHistoriaSoftwareSQL:
    def __init__(self):
        self.base_path = Path("Historia del software educativo y los sistemas con los que más se ha aprendido")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para historia del software"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS software_educativo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT,
            tecnologia TEXT,
            archivo_original TEXT,
            contenido TEXT,
            categoria TEXT DEFAULT 'historico'
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS simulaciones_historicas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS prototipos_educativos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tecnologia TEXT,
            archivo_original TEXT,
            estado TEXT DEFAULT 'prototipo'
        )
        ''')
        
        print("✅ Tablas de historia del software creadas")
    
    def importar_software(self):
        """Importar todos los programas"""
        print("📥 Importando software educativo histórico...")
        
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
            tipo = self._clasificar_software(nombre, contenido)
            tecnologia = self._detectar_tecnologia(contenido)
            
            db.ejecutar('''
            INSERT INTO software_educativo (nombre, descripcion, tipo, tecnologia, archivo_original, contenido)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', [nombre, f"Programa educativo: {nombre}", tipo, tecnologia, str(archivo), contenido])
            
            count += 1
            print(f"  ✅ Importado: {nombre}")
        
        print(f"\n📊 Total importados: {count} programas")
    
    def _clasificar_software(self, nombre, contenido):
        """Clasificar el software por tipo"""
        nombre_lower = nombre.lower()
        contenido_lower = contenido.lower()
        
        if "logo" in nombre_lower:
            return "logo"
        elif "khan" in nombre_lower:
            return "khan_academy"
        elif "oregon" in nombre_lower:
            return "simulacion"
        elif "simcity" in nombre_lower:
            return "simulacion"
        elif "duolingo" in nombre_lower:
            return "idiomas"
        elif "griego" in nombre_lower:
            return "idiomas"
        elif "fotomat" in nombre_lower or "photomath" in nombre_lower:
            return "matematicas"
        elif "carmen" in nombre_lower:
            return "juego"
        elif "tkinter" in contenido_lower:
            return "gui"
        elif "kivy" in contenido_lower:
            return "gui"
        else:
            return "educativo"
    
    def _detectar_tecnologia(self, contenido):
        """Detectar tecnologías utilizadas"""
        tecnologias = []
        if "tkinter" in contenido.lower():
            tecnologias.append("Tkinter")
        if "kivy" in contenido.lower():
            tecnologias.append("Kivy")
        if "pygame" in contenido.lower():
            tecnologias.append("Pygame")
        if "sqlite" in contenido.lower():
            tecnologias.append("SQLite")
        if "opencv" in contenido.lower():
            tecnologias.append("OpenCV")
        if "tesseract" in contenido.lower():
            tecnologias.append("Tesseract")
        if "turtle" in contenido.lower():
            tecnologias.append("Turtle")
        return ", ".join(tecnologias) if tecnologias else "Python"

if __name__ == '__main__':
    importador = ImportadorHistoriaSoftwareSQL()
    importador.importar_software()
