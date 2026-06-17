#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cálculo de perímetros - Versión SQL"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class PerimetrosSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print("\n📐 PERÍMETROS")
        print("=" * 40)
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Círculo")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            lado = float(input("Lado: "))
            print(f"📝 Perímetro: {lado * 4}")
        elif opcion == '2':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            print(f"📝 Perímetro: {2 * (base + altura)}")
        elif opcion == '3':
            radio = float(input("Radio: "))
            print(f"📝 Perímetro: {2 * 3.1416 * radio:.2f}")
def main():
    p = PerimetrosSQL()
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
