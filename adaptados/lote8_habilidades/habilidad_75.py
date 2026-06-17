#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Habilidades blandas - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class HabilidadSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🤝 HABILIDADES - PROGRAMA $i")
        print("=" * 40)
        temas = [
            ('¿Qué es la comunicación asertiva?', 'Expresar ideas con respeto'),
            ('¿Qué es el liderazgo?', 'Guiar a un equipo hacia un objetivo'),
            ('¿Qué es la empatía?', 'Entender los sentimientos de otros'),
            ('¿Qué es la resiliencia?', 'Superar adversidades'),
            ('¿Qué es el trabajo en equipo?', 'Colaboración para lograr metas'),
            ('¿Qué es la inteligencia emocional?', 'Gestionar emociones propias y ajenas'),
        ]
        import random
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu definición: ").strip()
        print(f"💡 {p[1]}")

def main():
    h = HabilidadSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    h.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            h.practicar()
        else:
            break
if __name__ == '__main__':
    main()
