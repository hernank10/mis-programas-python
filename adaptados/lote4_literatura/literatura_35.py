#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Literatura y arte - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class LiteraturaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n📚 LITERATURA - PROGRAMA $i")
        print("=" * 40)
        preguntas = [
            ('¿Quién escribió "La Odisea"?', 'Homero'),
            ('¿Quién pintó "La Mona Lisa"?', 'Da Vinci'),
            ('¿Quién es el autor de "El Principito"?', 'Saint-Exupéry'),
            ('¿Qué estilo pictórico usó Picasso?', 'Cubismo'),
            ('¿Quién escribió "1984"?', 'George Orwell'),
            ('¿Qué obra escribió Julio Cortázar?', 'Rayuela'),
            ('¿Quién es el padre del realismo mágico?', 'García Márquez'),
        ]
        import random
        p = random.choice(preguntas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        if resp.lower() == p[1].lower():
            print("✅ ¡Correcto!")
        else:
            print(f"❌ La respuesta es: {p[1]}")

def main():
    l = LiteraturaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            l.practicar()
        else:
            break
if __name__ == '__main__':
    main()
