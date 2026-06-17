#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE NUEVOS JUEGOS II A SQL
Autor: @Hernank10
"""

import os
import sys
import re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorNuevosJuegos:
    def __init__(self):
        self.base_path = Path("NUEVOS JUEGOS II")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para juegos"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS juegos_sintaxis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tipo TEXT,
            categoria TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS juegos_bilingues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            tecnologia TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS juegos_consola (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            num_ejercicios INTEGER DEFAULT 0,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS juegos_pygame (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            contenido TEXT,
            archivo_original TEXT
        )
        ''')
        
        print("✅ Tablas de juegos creadas")
    
    def importar_juegos(self):
        """Importar todos los juegos"""
        print("📥 Importando NUEVOS JUEGOS II...")
        
        if not self.base_path.exists():
            print(f"❌ No se encontró la carpeta: {self.base_path}")
            return
        
        count_sintaxis = 0
        count_bilingues = 0
        count_consola = 0
        count_pygame = 0
        
        # Importar juegos principales
        for archivo in self.base_path.glob("*.py"):
            nombre = archivo.stem
            contenido = ""
            
            try:
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()[:3000]
            except:
                pass
            
            nombre_lower = nombre.lower()
            
            # Clasificar
            if "sintáctico" in nombre_lower or "sintactico" in nombre_lower:
                db.ejecutar('''
                INSERT INTO juegos_sintaxis (nombre, descripcion, tipo, categoria, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', [nombre, "Juego de sintaxis", "sintaxis", "general", contenido, str(archivo)])
                count_sintaxis += 1
            
            elif "bilingüe" in nombre_lower or "bilingue" in nombre_lower or "español" in nombre_lower:
                db.ejecutar('''
                INSERT INTO juegos_bilingues (nombre, descripcion, tecnologia, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, "Juego bilingüe", "varios", contenido, str(archivo)])
                count_bilingues += 1
            
            elif "consola" in nombre_lower:
                num_ejercicios = 0
                if "4" in nombre:
                    num_ejercicios = 4
                elif "5" in nombre:
                    num_ejercicios = 5
                elif "6" in nombre:
                    num_ejercicios = 6
                elif "7" in nombre:
                    num_ejercicios = 7
                
                db.ejecutar('''
                INSERT INTO juegos_consola (nombre, descripcion, num_ejercicios, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, "Juego de consola", num_ejercicios, contenido, str(archivo)])
                count_consola += 1
            
            elif "pygame" in nombre_lower or "pygame" in contenido.lower():
                db.ejecutar('''
                INSERT INTO juegos_pygame (nombre, descripcion, contenido, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, "Juego con Pygame", contenido, str(archivo)])
                count_pygame += 1
            
            else:
                # Juego general
                db.ejecutar('''
                INSERT INTO juegos_sintaxis (nombre, descripcion, tipo, categoria, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', [nombre, "Juego educativo", "general", "general", contenido, str(archivo)])
                count_sintaxis += 1
        
        # Importar juegos bilingües (subcarpeta)
        bilingue_path = self.base_path / "bilingües" / "Nuevas aplicaciones bilingües español-inglés pygame y kivi"
        if bilingue_path.exists():
            print("  📥 Importando juegos bilingües...")
            for archivo in bilingue_path.glob("*.py"):
                nombre = archivo.stem
                contenido = ""
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:3000]
                except:
                    pass
                
                db.ejecutar('''
                INSERT INTO juegos_bilingues (nombre, descripcion, tecnologia, contenido, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [nombre, "Juego bilingüe español-inglés", "pygame/kivy", contenido, str(archivo)])
                count_bilingues += 1
        
        # Importar juegos de pygame (subcarpeta)
        pygame_path = self.base_path / "pygame" / "APLICACIONES juegos pygame de inglés-español de sintaxis con python"
        if pygame_path.exists():
            print("  📥 Importando juegos Pygame...")
            for archivo in pygame_path.glob("*.py"):
                nombre = archivo.stem
                contenido = ""
                try:
                    with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()[:3000]
                except:
                    pass
                
                db.ejecutar('''
                INSERT INTO juegos_pygame (nombre, descripcion, contenido, archivo_original)
                VALUES (?, ?, ?, ?)
                ''', [nombre, "Juego Pygame bilingüe", contenido, str(archivo)])
                count_pygame += 1
        
        print(f"\n📊 Total importados:")
        print(f"  🎮 Juegos de sintaxis: {count_sintaxis}")
        print(f"  🌐 Juegos bilingües: {count_bilingues}")
        print(f"  💻 Juegos de consola: {count_consola}")
        print(f"  🎨 Juegos Pygame: {count_pygame}")

if __name__ == '__main__':
    importador = ImportadorNuevosJuegos()
    importador.importar_juegos()
