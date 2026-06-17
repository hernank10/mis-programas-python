#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La palabra correcta - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class PalabraCorrectaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS palabras_parecidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            incorrecta1 TEXT NOT NULL,
            incorrecta2 TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM palabras_parecidas")[0] == 0:
            parecidas = [
                ('haber', 'aber', 'haver'),
                ('a ver', 'aber', 'haver'),
                ('vaya', 'baya', 'balla'),
                ('halla', 'haya', 'alla'),
                ('echo', 'hecho', 'ejo'),
                ('hecho', 'echo', 'ejo'),
                ('sino', 'sinto', 'cinco'),
                ('si no', 'sino', 'sinó'),
            ]
            for p in parecidas:
                db.ejecutar('INSERT OR IGNORE INTO palabras_parecidas (palabra, incorrecta1, incorrecta2) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def jugar(self):
        palabra = db.consultar_uno('SELECT * FROM palabras_parecidas ORDER BY RANDOM() LIMIT 1')
        if not palabra:
            print("❌ No hay palabras disponibles")
            return
        
        opciones = [palabra['palabra'], palabra['incorrecta1'], palabra['incorrecta2']]
        random.shuffle(opciones)
        
        print(f"\n📝 LA PALABRA CORRECTA")
        print("=" * 40)
        print(f"1. {opciones[0]}")
        print(f"2. {opciones[1]}")
        print(f"3. {opciones[2]}")
        
        respuesta = input("\n✍️ Elige la palabra correcta (1/2/3): ").strip()
        
        try:
            idx = int(respuesta) - 1
            if 0 <= idx < len(opciones) and opciones[idx] == palabra['palabra']:
                print("✅ ¡Correcto! 🎉")
            else:
                print(f"❌ La palabra correcta es: {palabra['palabra']}")
        except:
            print("❌ Opción no válida")

def main():
    p = PalabraCorrectaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    
    while True:
        print("\n1. Jugar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            p.jugar()
        else:
            break

if __name__ == '__main__':
    main()
