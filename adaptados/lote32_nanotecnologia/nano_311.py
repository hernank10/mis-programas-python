#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class NanoSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un nanómetro?', 'Una milmillonésima parte de un metro'),
            ('¿Qué es la nanotecnología?', 'Tecnología a escala atómica'),
            ('¿Qué son los nanotubos?', 'Estructuras de carbono a nanoescala'),
            ('¿Qué es un nanorobot?', 'Robot a escala nanométrica'),
            ('¿Qué aplicaciones tiene la nanotecnología?', 'Medicina, electrónica, materiales'),
            ('¿Qué es la nanoelectrónica?', 'Electrónica a escala nanométrica'),
            ('¿Qué es la nanomedicina?', 'Medicina a escala nanométrica'),
            ('¿Qué es un punto cuántico?', 'Partícula nanoscópica'),
            ('¿Qué es el grafeno?', 'Material de carbono a nanoescala'),
            ('¿Qué es un nanomaterial?', 'Material con estructuras nanométricas'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    n = NanoSQL()
    username = input("Usuario: ").strip()
    n.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': n.practicar()
        else: break
if __name__ == '__main__': main()
