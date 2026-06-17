#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tecnología y gadgets - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class TecnologiaSQL:
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
            ('¿Qué es un procesador?', 'El cerebro de la computadora'),
            ('¿Qué es la inteligencia artificial?', 'Máquinas que aprenden'),
            ('¿Qué es el internet de las cosas?', 'Dispositivos conectados a internet'),
            ('¿Qué es el 5G?', 'Quinta generación de redes móviles'),
            ('¿Qué es la realidad virtual?', 'Simulación de entornos'),
            ('¿Qué es un algoritmo?', 'Secuencia de pasos para resolver un problema'),
            ('¿Qué es la ciberseguridad?', 'Protección de sistemas informáticos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    t = TecnologiaSQL()
    username = input("Usuario: ").strip()
    t.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            t.practicar()
        else:
            break
if __name__ == '__main__':
    main()
