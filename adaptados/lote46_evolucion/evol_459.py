#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class EvoSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la evolución?', 'Cambio en las especies a lo largo del tiempo'),
            ('¿Qué es la selección natural?', 'Supervivencia del más apto'),
            ('¿Qué es una mutación?', 'Cambio en el ADN'),
            ('¿Qué es la adaptación?', 'Característica que ayuda a sobrevivir'),
            ('¿Qué es la especiación?', 'Formación de nuevas especies'),
            ('¿Qué es la evolución humana?', 'Origen y desarrollo del ser humano'),
            ('¿Qué es la evolución cultural?', 'Cambios en la cultura'),
            ('¿Qué es la evolución tecnológica?', 'Avance de la tecnología'),
            ('¿Qué es la extinción?', 'Desaparición de una especie'),
            ('¿Qué es la biodiversidad?', 'Variedad de especies'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    e = EvoSQL()
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': e.practicar()
        else: break
if __name__ == '__main__': main()
