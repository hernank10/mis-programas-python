#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculadora básica - Versión SQL"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CalculadoraSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS operaciones_calculadora (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            operacion TEXT,
            resultado TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def calcular(self):
        print("\n🧮 CALCULADORA BÁSICA")
        print("=" * 40)
        print("Operaciones: +, -, *, /, ** (potencia), % (módulo)")
        
        try:
            num1 = float(input("Número 1: "))
            op = input("Operación: ").strip()
            num2 = float(input("Número 2: "))
            
            if op == '+':
                resultado = num1 + num2
            elif op == '-':
                resultado = num1 - num2
            elif op == '*':
                resultado = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("❌ No se puede dividir por cero")
                    return
                resultado = num1 / num2
            elif op == '**':
                resultado = num1 ** num2
            elif op == '%':
                resultado = num1 % num2
            else:
                print("❌ Operación no válida")
                return
            
            print(f"📝 Resultado: {num1} {op} {num2} = {resultado}")
            db.ejecutar('INSERT INTO operaciones_calculadora (usuario_id, operacion, resultado) VALUES (?, ?, ?)',
                        [self.usuario_id, f"{num1} {op} {num2}", str(resultado)])
        except ValueError:
            print("❌ Entrada no válida")

def main():
    c = CalculadoraSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    
    while True:
        print("\n1. Calcular")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            c.calcular()
        else:
            break

if __name__ == '__main__':
    main()
