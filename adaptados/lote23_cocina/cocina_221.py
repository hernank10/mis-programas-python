#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class CocSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un sofrito?', 'Base de cebolla, ajo y tomate'),
            ('¿Qué es la paella?', 'Plato de arroz valenciano'),
            ('¿Qué es el ceviche?', 'Pescado marinado en limón'),
            ('¿Qué es un horno de convección?', 'Horno con ventilador'),
            ('¿Qué es un chef?', 'Cocinero profesional'),
            ('¿Qué es la gastronomía?', 'Arte de la cocina'),
            ('¿Qué es el umami?', 'Quinto sabor básico'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    c = CocSQL()
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': c.practicar()
        else: break
if __name__ == '__main__': main()
