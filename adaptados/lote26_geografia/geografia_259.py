#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class GeoSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un río?', 'Corriente de agua natural'),
            ('¿Qué es una montaña?', 'Elevación del terreno'),
            ('¿Qué es un desierto?', 'Zona árida'),
            ('¿Qué es la lluvia?', 'Precipitación de agua'),
            ('¿Qué es un glaciar?', 'Masa de hielo'),
            ('¿Qué es un bosque?', 'Área con muchos árboles'),
            ('¿Qué es un volcán?', 'Abertura en la corteza terrestre'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    g = GeoSQL()
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': g.practicar()
        else: break
if __name__ == '__main__': main()
