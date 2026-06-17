#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class RobSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un robot?', 'Máquina programable'),
            ('¿Qué es la robótica?', 'Ciencia de los robots'),
            ('¿Qué es un actuador?', 'Componente que produce movimiento'),
            ('¿Qué es un sensor?', 'Componente que detecta entorno'),
            ('¿Qué es un microcontrolador?', 'Cerebro del robot'),
            ('¿Qué es un robot educativo?', 'Robot para aprendizaje'),
            ('¿Qué es la programación de robots?', 'Instrucciones para robots'),
            ('¿Qué es un brazo robótico?', 'Brazo mecánico programable'),
            ('¿Qué es un robot móvil?', 'Robot con capacidad de movimiento'),
            ('¿Qué es la automatización?', 'Procesos automáticos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    r = RobSQL()
    username = input("Usuario: ").strip()
    r.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': r.practicar()
        else: break
if __name__ == '__main__': main()
