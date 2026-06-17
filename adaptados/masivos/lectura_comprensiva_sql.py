#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicios de lectura comprensiva - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class LecturaComprensivaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS lecturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            texto TEXT NOT NULL,
            preguntas TEXT,
            respuestas TEXT,
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM lecturas")[0] == 0:
            self._cargar_lecturas()
    
    def _cargar_lecturas(self):
        lecturas = [
            ('El perro y el gato', 'Había una vez un perro y un gato que vivían juntos...', 
             '¿Qué animales vivían juntos?', 'perro y gato', 1),
            ('La ciudad', 'La ciudad de Madrid es la capital de España...', 
             '¿Cuál es la capital de España?', 'Madrid', 1),
        ]
        for l in lecturas:
            db.ejecutar('INSERT OR IGNORE INTO lecturas (titulo, texto, preguntas, respuestas, nivel) VALUES (?, ?, ?, ?, ?)', l)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def leer(self):
        lecturas = db.consultar('SELECT id, titulo, texto, preguntas, respuestas FROM lecturas ORDER BY RANDOM() LIMIT 1')
        if not lecturas:
            print("❌ No hay lecturas disponibles")
            return
        
        lectura = lecturas[0]
        print(f"\n📖 {lectura['titulo']}")
        print("=" * 40)
        print(f"\n{lectura['texto']}")
        print(f"\n❓ {lectura['preguntas']}")
        
        respuesta = input("\nTu respuesta: ").strip()
        if respuesta.lower() == lectura['respuestas'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ La respuesta correcta era: {lectura['respuestas']}")

def main():
    l = LecturaComprensivaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    
    while True:
        print("\n1. Leer texto")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            l.leer()
        else:
            break

if __name__ == '__main__':
    main()
