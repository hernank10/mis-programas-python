#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regla de tres - Versión SQL"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class ReglaTresSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print("\n📐 REGLA DE TRES")
        print("=" * 40)
        print("Si 5 manzanas cuestan $10, ¿cuánto cuestan 8 manzanas?")
        respuesta = input("Respuesta: $").strip()
        try:
            if float(respuesta) == 16:
                print("✅ ¡Correcto! $16")
            else:
                print("❌ Incorrecto. $16")
        except:
            print("❌ Entrada no válida")
def main():
    r = ReglaTresSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    r.set_usuario(username)
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            r.practicar()
        else:
            break
if __name__ == '__main__':
    main()
