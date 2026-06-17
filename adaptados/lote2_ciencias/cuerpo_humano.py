#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cuerpo humano - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CuerpoHumanoSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS organos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            sistema TEXT,
            funcion TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM organos")[0] == 0:
            organos = [
                ('Corazón', 'circulatorio', 'Bombear sangre'),
                ('Pulmones', 'respiratorio', 'Intercambio de gases'),
                ('Cerebro', 'nervioso', 'Control del cuerpo'),
                ('Estómago', 'digestivo', 'Digestión de alimentos'),
                ('Hígado', 'digestivo', 'Filtrar toxinas'),
                ('Riñones', 'excretor', 'Filtrar la sangre'),
            ]
            for o in organos:
                db.ejecutar('INSERT INTO organos (nombre, sistema, funcion) VALUES (?, ?, ?)', o)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        o = db.consultar_uno('SELECT * FROM organos ORDER BY RANDOM() LIMIT 1')
        print(f"\n🧠 Órgano: {o['nombre']}")
        print(f"   Sistema: {o['sistema']}")
        print(f"   Función: {o['funcion']}")

def main():
    c = CuerpoHumanoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            c.practicar()
        else:
            break
if __name__ == '__main__':
    main()
