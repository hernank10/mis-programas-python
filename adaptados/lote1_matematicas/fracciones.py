#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Práctica de fracciones - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class FraccionesSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        print("\n🔢 PRÁCTICA DE FRACCIONES")
        print("=" * 40)
        print("1. Suma de fracciones")
        print("2. Resta de fracciones")
        print("3. Multiplicación")
        print("4. División")
        
        opcion = input("\nElige: ").strip()
        
        # Generar fracciones aleatorias
        n1 = random.randint(1, 10)
        d1 = random.randint(2, 10)
        n2 = random.randint(1, 10)
        d2 = random.randint(2, 10)
        
        print(f"\n📝 Fracción 1: {n1}/{d1}")
        print(f"📝 Fracción 2: {n2}/{d2}")
        
        if opcion == '1':
            resultado = f"({n1*d2 + n2*d1})/({d1*d2})"
        elif opcion == '2':
            resultado = f"({n1*d2 - n2*d1})/({d1*d2})"
        elif opcion == '3':
            resultado = f"{n1*n2}/{d1*d2}"
        elif opcion == '4':
            resultado = f"{n1*d2}/{d1*n2}"
        else:
            print("❌ Opción no válida")
            return
        
        print(f"📌 Resultado: {resultado}")

def main():
    f = FraccionesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    f.set_usuario(username)
    
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            f.practicar()
        else:
            break

if __name__ == '__main__':
    main()
