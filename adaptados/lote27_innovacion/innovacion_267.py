#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class InnSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la innovación?', 'Crear algo nuevo y útil'),
            ('¿Qué es la inteligencia artificial?', 'Máquinas que piensan'),
            ('¿Qué es la robótica?', 'Tecnología de robots'),
            ('¿Qué es la impresión 3D?', 'Crear objetos capa por capa'),
            ('¿Qué es la realidad virtual?', 'Simulación de entornos'),
            ('¿Qué es el Big Data?', 'Grandes volúmenes de datos'),
            ('¿Qué es un drone?', 'Vehículo aéreo no tripulado'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    i = InnSQL()
    username = input("Usuario: ").strip()
    i.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': i.practicar()
        else: break
if __name__ == '__main__': main()
