#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Palabras compuestas - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class PalabrasCompuestasSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS palabras_compuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra1 TEXT NOT NULL,
            palabra2 TEXT NOT NULL,
            compuesta TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM palabras_compuestas")[0] == 0:
            compuestas = [
                ('agua', 'ardiente', 'aguardiente'),
                ('casa', 'cuna', 'casacuna'),
                ('pasa', 'tiempo', 'pasatiempo'),
                ('boca', 'abajo', 'bocaabajo'),
                ('saca', 'punta', 'sacapunta'),
                ('rompe', 'olas', 'rompeolas'),
            ]
            for c in compuestas:
                db.ejecutar('INSERT OR IGNORE INTO palabras_compuestas (palabra1, palabra2, compuesta) VALUES (?, ?, ?)', c)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        compuesta = db.consultar_uno('SELECT * FROM palabras_compuestas ORDER BY RANDOM() LIMIT 1')
        if not compuesta:
            print("❌ No hay palabras compuestas disponibles")
            return
        
        print(f"\n🔤 PALABRAS COMPUESTAS")
        print("=" * 40)
        print(f"📖 {compuesta['palabra1']} + {compuesta['palabra2']}")
        
        respuesta = input("\n✍️ ¿Cuál es la palabra compuesta? ").strip()
        
        if respuesta.lower() == compuesta['compuesta'].lower():
            print("✅ ¡Correcto! 🎉")
        else:
            print(f"❌ La palabra compuesta es: {compuesta['compuesta']}")

def main():
    p = PalabrasCompuestasSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            p.practicar()
        else:
            break

if __name__ == '__main__':
    main()
