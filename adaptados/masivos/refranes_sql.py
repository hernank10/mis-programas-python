#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aprender refranes y expresiones - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class RefranesSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS refranes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            refran TEXT NOT NULL,
            significado TEXT NOT NULL,
            categoria TEXT DEFAULT 'popular'
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM refranes")[0] == 0:
            refranes = [
                ('No hay mal que por bien no venga', 'Todo problema puede traer algo bueno', 'popular'),
                ('En boca cerrada no entran moscas', 'Es mejor callar para evitar problemas', 'popular'),
                ('Al que madruga, Dios le ayuda', 'Los que se esfuerzan temprano tienen éxito', 'popular'),
                ('Más vale pájaro en mano que ciento volando', 'Es mejor tener algo seguro que arriesgarse', 'popular'),
                ('La práctica hace al maestro', 'La repetición lleva a la perfección', 'popular'),
            ]
            for r in refranes:
                db.ejecutar('INSERT OR IGNORE INTO refranes (refran, significado, categoria) VALUES (?, ?, ?)', r)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def aprender(self):
        refran = db.consultar_uno('SELECT * FROM refranes ORDER BY RANDOM() LIMIT 1')
        if not refran:
            print("❌ No hay refranes disponibles")
            return
        
        print(f"\n📖 REFRANES")
        print("=" * 40)
        print(f"📜 Refrán: {refran['refran']}")
        print(f"📝 Significado: {refran['significado']}")
        print(f"📂 Categoría: {refran['categoria']}")

def main():
    r = RefranesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    r.set_usuario(username)
    
    while True:
        print("\n1. Aprender refrán")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            r.aprender()
        else:
            break

if __name__ == '__main__':
    main()
