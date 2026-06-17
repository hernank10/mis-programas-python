#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deportes y recreación - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class DeporteSQL:
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
            ('¿En qué deporte se usa una pelota naranja con hoyuelos?', 'Baloncesto'),
            ('¿Cuántos jugadores tiene un equipo de fútbol?', '11'),
            ('¿Cuál es el deporte más popular del mundo?', 'Fútbol'),
            ('¿Qué deporte se juega en una cancha de arcilla?', 'Tenis'),
            ('¿Cuántos puntos vale un touchdown?', '6'),
            ('¿Qué deporte es la Fórmula 1?', 'Automovilismo'),
            ('¿Cuánto dura un partido de fútbol?', '90 minutos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    d = DeporteSQL()
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
