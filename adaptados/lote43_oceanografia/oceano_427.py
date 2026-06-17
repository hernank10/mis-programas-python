#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class OceSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el océano?', 'Gran masa de agua salada'),
            ('¿Qué es una corriente marina?', 'Flujo de agua en el océano'),
            ('¿Qué es la marea?', 'Subida y bajada del nivel del mar'),
            ('¿Qué es el plancton?', 'Organismos microscópicos marinos'),
            ('¿Qué es un arrecife?', 'Estructura de coral'),
            ('¿Qué es la fosa oceánica?', 'Depresión profunda en el fondo marino'),
            ('¿Qué es el fitoplancton?', 'Organismos vegetales marinos'),
            ('¿Qué es el zooplancton?', 'Organismos animales marinos'),
            ('¿Qué es la contaminación marina?', 'Contaminación de los océanos'),
            ('¿Qué es la acidificación del océano?', 'Disminución del pH del océano'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    o = OceSQL()
    username = input("Usuario: ").strip()
    o.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': o.practicar()
        else: break
if __name__ == '__main__': main()
