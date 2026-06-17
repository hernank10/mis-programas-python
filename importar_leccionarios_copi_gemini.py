#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE LECCIONARIOS COPI Y GEMEINI A SQL
Autor: @Hernank10
"""

import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorLeccionariosCopiGemini:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA/LECCIIONARIOS COPI Y GEMEINI")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para leccionarios Copi y Gemini"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecciones_copi_gemini (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            leccion_id TEXT,
            grado TEXT,
            titulo TEXT,
            contenido TEXT,
            tipo TEXT,
            version TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS sintaxis_quest_edu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grado TEXT,
            leccion_id TEXT,
            titulo TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS documentacion_castellano (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            tipo TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas de leccionarios Copi y Gemini creadas")
    
    def extraer_grado(self, nombre):
        """Extraer el grado del nombre del archivo"""
        patrones = [
            (r'(\d+)[º°]\s*grado', r'\1º Grado'),
            (r'(\d+)[º°]\s*de\s*primaria', r'\1º Primaria'),
            (r'grado\s*(\d+)', r'\1º Grado'),
            (r'primaria', 'Primaria'),
            (r'bachillerato', 'Bachillerato'),
            (r'universitario', 'Universitario'),
            (r'preuniversitario', 'Preuniversitario'),
        ]
        
        for patron, replacement in patrones:
            if re.search(patron, nombre, re.IGNORECASE):
                return replacement
        return "General"
    
    def extraer_leccion_id(self, nombre):
        """Extraer el ID de la lección"""
        match = re.search(r'Lecci[óo]n\s*(\d+)', nombre, re.IGNORECASE)
        if match:
            return match.group(1)
        return None
    
    def detectar_version(self, nombre):
        """Detectar si es Copi o Gemini"""
        if "copi" in nombre.lower():
            return "Copi"
        elif "gem" in nombre.lower() or "gemi" in nombre.lower():
            return "Gemini"
        return "Original"
    
    def importar_lecciones(self):
        """Importar todas las lecciones"""
        print("📥 Importando lecciones Copi y Gemini...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_lecciones = 0
        count_sintaxis = 0
        count_docs = 0
        
        for archivo in self.base_path.glob("*"):
            nombre = archivo.stem
            contenido = ""
            
            # Leer contenido según tipo de archivo
            if archivo.suffix == '.py':
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:5000]
                except:
                    pass
            elif archivo.suffix in ['.docx', '.pdf', '.txt']:
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:2000]
                except:
                    contenido = f"Archivo: {archivo.name}"
            
            # Clasificar el archivo
            if "sintaxis quest" in nombre.lower():
                grado = self.extraer_grado(nombre)
                leccion_id = self.extraer_leccion_id(nombre)
                db.ejecutar('''
                INSERT INTO sintaxis_quest_edu (grado, leccion_id, titulo, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [grado, leccion_id, nombre, contenido, str(archivo)])
                count_sintaxis += 1
            
            elif "lección" in nombre.lower() or "leccion" in nombre.lower():
                grado = self.extraer_grado(nombre)
                leccion_id = self.extraer_leccion_id(nombre)
                version = self.detectar_version(nombre)
                
                db.ejecutar('''
                INSERT INTO lecciones_copi_gemini (leccion_id, grado, titulo, contenido, tipo, version, archivo_original)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', [leccion_id, grado, nombre, contenido, "leccion", version, str(archivo)])
                count_lecciones += 1
            
            elif archivo.suffix in ['.docx', '.pdf', '.txt']:
                db.ejecutar('''
                INSERT INTO documentacion_castellano (titulo, contenido, tipo, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, contenido, archivo.suffix[1:], str(archivo)])
                count_docs += 1
            
            # Mostrar progreso
            total = count_lecciones + count_sintaxis + count_docs
            if total % 10 == 0:
                print(f"  📖 Procesados {total} archivos...")
        
        print(f"\n📊 Total importados:")
        print(f"  📖 Lecciones Copi/Gemini: {count_lecciones}")
        print(f"  📚 Sintaxis Quest EDU: {count_sintaxis}")
        print(f"  📄 Documentación: {count_docs}")

if __name__ == '__main__':
    importador = ImportadorLeccionariosCopiGemini()
    importador.importar_lecciones()
