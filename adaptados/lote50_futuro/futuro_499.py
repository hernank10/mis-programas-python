#!/usr/bin/env python3
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class FutSQL:
    def __init__(self): self.usuario_id = None
    def set_usuario(self, username):
        u = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if u: self.usuario_id = u[0]; return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es el futuro?', 'Tiempo por venir'),
            ('¿Qué son las tendencias?', 'Direcciones futuras'),
            ('¿Qué es la predicción?', 'Previsión de sucesos futuros'),
            ('¿Qué es la tecnología emergente?', 'Tecnología en desarrollo'),
            ('¿Qué es la sostenibilidad?', 'Uso responsable de recursos'),
            ('¿Qué es la inteligencia artificial futura?', 'IA más avanzada'),
            ('¿Qué es la exploración espacial?', 'Viajes al espacio'),
            ('¿Qué es la medicina del futuro?', 'Medicina avanzada'),
            ('¿Qué es la educación del futuro?', 'Educación innovadora'),
            ('¿Qué es el trabajo del futuro?', 'Trabajo con nuevas tecnologías'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        r = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    f = FutSQL()
    username = input("Usuario: ").strip()
    f.set_usuario(username)
    while True:
        print("\n1. Practicar\n0. Salir")
        if input("Elige: ").strip() == '1': f.practicar()
        else: break
if __name__ == '__main__': main()
