#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class MusSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es una nota musical?', 'Sonido con altura determinada'),
            ('¿Qué es un acorde?', 'Varias notas sonando juntas'),
            ('¿Quién es Mozart?', 'Compositor clásico'),
            ('¿Qué es la guitarra?', 'Instrumento de cuerda'),
            ('¿Qué es una sinfonía?', 'Composición para orquesta'),
            ('¿Qué es el jazz?', 'Género musical improvisado'),
            ('¿Qué es un coro?', 'Grupo de cantantes'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    m = MusSQL()
    username = input("Usuario: ").strip()
    m.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': m.practicar()
        else: break
if __name__ == '__main__': main()
