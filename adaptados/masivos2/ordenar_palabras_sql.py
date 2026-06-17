#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ordenar palabras - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class OrdenarPalabrasSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS palabras_desordenadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM palabras_desordenadas")[0] == 0:
            palabras = [
                ('casa', 1), ('perro', 1), ('gato', 1), ('amigo', 1), ('familia', 1),
                ('inteligente', 2), ('responsabilidad', 2), ('computadora', 2),
                ('felicidad', 2), ('amistad', 2), ('conocimiento', 3), ('maravilloso', 3),
            ]
            for p in palabras:
                db.ejecutar('INSERT OR IGNORE INTO palabras_desordenadas (palabra, nivel) VALUES (?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def jugar(self):
        palabra = db.consultar_uno('SELECT * FROM palabras_desordenadas ORDER BY RANDOM() LIMIT 1')
        if not palabra:
            print("❌ No hay palabras disponibles")
            return
        
        letras = list(palabra['palabra'])
        random.shuffle(letras)
        
        print(f"\n🔤 ORDENAR PALABRAS")
        print("=" * 40)
        print(f"📊 Nivel: {'⭐' * palabra['nivel']}")
        print(f"🔤 Letras: {' '.join(letras)}")
        
        respuesta = input("\n✍️ ¿Cuál es la palabra? ").strip()
        
        if respuesta.lower() == palabra['palabra'].lower():
            print("✅ ¡Correcto! 🎉")
        else:
            print(f"❌ La palabra era: {palabra['palabra']}")

def main():
    o = OrdenarPalabrasSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    o.set_usuario(username)
    
    while True:
        print("\n1. Jugar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            o.jugar()
        else:
            break

if __name__ == '__main__':
    main()
