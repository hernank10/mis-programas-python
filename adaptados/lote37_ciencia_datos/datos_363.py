#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class DatosSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la ciencia de datos?', 'Extraer conocimiento de datos'),
            ('¿Qué es el análisis de datos?', 'Interpretar datos'),
            ('¿Qué es una visualización?', 'Representación gráfica de datos'),
            ('¿Qué es la estadística?', 'Ciencia de los datos'),
            ('¿Qué es una base de datos?', 'Organización de datos'),
            ('¿Qué es un modelo predictivo?', 'Predicción de futuros eventos'),
            ('¿Qué es el Big Data?', 'Grandes conjuntos de datos'),
            ('¿Qué es la limpieza de datos?', 'Preparar datos para análisis'),
            ('¿Qué es un dashboard?', 'Panel de visualización de datos'),
            ('¿Qué es un algoritmo?', 'Procedimiento para resolver problemas'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    d = DatosSQL()
    username = input("Usuario: ").strip()
    d.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': d.practicar()
        else: break
if __name__ == '__main__': main()
