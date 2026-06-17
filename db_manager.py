#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gestor central de base de datos SQL para todos los programas
Autor: @Hernank10
"""

import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'lms_educativo.db')

class DBManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
    
    @contextmanager
    def conectar(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    def ejecutar(self, sql, params=None):
        with self.conectar() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            conn.commit()
            return cursor.lastrowid
    
    def consultar(self, sql, params=None):
        with self.conectar() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
    
    def consultar_uno(self, sql, params=None):
        with self.conectar() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchone()

db = DBManager()
print("✅ db_manager.py cargado correctamente")
