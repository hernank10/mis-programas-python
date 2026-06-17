#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Análisis sintáctico de oraciones - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class AnalisisSintacticoSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS oraciones_sintaxis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            oracion TEXT NOT NULL,
            sujeto TEXT NOT NULL,
            predicado TEXT NOT NULL,
            tipo TEXT DEFAULT 'simple',
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM oraciones_sintaxis")[0] == 0:
            oraciones = [
                ('El perro ladra fuerte', 'El perro', 'ladra fuerte', 'simple', 1),
                ('María estudia en la biblioteca', 'María', 'estudia en la biblioteca', 'simple', 1),
                ('Juan y Pedro juegan al fútbol', 'Juan y Pedro', 'juegan al fútbol', 'compuesta', 2),
                ('El libro que leí ayer es interesante', 'El libro', 'que leí ayer es interesante', 'compuesta', 2),
            ]
            for o in oraciones:
                db.ejecutar('INSERT OR IGNORE INTO oraciones_sintaxis (oracion, sujeto, predicado, tipo, nivel) VALUES (?, ?, ?, ?, ?)', o)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def analizar(self):
        oracion = db.consultar_uno('SELECT * FROM oraciones_sintaxis ORDER BY RANDOM() LIMIT 1')
        if not oracion:
            print("❌ No hay oraciones disponibles")
            return
        
        print(f"\n📖 ANÁLISIS SINTÁCTICO")
        print("=" * 40)
        print(f"🔍 Oración: {oracion['oracion']}")
        print(f"👤 Sujeto: {oracion['sujeto']}")
        print(f"⚡ Predicado: {oracion['predicado']}")
        print(f"📊 Tipo: {oracion['tipo']}")
        print(f"📈 Nivel: {oracion['nivel']}")

def main():
    a = AnalisisSintacticoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    a.set_usuario(username)
    
    while True:
        print("\n1. Analizar oración")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            a.analizar()
        else:
            break

if __name__ == '__main__':
    main()
