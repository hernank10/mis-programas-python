#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Filosofía y ética - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class FilosofiaSQL:
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
            ('¿Quién es el padre de la filosofía occidental?', 'Sócrates'),
            ('¿Cuál es la frase célebre de Descartes?', 'Pienso, luego existo'),
            ('¿Qué es la ética?', 'Estudio de la moral'),
            ('¿Qué es el utilitarismo?', 'Máxima felicidad para el mayor número'),
            ('¿Quién escribió "El contrato social"?', 'Rousseau'),
            ('¿Qué es el nihilismo?', 'Negación de todo valor'),
            ('¿Quién es el filósofo del "superhombre"?', 'Nietzsche'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    f = FilosofiaSQL()
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
