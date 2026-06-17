#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class PsiSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la psicología?', 'Estudio de la mente y el comportamiento'),
            ('¿Qué es la ansiedad?', 'Respuesta al miedo o preocupación'),
            ('¿Qué es la autoestima?', 'Valoración de uno mismo'),
            ('¿Qué es la resiliencia?', 'Capacidad de superar adversidades'),
            ('¿Qué es la empatía?', 'Ponerse en el lugar del otro'),
            ('¿Qué es la inteligencia emocional?', 'Gestionar emociones'),
            ('¿Qué es la motivación?', 'Impulso para actuar'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    p = PsiSQL()
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': p.practicar()
        else: break
if __name__ == '__main__': main()
