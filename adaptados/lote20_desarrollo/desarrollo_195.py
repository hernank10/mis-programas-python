#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desarrollo personal - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class DesarrolloSQL:
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
            ('¿Qué es la productividad?', 'Eficiencia en el trabajo'),
            ('¿Qué es un hábito?', 'Acción repetida regularmente'),
            ('¿Qué es la motivación?', 'Impulso para actuar'),
            ('¿Qué es la disciplina?', 'Acción constante y ordenada'),
            ('¿Qué es la resiliencia?', 'Capacidad de superar adversidades'),
            ('¿Qué es la inteligencia emocional?', 'Manejo de emociones'),
            ('¿Qué es la autoestima?', 'Valoración de uno mismo'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    d = DesarrolloSQL()
    username = input("Usuario: ").strip()
    d.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            d.practicar()
        else:
            break
if __name__ == '__main__':
    main()
