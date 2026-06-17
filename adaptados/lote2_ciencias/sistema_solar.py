#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sistema solar - Versión SQL"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class SistemaSolarSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS planetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            tipo TEXT,
            lunas INTEGER
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM planetas")[0] == 0:
            planetas = [
                ('Mercurio', 'rocoso', 0), ('Venus', 'rocoso', 0),
                ('Tierra', 'rocoso', 1), ('Marte', 'rocoso', 2),
                ('Júpiter', 'gaseoso', 95), ('Saturno', 'gaseoso', 146),
                ('Urano', 'gaseoso', 27), ('Neptuno', 'gaseoso', 16),
            ]
            for p in planetas:
                db.ejecutar('INSERT INTO planetas (nombre, tipo, lunas) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        p = db.consultar_uno('SELECT * FROM planetas ORDER BY RANDOM() LIMIT 1')
        print(f"\n🪐 Planeta: {p['nombre']}")
        print(f"   Tipo: {p['tipo']}")
        print(f"   Lunas: {p['lunas']}")

def main():
    s = SistemaSolarSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    s.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            s.practicar()
        else:
            break
if __name__ == '__main__':
    main()
