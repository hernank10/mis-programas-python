#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ecuaciones simples - Versión SQL"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db
class EcuacionesSQL:
    def __init__(self):
        self.usuario_id = None
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    def practicar(self):
        print("\n📐 ECUACIONES SIMPLES")
        print("=" * 40)
        print("Resuelve: 2x + 3 = 7")
        respuesta = input("x = ").strip()
        try:
            if float(respuesta) == 2:
                print("✅ ¡Correcto! x = 2")
            else:
                print("❌ Incorrecto. x = 2")
        except:
            print("❌ Entrada no válida")
def main():
    e = EcuacionesSQL()
    print("\n🔑 Iniciar sesión")
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
