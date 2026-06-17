#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE LECCIONES DE GRAMÁTICA-CURSOS A SQL
Autor: @Hernank10
"""

import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorLeccionesGramaticaCursos:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA/LECCIONES DE GRMATICA-CURSOS")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para lecciones de gramática-cursos"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecciones_gramatica_cursos (
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
        CREATE TABLE IF NOT EXISTS sintaxis_quest_cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grado TEXT,
            leccion_id TEXT,
            titulo TEXT,
            contenido TEXT,
            archivo_original TEXT,
            version TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS menus_lecciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            leccion_id TEXT,
            grado TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas de lecciones de gramática-cursos creadas")
    
    def extraer_grado(self, nombre):
        """Extraer el grado del nombre del archivo"""
        patrones = [
            (r'(\d+)[º°]\s*grado', r'\1º Grado'),
            (r'(\d+)[º°]\s*de\s*primaria', r'\1º Primaria'),
            (r'(\d+)[º°]\s*secundaria', r'\1º Secundaria'),
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
    
    def importar_lecciones(self):
        """Importar todas las lecciones"""
        print("📥 Importando lecciones de gramática-cursos...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_lecciones = 0
        count_sintaxis = 0
        count_menus = 0
        
        for archivo in self.base_path.glob("*"):
            nombre = archivo.stem
            contenido = ""
            
            if archivo.suffix == '.py':
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:5000]
                except:
                    pass
            elif archivo.suffix in ['.docx']:
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:2000]
                except:
                    contenido = f"Archivo: {archivo.name}"
            
            # Clasificar el archivo
            if "sintaxis quest" in nombre.lower():
                grado = self.extraer_grado(nombre)
                leccion_id = self.extraer_leccion_id(nombre)
                
                # Detectar versión
                version = "Original"
                if "tkinter" in nombre.lower():
                    version = "Tkinter"
                elif "kivi" in nombre.lower():
                    version = "Kivy"
                elif "mejorado" in nombre.lower():
                    version = "Mejorado"
                
                db.ejecutar('''
                INSERT INTO sintaxis_quest_cursos (grado, leccion_id, titulo, contenido, archivo_original, version)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', [grado, leccion_id, nombre, contenido, str(archivo), version])
                count_sintaxis += 1
            
            elif "menú" in nombre.lower() or "menu" in nombre.lower():
                leccion_id = self.extraer_leccion_id(nombre)
                grado = self.extraer_grado(nombre)
                
                db.ejecutar('''
                INSERT INTO menus_lecciones (titulo, contenido, leccion_id, grado, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, contenido, leccion_id, grado, str(archivo)])
                count_menus += 1
            
            elif "lección" in nombre.lower() or "leccion" in nombre.lower():
                grado = self.extraer_grado(nombre)
                leccion_id = self.extraer_leccion_id(nombre)
                
                # Determinar categoría
                categoria = "general"
                if "argumento" in nombre.lower():
                    categoria = "argumentacion"
                elif "verbo" in nombre.lower():
                    categoria = "verbos"
                elif "sustantivo" in nombre.lower():
                    categoria = "sustantivos"
                elif "predicado" in nombre.lower():
                    categoria = "predicado"
                elif "sujeto" in nombre.lower():
                    categoria = "sujeto"
                elif "complemento" in nombre.lower():
                    categoria = "complementos"
                elif "conector" in nombre.lower():
                    categoria = "conectores"
                
                db.ejecutar('''
                INSERT INTO lecciones_gramatica_cursos (leccion_id, grado, titulo, contenido, tipo, archivo_original, categoria)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', [leccion_id, grado, nombre, contenido, "leccion", str(archivo), categoria])
                count_lecciones += 1
            
            # Mostrar progreso
            total = count_lecciones + count_sintaxis + count_menus
            if total % 20 == 0 and total > 0:
                print(f"  📖 Procesados {total} archivos...")
        
        print(f"\n📊 Total importados:")
        print(f"  📖 Lecciones: {count_lecciones}")
        print(f"  📚 Sintaxis Quest: {count_sintaxis}")
        print(f"  📋 Menús: {count_menus}")

if __name__ == '__main__':
    importador = ImportadorLeccionesGramaticaCursos()
    importador.importar_lecciones()
