#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preparación para exámenes - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ExamenSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n📝 EXAMEN - PROGRAMA $i")
        print("=" * 40)
        print("Simulacro de examen (5 preguntas):")
        preguntas = [
            ('1. ¿Cuál es la capital de España?', 'Madrid'),
            ('2. ¿Cuánto es 5 + 7?', '12'),
            ('3. ¿Qué gas respiramos?', 'Oxígeno'),
            ('4. ¿Cuál es el planeta más grande?', 'Júpiter'),
            ('5. ¿Quién escribió "Don Quijote"?', 'Cervantes'),
        ]
        aciertos = 0
        for p in preguntas:
            print(f"\n❓ {p[0]}")
            resp = input("Tu respuesta: ").strip()
            if resp.lower() == p[1].lower():
                print("✅ Correcto")
                aciertos += 1
            else:
                print(f"❌ La respuesta es: {p[1]}")
        print(f"\n🏆 Puntaje: {aciertos}/{len(preguntas)}")

def main():
    e = ExamenSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            e.practicar()
        else:
            break
if __name__ == '__main__':
    main()
