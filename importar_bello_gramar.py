#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE BELLO GRAMAR A SQL
Autor: @Hernank10
"""

import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorBelloGramar:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA/bello_gramar/Bello Gramar")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para Bello Gramar"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_sintaxis_bello (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            tipo TEXT,
            categoria TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS comparacion_igualdad (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            tecnologia TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS enumeracion_sintactica (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            tipo TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas de Bello Gramar creadas")
    
    def importar_bello_gramar(self):
        """Importar todos los archivos de Bello Gramar"""
        print("📥 Importando Bello Gramar...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_sintaxis = 0
        
        for archivo in self.base_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:5000]
            except:
                pass
            
            # Clasificar
            categoria = "general"
            if "estructurar" in nombre.lower() or "estructura" in nombre.lower():
                categoria = "estructura"
            elif "sintactica" in nombre.lower() or "sintáctica" in nombre.lower():
                categoria = "sintaxis"
            elif "practicar" in nombre.lower() or "practica" in nombre.lower():
                categoria = "practica"
            elif "educativo" in nombre.lower():
                categoria = "educativo"
            
            db.ejecutar('''
            INSERT INTO ejercicios_sintaxis_bello (titulo, contenido, tipo, categoria, archivo_original)
            VALUES (?, ?, ?, ?, ?)
            ''', [nombre, contenido, "ejercicio", categoria, str(archivo)])
            count_sintaxis += 1
        
        print(f"  ✅ Importados {count_sintaxis} ejercicios de sintaxis")
    
    def importar_comparacion(self):
        """Importar ejercicios de comparación de igualdad"""
        print("\n📥 Importando Comparación de Igualdad...")
        
        comp_path = self.base_path / "Nueva gramática_ejercicicios_construcciones" / "Comparación de Igualdad"
        if not comp_path.exists():
            print("  ⚠️ No se encontró la carpeta Comparación de Igualdad")
            return
        
        count = 0
        for archivo in comp_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:5000]
            except:
                pass
            
            tecnologia = "desconocida"
            if "kivy" in nombre.lower():
                tecnologia = "Kivy"
            elif "android" in nombre.lower():
                tecnologia = "Android"
            
            db.ejecutar('''
            INSERT INTO comparacion_igualdad (titulo, contenido, tecnologia, archivo_original)
            VALUES (?, ?, ?, ?)
            ''', [nombre, contenido, tecnologia, str(archivo)])
            count += 1
        
        print(f"  ✅ Importados {count} ejercicios de comparación")
    
    def importar_enumeracion(self):
        """Importar ejercicios de enumeración sintáctica"""
        print("\n📥 Importando Enumeración Sintáctica...")
        
        enum_path = self.base_path / "Nueva gramática_ejercicicios_construcciones" / "Enumeracion_Sintactica_Interactivo"
        if not enum_path.exists():
            print("  ⚠️ No se encontró la carpeta Enumeracion_Sintactica_Interactivo")
            return
        
        count = 0
        for archivo in enum_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:5000]
            except:
                pass
            
            tipo = "general"
            if "tkinter" in nombre.lower():
                tipo = "Tkinter"
            elif "preguntas" in nombre.lower() or "cuestionario" in nombre.lower():
                tipo = "cuestionario"
            elif "gestor" in nombre.lower():
                tipo = "gestor"
            elif "practicador" in nombre.lower() or "entrenador" in nombre.lower():
                tipo = "practicador"
            
            db.ejecutar('''
            INSERT INTO enumeracion_sintactica (titulo, contenido, tipo, archivo_original)
            VALUES (?, ?, ?, ?)
            ''', [nombre, contenido, tipo, str(archivo)])
            count += 1
        
        print(f"  ✅ Importados {count} ejercicios de enumeración sintáctica")

if __name__ == '__main__':
    importador = ImportadorBelloGramar()
    importador.importar_bello_gramar()
    importador.importar_comparacion()
    importador.importar_enumeracion()
