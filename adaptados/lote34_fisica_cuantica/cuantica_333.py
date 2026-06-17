#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class CuantSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un cuanto?', 'Cantidad mínima de energía'),
            ('¿Qué es la superposición cuántica?', 'Múltiples estados a la vez'),
            ('¿Qué es el entrelazamiento cuántico?', 'Conexión entre partículas'),
            ('¿Qué es el principio de incertidumbre?', 'Limitación en la medición'),
            ('¿Qué es un fotón?', 'Partícula de luz'),
            ('¿Qué es el efecto túnel?', 'Atravesar barreras cuánticas'),
            ('¿Qué es la física cuántica?', 'Estudio del mundo subatómico'),
            ('¿Qué es un qubit?', 'Bit cuántico'),
            ('¿Qué es la dualidad onda-partícula?', 'Ser partícula y onda a la vez'),
            ('¿Qué es un campo cuántico?', 'Campo de partículas cuánticas'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    c = CuantSQL()
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': c.practicar()
        else: break
if __name__ == '__main__': main()
