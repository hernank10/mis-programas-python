#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Geometría básica - Versión SQL"""

import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class GeometriaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS calculos_geometria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            figura TEXT,
            calculo TEXT,
            resultado REAL
        )
        ''')
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def calcular(self):
        print("\n📐 GEOMETRÍA BÁSICA")
        print("=" * 40)
        print("1. Área del círculo")
        print("2. Área del rectángulo")
        print("3. Área del triángulo")
        print("4. Teorema de Pitágoras")
        print("5. Volumen del cubo")
        
        opcion = input("\nElige una opción: ").strip()
        
        if opcion == '1':
            r = float(input("Radio: "))
            area = math.pi * r ** 2
            print(f"📝 Área del círculo: {area:.2f}")
            db.ejecutar('INSERT INTO calculos_geometria (usuario_id, figura, calculo, resultado) VALUES (?, ?, ?, ?)',
                        [self.usuario_id, "círculo", f"π * {r}²", area])
        elif opcion == '2':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            area = base * altura
            print(f"📝 Área del rectángulo: {area}")
        elif opcion == '3':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            area = (base * altura) / 2
            print(f"📝 Área del triángulo: {area}")
        elif opcion == '4':
            a = float(input("Cateto a: "))
            b = float(input("Cateto b: "))
            c = math.sqrt(a**2 + b**2)
            print(f"📝 Hipotenusa: {c:.2f}")
        elif opcion == '5':
            lado = float(input("Lado: "))
            volumen = lado ** 3
            print(f"📝 Volumen del cubo: {volumen}")
        else:
            print("❌ Opción no válida")

def main():
    g = GeometriaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    
    while True:
        print("\n1. Calcular")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            g.calcular()
        else:
            break

if __name__ == '__main__':
    main()
