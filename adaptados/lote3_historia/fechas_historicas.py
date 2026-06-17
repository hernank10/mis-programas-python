#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fechas históricas - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class FechasSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS fechas_historicas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT,
            fecha TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM fechas_historicas")[0] == 0:
            eventos = [
                ('Descubrimiento de América', '1492'),
                ('Revolución Francesa', '1789'),
                ('Independencia de Colombia', '1810'),
                ('Primera Guerra Mundial', '1914'),
                ('Segunda Guerra Mundial', '1939'),
                ('Llegada del hombre a la Luna', '1969'),
            ]
            for e in eventos:
                db.ejecutar('INSERT INTO fechas_historicas (evento, fecha) VALUES (?, ?)', e)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        e = db.consultar_uno('SELECT * FROM fechas_historicas ORDER BY RANDOM() LIMIT 1')
        print(f"\n📜 Evento: {e['evento']}")
        resp = input("Fecha: ").strip()
        if resp == e['fecha']:
            print("✅ ¡Correcto!")
        else:
            print(f"❌ La fecha es: {e['fecha']}")

def main():
    f = FechasSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    f.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            f.practicar()
        else:
            break
if __name__ == '__main__':
    main()
