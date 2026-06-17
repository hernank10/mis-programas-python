#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Astronomía y espacio - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class AstronomiaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        temas = [
            ('¿Cuántos planetas hay en el sistema solar?', '8'),
            ('¿Qué es un agujero negro?', 'Región con gravedad extrema'),
            ('¿Qué es una estrella?', 'Cuerpo celeste que emite luz'),
            ('¿Qué es la Vía Láctea?', 'Nuestra galaxia'),
            ('¿Qué es un cometa?', 'Cuerpo de hielo y polvo'),
            ('¿Qué es el Big Bang?', 'Origen del universo'),
            ('¿Cuál es la estrella más cercana?', 'El Sol'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    a = AstronomiaSQL()
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
