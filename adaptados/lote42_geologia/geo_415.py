#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class GeolSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un mineral?', 'Sustancia natural inorgánica'),
            ('¿Qué es una roca?', 'Agregado de minerales'),
            ('¿Qué es el magma?', 'Roca fundida bajo la superficie'),
            ('¿Qué es un volcán?', 'Abertura en la corteza terrestre'),
            ('¿Qué es un terremoto?', 'Movimiento de la corteza terrestre'),
            ('¿Qué es la erosión?', 'Desgaste de la superficie terrestre'),
            ('¿Qué es un fósil?', 'Rastro de vida antigua'),
            ('¿Qué es el suelo?', 'Capa superficial de la Tierra'),
            ('¿Qué es el ciclo de las rocas?', 'Transformación de rocas'),
            ('¿Qué es el relieve?', 'Formas de la superficie terrestre'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    g = GeolSQL()
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': g.practicar()
        else: break
if __name__ == '__main__': main()
