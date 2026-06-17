#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capitales del mundo - Versión SQL"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CapitalesSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS capitales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pais TEXT,
            capital TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM capitales")[0] == 0:
            paises = [
                ('España', 'Madrid'), ('Francia', 'París'), ('Italia', 'Roma'),
                ('Alemania', 'Berlín'), ('Reino Unido', 'Londres'),
                ('Portugal', 'Lisboa'), ('Colombia', 'Bogotá'),
                ('Argentina', 'Buenos Aires'), ('México', 'Ciudad de México'),
                ('Japón', 'Tokio'), ('China', 'Pekín'), ('India', 'Nueva Delhi'),
                ('Australia', 'Canberra'), ('Canadá', 'Ottawa'),
                ('Estados Unidos', 'Washington DC'),
            ]
            for p in paises:
                db.ejecutar('INSERT INTO capitales (pais, capital) VALUES (?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        c = db.consultar_uno('SELECT * FROM capitales ORDER BY RANDOM() LIMIT 1')
        print(f"\n🌍 País: {c['pais']}")
        resp = input("Capital: ").strip()
        if resp.lower() == c['capital'].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ La capital es: {c['capital']}")

def main():
    c = CapitalesSQL()
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
