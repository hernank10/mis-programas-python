#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sopa de letras educativa - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class SopaLetrasSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS sopa_letras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            categoria TEXT DEFAULT 'general',
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM sopa_letras")[0] == 0:
            palabras = [
                ('casa', 'hogar', 1), ('perro', 'animales', 1), ('gato', 'animales', 1),
                ('amigo', 'personas', 1), ('familia', 'personas', 1), ('agua', 'naturaleza', 1),
                ('sol', 'naturaleza', 1), ('luna', 'naturaleza', 1), ('estrella', 'naturaleza', 2),
                ('inteligente', 'adjetivos', 2), ('rapido', 'adjetivos', 2), ('lento', 'adjetivos', 2),
                ('feliz', 'emociones', 1), ('triste', 'emociones', 1), ('fuerte', 'adjetivos', 2),
                ('escuela', 'educacion', 1), ('libro', 'educacion', 1), ('maestro', 'educacion', 1),
            ]
            for p in palabras:
                db.ejecutar('INSERT OR IGNORE INTO sopa_letras (palabra, categoria, nivel) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def jugar(self):
        # Obtener una palabra aleatoria
        palabra = db.consultar_uno('SELECT * FROM sopa_letras ORDER BY RANDOM() LIMIT 1')
        if not palabra:
            print("❌ No hay palabras disponibles")
            return
        
        # Mostrar pista
        print(f"\n🧩 SOPA DE LETRAS")
        print("=" * 40)
        print(f"💡 Pista: {palabra['categoria']} - Nivel {palabra['nivel']}")
        print(f"📏 La palabra tiene {len(palabra['palabra'])} letras")
        
        # Mostrar letras desordenadas
        letras = list(palabra['palabra'])
        random.shuffle(letras)
        print(f"🔤 Letras: {' '.join(letras)}")
        
        respuesta = input("\n✍️ ¿Cuál es la palabra? ").strip()
        
        if respuesta.lower() == palabra['palabra'].lower():
            print("✅ ¡Correcto! 🎉")
        else:
            print(f"❌ La palabra era: {palabra['palabra']}")

def main():
    s = SopaLetrasSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    s.set_usuario(username)
    
    while True:
        print("\n1. Jugar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            s.jugar()
        else:
            break

if __name__ == '__main__':
    main()
