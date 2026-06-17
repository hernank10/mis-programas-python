#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class RelSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el cristianismo?', 'Religión basada en Jesús'),
            ('¿Qué es el hinduismo?', 'Religión de la India'),
            ('¿Quién es Zeus?', 'Dios del trueno en la mitología griega'),
            ('¿Qué es el budismo?', 'Enseñanzas de Buda'),
            ('¿Qué es la mitología nórdica?', 'Mitos de los vikingos'),
            ('¿Qué es el islam?', 'Religión del profeta Mahoma'),
            ('¿Quién es Odín?', 'Dios principal en la mitología nórdica'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    r = RelSQL()
    username = input("Usuario: ").strip()
    r.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': r.practicar()
        else: break
if __name__ == '__main__': main()
