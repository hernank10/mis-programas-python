#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arte y diseño - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ArteSQL:
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
            ('¿Quién pintó La Mona Lisa?', 'Da Vinci'),
            ('¿Qué es el cubismo?', 'Arte con formas geométricas'),
            ('¿Quién es el autor de La Noche Estrellada?', 'Van Gogh'),
            ('¿Qué es el diseño gráfico?', 'Comunicación visual'),
            ('¿Qué es el arte abstracto?', 'Arte sin representación figurativa'),
            ('¿Quién es el artista del Guernica?', 'Picasso'),
            ('¿Qué es el minimalismo?', 'Simplicidad y funcionalidad'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    a = ArteSQL()
    username = input("Usuario: ").strip()
    a.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            a.practicar()
        else:
            break
if __name__ == '__main__':
    main()
