#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class FarSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un medicamento?', 'Sustancia para tratar enfermedades'),
            ('¿Qué es una vacuna?', 'Prevención de enfermedades'),
            ('¿Qué es un antibiótico?', 'Combate infecciones bacterianas'),
            ('¿Qué es un analgésico?', 'Alivia el dolor'),
            ('¿Qué es la dosificación?', 'Cantidad de medicamento a tomar'),
            ('¿Qué es una reacción adversa?', 'Efecto secundario no deseado'),
            ('¿Qué es un placebo?', 'Sustancia sin efecto terapéutico'),
            ('¿Qué es un fármaco?', 'Principio activo de un medicamento'),
            ('¿Qué es la farmacología?', 'Estudio de los medicamentos'),
            ('¿Qué es la farmacia?', 'Ciencia de la preparación de medicamentos'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    f = FarSQL()
    username = input("Usuario: ").strip()
    f.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': f.practicar()
        else: break
if __name__ == '__main__': main()
