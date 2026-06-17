#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Potencias y raíces - Versión SQL"""

import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class PotenciasRaicesSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        print("\n🔢 POTENCIAS Y RAÍCES")
        print("=" * 40)
        print("1. Potencia (a^b)")
        print("2. Raíz cuadrada")
        print("3. Raíz cúbica")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            base = float(input("Base: "))
            exp = float(input("Exponente: "))
            print(f"📝 {base}^{exp} = {base**exp}")
        elif opcion == '2':
            num = float(input("Número: "))
            print(f"📝 √{num} = {math.sqrt(num):.4f}")
        elif opcion == '3':
            num = float(input("Número: "))
            print(f"📝 ³√{num} = {num**(1/3):.4f}")

def main():
    p = PotenciasRaicesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    p.set_usuario(username)
    
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            p.practicar()
        else:
            break

if __name__ == '__main__':
    main()
