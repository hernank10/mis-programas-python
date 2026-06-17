#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tablas de multiplicar - Versión SQL"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class TablasMultiplicarSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS practica_tablas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            numero INTEGER,
            aciertos INTEGER DEFAULT 0,
            intentos INTEGER DEFAULT 0
        )
        ''')
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self, numero):
        aciertos = 0
        print(f"\n🔢 TABLA DEL {numero}")
        print("=" * 40)
        
        for i in range(1, 11):
            respuesta = input(f"{numero} x {i} = ").strip()
            try:
                if int(respuesta) == numero * i:
                    print("✅ ¡Correcto!")
                    aciertos += 1
                else:
                    print(f"❌ Incorrecto. La respuesta es {numero * i}")
            except:
                print("❌ Entrada no válida")
        
        print(f"\n📊 Aciertos: {aciertos}/10")
        db.ejecutar('INSERT INTO practica_tablas (usuario_id, numero, aciertos, intentos) VALUES (?, ?, ?, ?)',
                    [self.usuario_id, numero, aciertos, 10])

def main():
    t = TablasMultiplicarSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    t.set_usuario(username)
    
    while True:
        print("\n1. Practicar tabla")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            try:
                num = int(input("Número (1-10): "))
                if 1 <= num <= 10:
                    t.practicar(num)
                else:
                    print("❌ Número entre 1 y 10")
            except:
                print("❌ Entrada no válida")
        else:
            break

if __name__ == '__main__':
    main()
