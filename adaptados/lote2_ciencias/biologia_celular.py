#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología celular - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class BiologiaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS preguntas_biologia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT,
            respuesta TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM preguntas_biologia")[0] == 0:
            preguntas = [
                ('¿Qué orgánulo es la central energética de la célula?', 'mitocondria'),
                ('¿Qué orgánulo contiene el material genético?', 'núcleo'),
                ('¿Qué orgánulo realiza la fotosíntesis?', 'cloroplasto'),
            ]
            for p in preguntas:
                db.ejecutar('INSERT INTO preguntas_biologia (pregunta, respuesta) VALUES (?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        p = db.consultar_uno('SELECT * FROM preguntas_biologia ORDER BY RANDOM() LIMIT 1')
        print(f"\n🔬 {p['pregunta']}")
        resp = input("Tu respuesta: ").strip()
        if resp.lower() == p['respuesta'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ La respuesta es: {p['respuesta']}")

def main():
    b = BiologiaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    b.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            b.practicar()
        else:
            break
if __name__ == '__main__':
    main()
