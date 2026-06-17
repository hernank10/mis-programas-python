#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Historia y geografía - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class HistoriaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🌍 HISTORIA - PROGRAMA $i")
        print("=" * 40)
        preguntas = [
            ('¿Quién descubrió América?', 'Cristóbal Colón'),
            ('¿Qué civilización construyó Machu Picchu?', 'Inca'),
            ('¿En qué año cayó el Imperio Romano?', '476'),
            ('¿Qué país tiene la mayor población del mundo?', 'India'),
            ('¿Cuál es el río más largo del mundo?', 'Amazonas'),
            ('¿Cuál es la montaña más alta del mundo?', 'Everest'),
            ('¿Qué océano es el más grande?', 'Pacífico'),
            ('¿Cuál es el país más grande del mundo?', 'Rusia'),
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
    h = HistoriaSQL()
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
