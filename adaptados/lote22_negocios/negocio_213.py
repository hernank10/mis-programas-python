#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class NegSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es una startup?', 'Empresa emergente innovadora'),
            ('¿Qué es el marketing?', 'Estrategias de promoción'),
            ('¿Qué es el liderazgo?', 'Guiar a un equipo'),
            ('¿Qué es la innovación?', 'Nuevas ideas y soluciones'),
            ('¿Qué es la estrategia empresarial?', 'Plan para alcanzar objetivos'),
            ('¿Qué es el emprendimiento?', 'Crear un negocio'),
            ('¿Qué es la rentabilidad?', 'Capacidad de generar ganancias'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    n = NegSQL()
    username = input("Usuario: ").strip()
    n.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': n.practicar()
        else: break
if __name__ == '__main__': main()
