#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class BioHumSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Cuántos huesos tiene el cuerpo humano?', '206'),
            ('¿Qué es el ADN?', 'Material genético'),
            ('¿Qué es el cerebro?', 'Centro de control del cuerpo'),
            ('¿Qué es el corazón?', 'Bomba que impulsa la sangre'),
            ('¿Qué son los glóbulos rojos?', 'Células que transportan oxígeno'),
            ('¿Qué es el sistema inmunológico?', 'Defensa del cuerpo'),
            ('¿Qué es la homeostasis?', 'Equilibrio interno'),
            ('¿Qué es el metabolismo?', 'Procesos químicos en el cuerpo'),
            ('¿Qué es una enfermedad?', 'Alteración de la salud'),
            ('¿Qué es la vacuna?', 'Prevención de enfermedades'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    b = BioHumSQL()
    username = input("Usuario: ").strip()
    b.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': b.practicar()
        else: break
if __name__ == '__main__': main()
