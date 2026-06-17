#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cultura general - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CulturaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🎯 CULTURA GENERAL - PROGRAMA $i")
        print("=" * 40)
        preguntas = [
            ('¿Cuántos continentes hay?', '5'),
            ('¿Cuál es el color del cielo?', 'Azul'),
            ('¿Qué animal es conocido como el rey de la selva?', 'León'),
            ('¿Cuántos días tiene una semana?', '7'),
            ('¿Cuántos meses tiene un año?', '12'),
            ('¿Qué es el Big Bang?', 'Origen del universo'),
            ('¿Quién escribió la teoría de la relatividad?', 'Einstein'),
            ('¿Qué es el ADN?', 'Material genético'),
            ('¿Cuál es el planeta más cercano al Sol?', 'Mercurio'),
            ('¿Qué es la gravedad?', 'Fuerza que atrae los objetos'),
        ]
        import random
        p = random.choice(preguntas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")

def main():
    c = CulturaSQL()
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
