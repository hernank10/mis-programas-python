#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Autores famosos - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class AutoresSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            obra TEXT,
            nacionalidad TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM autores")[0] == 0:
            autores = [
                ('Miguel de Cervantes', 'Don Quijote', 'Española'),
                ('Gabriel García Márquez', 'Cien años de soledad', 'Colombiana'),
                ('Federico García Lorca', 'Bodas de sangre', 'Española'),
                ('Pablo Neruda', 'Veinte poemas de amor', 'Chilena'),
                ('Jorge Luis Borges', 'Ficciones', 'Argentina'),
                ('Mario Vargas Llosa', 'La ciudad y los perros', 'Peruana'),
                ('William Shakespeare', 'Hamlet', 'Inglesa'),
                ('Fiódor Dostoyevski', 'Crimen y castigo', 'Rusa'),
            ]
            for a in autores:
                db.ejecutar('INSERT INTO autores (nombre, obra, nacionalidad) VALUES (?, ?, ?)', a)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        a = db.consultar_uno('SELECT * FROM autores ORDER BY RANDOM() LIMIT 1')
        print(f"\n📖 Autor: {a['nombre']}")
        print(f"   Obra: {a['obra']}")
        print(f"   Nacionalidad: {a['nacionalidad']}")

def main():
    a = AutoresSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    a.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            a.practicar()
        else:
            break
if __name__ == '__main__':
    main()
