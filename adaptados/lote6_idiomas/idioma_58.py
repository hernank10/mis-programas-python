#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idiomas adicionales - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class IdiomaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🗣️ IDIOMAS - PROGRAMA $i")
        print("=" * 40)
        palabras = [
            ('Hola en francés', 'Bonjour'),
            ('Gracias en italiano', 'Grazie'),
            ('Sí en alemán', 'Ja'),
            ('No en francés', 'Non'),
            ('Amor en italiano', 'Amore'),
            ('Paz en alemán', 'Frieden'),
            ('Agua en francés', 'Eau'),
            ('Pan en italiano', 'Pane'),
            ('Casa en alemán', 'Haus'),
            ('Amigo en francés', 'Ami'),
        ]
        import random
        p = random.choice(palabras)
        print(f"\n❓ {p[0]}")
        resp = input("Traducción: ").strip()
        print(f"💡 La traducción es: {p[1]}")

def main():
    i = IdiomaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    i.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            i.practicar()
        else:
            break
if __name__ == '__main__':
    main()
