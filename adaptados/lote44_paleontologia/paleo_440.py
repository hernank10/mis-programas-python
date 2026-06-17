#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class PaleSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es un fósil?', 'Resto de organismo antiguo'),
            ('¿Qué es un dinosaurio?', 'Reptil prehistórico extinto'),
            ('¿Qué es la evolución?', 'Cambio a lo largo del tiempo'),
            ('¿Qué es un trilobites?', 'Artropodo marino fósil'),
            ('¿Qué es un ammonite?', 'Molusco fósil en espiral'),
            ('¿Qué es el período Jurásico?', 'Época de los dinosaurios'),
            ('¿Qué es un hueso fósil?', 'Hueso conservado como fósil'),
            ('¿Qué es la paleontología?', 'Estudio de la vida antigua'),
            ('¿Qué es un mamut?', 'Elefante prehistórico'),
            ('¿Qué es el Tyrannosaurus Rex?', 'Dinosaurio carnívoro gigante'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    p = PaleSQL()
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': p.practicar()
        else: break
if __name__ == '__main__': main()
