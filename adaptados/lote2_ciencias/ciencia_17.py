#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ciencias naturales - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CienciaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🔬 CIENCIA - PROGRAMA $i")
        print("=" * 40)
        print("📝 Pregunta de ciencias naturales")
        print("Responde con el término correcto.")
        
        preguntas = [
            ('¿Qué planeta es conocido como el planeta rojo?', 'Marte'),
            ('¿Qué gas respiramos?', 'Oxígeno'),
            ('¿Qué órgano bombea la sangre?', 'Corazón'),
            ('¿Qué partícula está en el núcleo del átomo?', 'Protón'),
            ('¿Qué proceso usan las plantas para hacer su alimento?', 'Fotosíntesis'),
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
    c = CienciaSQL()
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
