#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class CiberSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es una contraseña segura?', 'Combinación de letras, números y símbolos'),
            ('¿Qué es un virus informático?', 'Programa malicioso que se reproduce'),
            ('¿Qué es la ciberseguridad?', 'Protección de sistemas digitales'),
            ('¿Qué es el phishing?', 'Suplantación de identidad digital'),
            ('¿Qué es un firewall?', 'Barrera de seguridad de red'),
            ('¿Qué es el cifrado?', 'Protección de información con código'),
            ('¿Qué es la autenticación?', 'Verificar identidad de usuarios'),
            ('¿Qué es un hacker?', 'Experto en seguridad informática'),
            ('¿Qué es el malware?', 'Software malicioso en general'),
            ('¿Qué es una VPN?', 'Red privada virtual'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    c = CiberSQL()
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': c.practicar()
        else: break
if __name__ == '__main__': main()
