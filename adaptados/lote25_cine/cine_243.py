#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class CineSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el cine?', 'Arte de la imagen en movimiento'),
            ('¿Quién es Spielberg?', 'Director de cine'),
            ('¿Qué es un guión?', 'Texto de una película'),
            ('¿Qué es el cine de autor?', 'Películas con visión personal'),
            ('¿Qué es un documental?', 'Película de no ficción'),
            ('¿Qué es el cine mudo?', 'Películas sin sonido'),
            ('¿Qué es la dirección de cine?', 'Dirigir la producción'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    c = CineSQL()
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': c.practicar()
        else: break
if __name__ == '__main__': main()
