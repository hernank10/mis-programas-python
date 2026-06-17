#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IMPORTADOR DE GRAMATICA_CASTELLANA A SQL
Importa todos los programas y ejercicios a la base de datos SQL
Autor: @Hernank10
"""

import os
import sys
import json
import sqlite3
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_manager import db

class ImportadorGramaticaSQL:
    def __init__(self):
        self.base_path = Path("GRAMATICA_CASTELLANA")
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear tablas para gramática"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_gramatica_castellana (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            contenido TEXT,
            tipo TEXT DEFAULT 'ejercicio',
            nivel INTEGER DEFAULT 1,
            archivo_original TEXT
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecciones_castellano (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT,
            categoria TEXT,
            nivel INTEGER DEFAULT 1
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_ortografia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            regla TEXT,
            dificultad INTEGER DEFAULT 1
        )
        ''')
        
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS reglas_gramaticales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            regla TEXT NOT NULL,
            ejemplo TEXT,
            nivel INTEGER DEFAULT 1
        )
        ''')
        
        print("✅ Tablas de gramática creadas")
    
    def importar_ejercicios(self):
        """Importar ejercicios de la carpeta Ejercicios_palabras_diptongos_hiatos_tíldes"""
        carpeta = self.base_path / "Ejercicios_palabras_diptongos_hiatos_tíldes"
        if carpeta.exists():
            print(f"📥 Importando ejercicios de: {carpeta}")
            count = 0
            for archivo in carpeta.glob("*.py"):
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()
                db.ejecutar('''
                INSERT INTO ejercicios_gramatica_castellana (titulo, categoria, contenido, tipo, archivo_original)
                VALUES (?, ?, ?, ?, ?)
                ''', [archivo.stem, "ortografia", contenido[:5000], "ejercicio", str(archivo)])
                count += 1
            print(f"  ✅ Importados {count} ejercicios de ortografía")
    
    def importar_lecciones(self):
        """Importar lecciones de archivos .py sueltos"""
        print("📥 Importando lecciones...")
        archivos = [
            "Este archivo contiene 100 lecciones adicionales de lengua castellana.py",
            "Este es el diccionario3lengacastellana principal que contiene TODAS las 100 lecciones .py",
            "lecciones adicionales de lengua castellana_json.py",
        ]
        
        for archivo in archivos:
            ruta = self.base_path / archivo
            if ruta.exists():
                with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()
                db.ejecutar('''
                INSERT INTO lecciones_castellano (titulo, contenido, categoria)
                VALUES (?, ?, ?)
                ''', [archivo, contenido[:5000], "leccion"])
                print(f"  ✅ Importado: {archivo}")
    
    def importar_reglas_rae(self):
        """Importar reglas de la RAE"""
        print("📥 Importando reglas gramaticales...")
        reglas = [
            ("Ortografía", "La tilde en palabras agudas", "Llevan tilde las palabras agudas terminadas en vocal, -n o -s", 1),
            ("Ortografía", "La tilde en palabras graves", "Llevan tilde las palabras graves que NO terminan en vocal, -n o -s", 1),
            ("Ortografía", "La tilde en palabras esdrújulas", "Todas las palabras esdrújulas llevan tilde", 1),
            ("Sintaxis", "Sujeto y predicado", "El sujeto es quien realiza la acción, el predicado es la acción", 1),
            ("Sintaxis", "Complementos del verbo", "CD, CI, CC, CAgente", 2),
        ]
        for regla in reglas:
            db.ejecutar('''
            INSERT OR IGNORE INTO reglas_gramaticales (categoria, regla, ejemplo, nivel)
            VALUES (?, ?, ?, ?)
            ''', regla)
        print(f"  ✅ Importadas {len(reglas)} reglas gramaticales")
    
    def importar_todo(self):
        """Importar todo"""
        print("=" * 60)
        print("  📥 IMPORTANDO GRAMATICA_CASTELLANA A SQL")
        print("=" * 60)
        
        self.importar_ejercicios()
        self.importar_lecciones()
        self.importar_reglas_rae()
        
        print("\n" + "=" * 60)
        print("✅ IMPORTACIÓN COMPLETADA")
        print("=" * 60)
        
        # Estadísticas
        ejercicios = db.consultar_uno("SELECT COUNT(*) FROM ejercicios_gramatica_castellana")[0]
        lecciones = db.consultar_uno("SELECT COUNT(*) FROM lecciones_castellano")[0]
        reglas = db.consultar_uno("SELECT COUNT(*) FROM reglas_gramaticales")[0]
        
        print(f"📊 Ejercicios importados: {ejercicios}")
        print(f"📊 Lecciones importadas: {lecciones}")
        print(f"📊 Reglas gramaticales: {reglas}")

if __name__ == '__main__':
    importador = ImportadorGramaticaSQL()
    importador.importar_todo()
