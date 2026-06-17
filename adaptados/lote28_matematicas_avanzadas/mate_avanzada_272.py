#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class MatAvSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el teorema de Pitágoras?', 'a² + b² = c²'),
            ('¿Qué es el logaritmo?', 'Inversa de la potenciación'),
            ('¿Qué es la derivada?', 'Tasa de cambio'),
            ('¿Qué es una integral?', 'Área bajo la curva'),
            ('¿Qué es un número primo?', 'Divisible solo por 1 y sí mismo'),
            ('¿Qué es el factorial?', 'Producto de enteros consecutivos'),
            ('¿Qué es la probabilidad?', 'Medida de la posibilidad'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    m = MatAvSQL()
    username = input("Usuario: ").strip()
    m.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': m.practicar()
        else: break
if __name__ == '__main__': main()
