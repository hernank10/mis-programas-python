#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Medio ambiente - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class AmbienteSQL:
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
            ('¿Qué es el cambio climático?', 'Aumento de la temperatura global'),
            ('¿Qué son las energías renovables?', 'Energías de fuentes naturales'),
            ('¿Qué es la deforestación?', 'Tala de árboles'),
            ('¿Qué es la biodiversidad?', 'Variedad de especies'),
            ('¿Qué es el efecto invernadero?', 'Calentamiento por gases atrapados'),
            ('¿Qué es la contaminación?', 'Introducción de sustancias dañinas'),
            ('¿Qué es el reciclaje?', 'Reutilización de materiales'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    a = AmbienteSQL()
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
