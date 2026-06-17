#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicios de pronunciación - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class PronunciacionSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS ejercicios_pronunciacion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            fonetica TEXT NOT NULL,
            dificultad INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM ejercicios_pronunciacion")[0] == 0:
            palabras = [
                ('casa', 'kása', 1),
                ('perro', 'péro', 1),
                ('jardín', 'xardín', 2),
                ('llegar', 'ʎeɣár', 2),
                ('murciélago', 'murθjélago', 3),
            ]
            for p in palabras:
                db.ejecutar('INSERT OR IGNORE INTO ejercicios_pronunciacion (palabra, fonetica, dificultad) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        ejercicio = db.consultar_uno('SELECT * FROM ejercicios_pronunciacion ORDER BY RANDOM() LIMIT 1')
        if not ejercicio:
            print("❌ No hay ejercicios")
            return
        
        print(f"\n🗣️ PRONUNCIACIÓN")
        print("=" * 40)
        print(f"📖 Palabra: {ejercicio['palabra']}")
        print(f"🔊 AFI: {ejercicio['fonetica']}")
        print(f"📊 Dificultad: {'⭐' * ejercicio['dificultad']}")
        print("\n💡 Lee la palabra en voz alta y luego escucha la pronunciación ideal.")

def main():
    p = PronunciacionSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    
    while True:
        print("\n1. Practicar pronunciación")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            p.practicar()
        else:
            break

if __name__ == '__main__':
    main()
