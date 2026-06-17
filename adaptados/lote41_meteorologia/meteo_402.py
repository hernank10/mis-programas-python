#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class MeteoSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el clima?', 'Condiciones atmosféricas promedio'),
            ('¿Qué es un tornado?', 'Vórtice de aire violento'),
            ('¿Qué es un huracán?', 'Tormenta tropical intensa'),
            ('¿Qué es la lluvia?', 'Precipitación de agua'),
            ('¿Qué es la nieve?', 'Precipitación congelada'),
            ('¿Qué es el viento?', 'Movimiento del aire'),
            ('¿Qué es la presión atmosférica?', 'Peso del aire'),
            ('¿Qué es un frente meteorológico?', 'Límite entre masas de aire'),
            ('¿Qué es la humedad?', 'Cantidad de vapor de agua'),
            ('¿Qué es el cambio climático?', 'Alteración del clima global'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    m = MeteoSQL()
    username = input("Usuario: ").strip()
    m.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': m.practicar()
        else: break
if __name__ == '__main__': main()
