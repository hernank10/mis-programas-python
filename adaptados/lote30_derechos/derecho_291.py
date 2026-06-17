#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class DerSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué son los derechos humanos?', 'Derechos inherentes a toda persona'),
            ('¿Qué es la igualdad?', 'Mismo trato para todos'),
            ('¿Qué es la libertad de expresión?', 'Derecho a opinar'),
            ('¿Qué es la justicia?', 'Equidad y cumplimiento de la ley'),
            ('¿Qué es la discriminación?', 'Trato desigual injusto'),
            ('¿Qué es la paz?', 'Estado de armonía'),
            ('¿Qué es la educación como derecho?', 'Acceso a la educación para todos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    d = DerSQL()
    username = input("Usuario: ").strip()
    d.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': d.practicar()
        else: break
if __name__ == '__main__': main()
