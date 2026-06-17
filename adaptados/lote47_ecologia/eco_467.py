#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class EcoSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la ecología?', 'Estudio de las relaciones entre seres vivos'),
            ('¿Qué es un ecosistema?', 'Comunidad de seres vivos y su entorno'),
            ('¿Qué es la cadena alimenticia?', 'Flujo de energía entre seres vivos'),
            ('¿Qué es un bioma?', 'Gran ecosistema terrestre'),
            ('¿Qué es la biodiversidad?', 'Variedad de especies'),
            ('¿Qué es la conservación?', 'Protección de la naturaleza'),
            ('¿Qué es una especie en peligro?', 'Especie en riesgo de extinción'),
            ('¿Qué es un hábitat?', 'Lugar donde vive una especie'),
            ('¿Qué es la población?', 'Grupo de individuos de la misma especie'),
            ('¿Qué es la comunidad?', 'Conjunto de poblaciones en un lugar'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    e = EcoSQL()
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': e.practicar()
        else: break
if __name__ == '__main__': main()
