#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comunicación y medios - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ComunicacionSQL:
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
            ('¿Qué es el periodismo?', 'Difusión de información'),
            ('¿Qué es la publicidad?', 'Promoción de productos'),
            ('¿Qué es una red social?', 'Plataforma de interacción en línea'),
            ('¿Qué es la comunicación no verbal?', 'Comunicación sin palabras'),
            ('¿Qué es un medio de comunicación?', 'Canal de difusión de información'),
            ('¿Qué es el marketing digital?', 'Estrategias de promoción en internet'),
            ('¿Qué es un influencer?', 'Persona con influencia en redes'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    c = ComunicacionSQL()
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
