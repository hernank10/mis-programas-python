#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programación básica - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ProgramacionSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n💻 PROGRAMACIÓN - PROGRAMA $i")
        print("=" * 40)
        conceptos = [
            ('¿Qué es una variable?', 'Espacio donde se guarda información'),
            ('¿Qué es un bucle?', 'Repetición de código'),
            ('¿Qué es una función?', 'Bloque de código reutilizable'),
            ('¿Qué es un condicional?', 'Toma de decisiones en el código'),
            ('¿Qué es una lista?', 'Colección de elementos'),
            ('¿Qué es un diccionario?', 'Pares clave-valor'),
            ('¿Qué es un bucle for?', 'Iteración sobre una secuencia'),
        ]
        import random
        p = random.choice(conceptos)
        print(f"\n❓ {p[0]}")
        resp = input("Tu definición: ").strip()
        print(f"💡 {p[1]}")

def main():
    p = ProgramacionSQL()
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
