#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MCM y MCD - Versión SQL"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class MCMSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print("\n🔢 MCM Y MCD")
        print("=" * 40)
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))
        print(f"📝 MCD: {math.gcd(a, b)}")
        print(f"📝 MCM: {a * b // math.gcd(a, b)}")
def main():
    m = MCMSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    m.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            m.practicar()
        else:
            break
if __name__ == '__main__':
    main()
