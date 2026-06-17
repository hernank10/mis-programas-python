#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Salud y bienestar - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class SaludSQL:
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
            ('¿Cuánta agua se recomienda beber al día?', '2 litros'),
            ('¿Qué es el ejercicio aeróbico?', 'Ejercicio que aumenta la frecuencia cardíaca'),
            ('¿Qué es la alimentación balanceada?', 'Comer de todos los grupos alimenticios'),
            ('¿Cuántas horas de sueño se recomiendan?', '7-8 horas'),
            ('¿Qué es el estrés?', 'Respuesta del cuerpo a la presión'),
            ('¿Qué es la meditación?', 'Práctica de atención plena'),
            ('¿Qué es el colesterol?', 'Grasa en la sangre'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    s = SaludSQL()
    username = input("Usuario: ").strip()
    s.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            s.practicar()
        else:
            break
if __name__ == '__main__':
    main()
