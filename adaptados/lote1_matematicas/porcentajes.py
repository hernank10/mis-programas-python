#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cálculo de porcentajes - Versión SQL"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class PorcentajesSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print("\n📊 PORCENTAJES")
        print("=" * 40)
        print("1. Calcular porcentaje")
        print("2. Aumento porcentual")
        print("3. Descuento porcentual")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            total = float(input("Total: "))
            parte = float(input("Parte: "))
            print(f"📝 {parte} es el {parte/total*100:.1f}% de {total}")
        elif opcion == '2':
            valor = float(input("Valor: "))
            pct = float(input("Porcentaje de aumento: "))
            print(f"📝 {valor} + {pct}% = {valor * (1 + pct/100):.2f}")
        elif opcion == '3':
            valor = float(input("Valor: "))
            pct = float(input("Porcentaje de descuento: "))
            print(f"📝 {valor} - {pct}% = {valor * (1 - pct/100):.2f}")
def main():
    p = PorcentajesSQL()
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
