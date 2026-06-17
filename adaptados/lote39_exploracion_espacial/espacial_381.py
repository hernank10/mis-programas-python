#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class EspSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un cohete?', 'Vehículo para viajes espaciales'),
            ('¿Qué es un satélite?', 'Objeto en órbita terrestre'),
            ('¿Qué es la Estación Espacial Internacional?', 'Laboratorio en el espacio'),
            ('¿Qué es un rover?', 'Vehículo explorador en otros planetas'),
            ('¿Qué es la misión Artemis?', 'Programa para volver a la Luna'),
            ('¿Qué es un agujero negro?', 'Región con gravedad extrema'),
            ('¿Qué es un exoplaneta?', 'Planeta fuera del sistema solar'),
            ('¿Qué es el telescopio James Webb?', 'Telescopio espacial avanzado'),
            ('¿Qué es la gravedad cero?', 'Estado sin peso aparente'),
            ('¿Qué es el espacio profundo?', 'Más allá del sistema solar'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    e = EspSQL()
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': e.practicar()
        else: break
if __name__ == '__main__': main()
