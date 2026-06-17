#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Elementos químicos - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class QuimicaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS elementos_quimicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            simbolo TEXT,
            numero INTEGER
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM elementos_quimicos")[0] == 0:
            elementos = [
                ('Hidrógeno', 'H', 1), ('Helio', 'He', 2), ('Litio', 'Li', 3),
                ('Carbono', 'C', 6), ('Oxígeno', 'O', 8), ('Hierro', 'Fe', 26),
                ('Oro', 'Au', 79), ('Plata', 'Ag', 47), ('Plomo', 'Pb', 82),
            ]
            for e in elementos:
                db.ejecutar('INSERT INTO elementos_quimicos (nombre, simbolo, numero) VALUES (?, ?, ?)', e)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        e = db.consultar_uno('SELECT * FROM elementos_quimicos ORDER BY RANDOM() LIMIT 1')
        print(f"\n🧪 Elemento: {e['nombre']} (Nº {e['numero']})")
        resp = input("Símbolo: ").strip()
        if resp.upper() == e['simbolo']:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ El símbolo es: {e['simbolo']}")

def main():
    q = QuimicaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    q.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            q.practicar()
        else:
            break
if __name__ == '__main__':
    main()
