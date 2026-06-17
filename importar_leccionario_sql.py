#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE LECCIONARIO DE LA LENGUA CASTELLANA A SQL
Autor: @Hernank10
"""

import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorLeccionarioSQL:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA/LECCIONARIO DE LA LENGUA CASTELLANA")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para el leccionario"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecciones_castellano_grados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            leccion_id TEXT,
            grado TEXT,
            titulo TEXT,
            contenido TEXT,
            tipo TEXT,
            archivo_original TEXT,
            categoria TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS programas_castellano (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_castellano_avanzados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            nivel TEXT,
            categoria TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas del leccionario creadas")
    
    def extraer_grado(self, nombre):
        """Extraer el grado del nombre del archivo"""
        patrones = [
            (r'(\d+)[º°]\s*grado', r'\1º Grado'),
            (r'(\d+)[º°]\s*de\s*primaria', r'\1º Primaria'),
            (r'grado\s*(\d+)', r'\1º Grado'),
            (r'primaria', 'Primaria'),
            (r'bachillerato', 'Bachillerato'),
            (r'universitario', 'Universitario'),
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
    
    def extraer_titulo(self, nombre):
        """Extraer el título de la lección"""
        # Eliminar prefijos comunes
        titulo = nombre
        titulo = re.sub(r'^Código Python – ', '', titulo)
        titulo = re.sub(r'^Lección\s*\d+\s*[-–]\s*', '', titulo)
        titulo = re.sub(r'\.py$', '', titulo)
        return titulo[:100]
    
    def importar_lecciones(self):
        """Importar todas las lecciones"""
        print("📥 Importando lecciones de lengua castellana...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_lecciones = 0
        count_programas = 0
        
        for archivo in self.base_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:5000]
            except:
                pass
            
            # Clasificar el archivo
            if "lección" in nombre.lower() or "leccion" in nombre.lower():
                grado = self.extraer_grado(nombre)
                leccion_id = self.extraer_leccion_id(nombre)
                titulo = self.extraer_titulo(nombre)
                
                db.ejecutar('''
                INSERT INTO lecciones_castellano_grados (leccion_id, grado, titulo, contenido, tipo, archivo_original)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', [leccion_id, grado, titulo, contenido, "leccion", str(archivo)])
                count_lecciones += 1
                
                if count_lecciones % 10 == 0:
                    print(f"  📖 Importadas {count_lecciones} lecciones...")
            
            elif any(p in nombre.lower() for p in ['práctica', 'practica', 'entrenador', 'tutor', 'centro']):
                db.ejecutar('''
                INSERT INTO programas_castellano (nombre, descripcion, contenido, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, f"Programa educativo: {nombre}", contenido, str(archivo)])
                count_programas += 1
            
            else:
                # Otros ejercicios
                db.ejecutar('''
                INSERT INTO ejercicios_castellano_avanzados (titulo, contenido, categoria, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, contenido, "general", str(archivo)])
        
        print(f"\n📊 Total importados:")
        print(f"  📖 Lecciones: {count_lecciones}")
        print(f"  📚 Programas: {count_programas}")

if __name__ == '__main__':
    importador = ImportadorLeccionarioSQL()
    importador.importar_lecciones()
