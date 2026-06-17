#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class GenSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el ADN?', 'Material genético'),
            ('¿Qué es un gen?', 'Unidad de herencia'),
            ('¿Qué es un cromosoma?', 'Estructura que contiene genes'),
            ('¿Qué es la herencia?', 'Transmisión de características'),
            ('¿Qué es la mutación?', 'Cambio en el ADN'),
            ('¿Qué es la genética?', 'Estudio de la herencia'),
            ('¿Qué es un alelo?', 'Forma alternativa de un gen'),
            ('¿Qué es el genoma?', 'Conjunto de genes de un organismo'),
            ('¿Qué es la biotecnología?', 'Uso de organismos para tecnología'),
            ('¿Qué es la ingeniería genética?', 'Manipulación del ADN'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    g = GenSQL()
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': g.practicar()
        else: break
if __name__ == '__main__': main()
