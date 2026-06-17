#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE NUEVA GRAMÁTICA - EJERCICIOS CONSTRUCCIONES II A SQL
Autor: @Hernank10
"""

import os
import sys
import re
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorNuevaGramaticaConstrucciones:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA/Nueva gramática_ejercicicios_construccionesII")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para nueva gramática - ejercicios construcciones II"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_construcciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT,
            contenido TEXT,
            categoria TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS programas_construcciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tecnologia TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_sintaxis_avanzada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            nivel TEXT,
            categoria TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS datos_construcciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contenido TEXT,
            tipo TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas de nueva gramática - construcciones creadas")
    
    def importar_ejercicios(self):
        """Importar todos los ejercicios"""
        print("📥 Importando ejercicios de nueva gramática - construcciones...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_ejercicios = 0
        count_programas = 0
        count_sintaxis = 0
        count_datos = 0
        
        for archivo in self.base_path.glob("*"):
            nombre = archivo.stem
            contenido = ""
            
            if archivo.suffix == '.py':
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:5000]
                except:
                    pass
            elif archivo.suffix in ['.json']:
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:2000]
                except:
                    contenido = f"Archivo JSON: {archivo.name}"
                db.ejecutar('''
                INSERT INTO datos_construcciones (nombre, contenido, tipo, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, contenido, "json", str(archivo)])
                count_datos += 1
                continue
            
            # Clasificar el archivo
            nombre_lower = nombre.lower()
            
            # Ejercicios de sintaxis avanzada
            if any(p in nombre_lower for p in ['enumeración', 'sintáctica', 'incisos', 'subordinadas', 'modificadores']):
                nivel = "avanzado"
                if "tkinter" in nombre_lower:
                    nivel = "tkinter"
                elif "kivi" in nombre_lower:
                    nivel = "kivy"
                
                db.ejecutar('''
                INSERT INTO ejercicios_sintaxis_avanzada (titulo, contenido, nivel, categoria, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, contenido, nivel, "sintaxis", str(archivo)])
                count_sintaxis += 1
            
            # Programas con interfaz
            elif any(p in nombre_lower for p in ['tkinter', 'kivy', 'pyqt', 'django', 'flask']):
                tecnologia = "desconocida"
                if "tkinter" in nombre_lower:
                    tecnologia = "Tkinter"
                elif "kivy" in nombre_lower:
                    tecnologia = "Kivy"
                elif "pyqt" in nombre_lower:
                    tecnologia = "PyQt"
                elif "django" in nombre_lower:
                    tecnologia = "Django"
                elif "flask" in nombre_lower:
                    tecnologia = "Flask"
                
                db.ejecutar('''
                INSERT INTO programas_construcciones (nombre, descripcion, tecnologia, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, f"Programa con {tecnologia}", tecnologia, contenido, str(archivo)])
                count_programas += 1
            
            # Ejercicios generales
            elif any(p in nombre_lower for p in ['ejercicio', 'practica', 'práctica', 'entrenador', 'gestor']):
                categoria = "general"
                if "comparativa" in nombre_lower:
                    categoria = "comparativas"
                elif "impersonal" in nombre_lower:
                    categoria = "impersonales"
                elif "anticipación" in nombre_lower:
                    categoria = "anticipacion"
                elif "complemento" in nombre_lower:
                    categoria = "complementos"
                elif "colocación" in nombre_lower or "colocaciones" in nombre_lower:
                    categoria = "colocaciones"
                elif "coherencia" in nombre_lower:
                    categoria = "coherencia"
                
                db.ejecutar('''
                INSERT INTO ejercicios_construcciones (titulo, tipo, contenido, categoria, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, "ejercicio", contenido, categoria, str(archivo)])
                count_ejercicios += 1
            
            # Mostrar progreso
            total = count_ejercicios + count_programas + count_sintaxis + count_datos
            if total % 20 == 0 and total > 0:
                print(f"  📖 Procesados {total} archivos...")
        
        print(f"\n📊 Total importados:")
        print(f"  📖 Ejercicios de sintaxis avanzada: {count_sintaxis}")
        print(f"  📚 Programas con interfaz: {count_programas}")
        print(f"  ✏️ Ejercicios generales: {count_ejercicios}")
        print(f"  📄 Datos (JSON): {count_datos}")

if __name__ == '__main__':
    importador = ImportadorNuevaGramaticaConstrucciones()
    importador.importar_ejercicios()
