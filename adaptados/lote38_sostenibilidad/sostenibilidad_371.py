#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class SosSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la sostenibilidad?', 'Uso responsable de recursos'),
            ('¿Qué son las energías renovables?', 'Energías de fuentes naturales'),
            ('¿Qué es el reciclaje?', 'Reutilizar materiales'),
            ('¿Qué es la huella de carbono?', 'Impacto ambiental'),
            ('¿Qué es el desarrollo sostenible?', 'Progreso sin dañar el planeta'),
            ('¿Qué es la energía solar?', 'Energía del sol'),
            ('¿Qué es la energía eólica?', 'Energía del viento'),
            ('¿Qué es el ahorro energético?', 'Reducir el consumo de energía'),
            ('¿Qué es el compostaje?', 'Transformar orgánicos en abono'),
            ('¿Qué es la economía circular?', 'Cerrar el ciclo de materiales'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    s = SosSQL()
    username = input("Usuario: ").strip()
    s.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': s.practicar()
        else: break
if __name__ == '__main__': main()
