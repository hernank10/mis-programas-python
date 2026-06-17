#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Economía y finanzas - Programa $i"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class EconomiaSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        temas = [
            ('¿Qué es la inflación?', 'Aumento general de precios'),
            ('¿Qué es el PIB?', 'Producto Interior Bruto'),
            ('¿Qué es el ahorro?', 'Guardar dinero para el futuro'),
            ('¿Qué es la inversión?', 'Usar dinero para generar más dinero'),
            ('¿Qué es un presupuesto?', 'Plan de ingresos y gastos'),
            ('¿Qué es la deuda?', 'Dinero que se debe'),
            ('¿Qué es el interés compuesto?', 'Interés sobre interés'),
        ]
        p = random.choice(temas)
        print(f"\n❓ {p[0]}")
        resp = input("Tu respuesta: ").strip()
        print(f"💡 {p[1]}")
def main():
    e = EconomiaSQL()
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            e.practicar()
        else:
            break
if __name__ == '__main__':
    main()
