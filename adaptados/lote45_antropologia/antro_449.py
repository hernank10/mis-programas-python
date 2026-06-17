#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class AntSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la antropología?', 'Estudio de la humanidad'),
            ('¿Qué es la cultura?', 'Conjunto de costumbres y creencias'),
            ('¿Qué es la sociedad?', 'Grupo de personas que viven juntas'),
            ('¿Qué es el lenguaje?', 'Sistema de comunicación humana'),
            ('¿Qué es la religión?', 'Sistema de creencias'),
            ('¿Qué es la alimentación?', 'Hábitos de consumo de alimentos'),
            ('¿Qué es la vestimenta?', 'Ropa utilizada por una cultura'),
            ('¿Qué es la diversidad cultural?', 'Variedad de culturas'),
            ('¿Qué es la antropología cultural?', 'Estudio de las culturas'),
            ('¿Qué es la antropología física?', 'Estudio de la evolución humana'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    a = AntSQL()
    username = input("Usuario: ").strip()
    a.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': a.practicar()
        else: break
if __name__ == '__main__': main()
