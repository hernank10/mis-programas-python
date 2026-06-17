#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lógica y razonamiento - Programa $i"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class LogicaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print(f"\n🧩 LÓGICA - PROGRAMA $i")
        print("=" * 40)
        acertijos = [
            ('¿Qué es lo que sube y baja pero no se mueve?', 'La temperatura'),
            ('¿Qué tiene llaves pero no puede abrir puertas?', 'El piano'),
            ('¿Qué tiene ojos pero no ve?', 'La aguja'),
            ('¿Qué es más grande que el universo?', 'La imaginación'),
            ('¿Qué es lo que siempre va delante de ti pero nunca ves?', 'El futuro'),
            ('¿Qué tiene agujas pero no cose?', 'El reloj'),
            ('¿Qué es lo que se moja mientras más se seca?', 'La toalla'),
        ]
        import random
        p = random.choice(acertijos)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 La respuesta es: {p[1]}")

def main():
    l = LogicaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            l.practicar()
        else:
            break
if __name__ == '__main__':
    main()
