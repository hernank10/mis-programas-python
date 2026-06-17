#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class IASQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la IA?', 'Sistemas que simulan inteligencia humana'),
            ('¿Qué es el aprendizaje automático?', 'Máquinas que aprenden de datos'),
            ('¿Qué es una red neuronal?', 'Sistema inspirado en el cerebro'),
            ('¿Qué es el deep learning?', 'Aprendizaje profundo con redes'),
            ('¿Qué es el procesamiento del lenguaje natural?', 'Entender lenguaje humano'),
            ('¿Qué es la visión por computadora?', 'Entender imágenes'),
            ('¿Qué es un agente inteligente?', 'Sistema que actúa autónomamente'),
            ('¿Qué es la ética en IA?', 'Principios para un uso responsable'),
            ('¿Qué es la robótica con IA?', 'Robots inteligentes'),
            ('¿Qué es la IA generativa?', 'Crear contenido nuevo'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    i = IASQL()
    username = input("Usuario: ").strip()
    i.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': i.practicar()
        else: break
if __name__ == '__main__': main()
