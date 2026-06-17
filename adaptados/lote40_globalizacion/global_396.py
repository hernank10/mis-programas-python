#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class GlobalSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la globalización?', 'Interconexión mundial'),
            ('¿Qué es el comercio internacional?', 'Intercambio entre países'),
            ('¿Qué es la multiculturalidad?', 'Diversidad cultural'),
            ('¿Qué es la cooperación internacional?', 'Ayuda entre países'),
            ('¿Qué es la migración?', 'Movimiento de personas entre países'),
            ('¿Qué es la economía global?', 'Economía interconectada'),
            ('¿Qué es la cultura global?', 'Influencias culturales compartidas'),
            ('¿Qué es el turismo internacional?', 'Viajes entre países'),
            ('¿Qué es la diplomacia?', 'Relaciones entre países'),
            ('¿Qué es la paz mundial?', 'Ausencia de conflictos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    g = GlobalSQL()
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': g.practicar()
        else: break
if __name__ == '__main__': main()
