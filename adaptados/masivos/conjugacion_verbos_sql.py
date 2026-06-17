#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Practicar conjugación de verbos - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ConjugacionVerbosSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS verbos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            infinitivo TEXT NOT NULL,
            conjugacion TEXT NOT NULL,
            tiempo TEXT DEFAULT 'presente'
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM verbos")[0] == 0:
            verbos = [
                ('hablar', 'hablo, hablas, habla, hablamos, habláis, hablan', 'presente'),
                ('comer', 'como, comes, come, comemos, coméis, comen', 'presente'),
                ('vivir', 'vivo, vives, vive, vivimos, vivís, viven', 'presente'),
                ('ser', 'soy, eres, es, somos, sois, son', 'presente'),
                ('estar', 'estoy, estás, está, estamos, estáis, están', 'presente'),
            ]
            for v in verbos:
                db.ejecutar('INSERT OR IGNORE INTO verbos (infinitivo, conjugacion, tiempo) VALUES (?, ?, ?)', v)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        verbo = db.consultar_uno('SELECT * FROM verbos ORDER BY RANDOM() LIMIT 1')
        if not verbo:
            print("❌ No hay verbos disponibles")
            return
        
        print(f"\n🔤 CONJUGACIÓN DE VERBOS")
        print("=" * 40)
        print(f"📖 Infinitivo: {verbo['infinitivo']}")
        print(f"⏳ Tiempo: {verbo['tiempo']}")
        print(f"\n📝 Conjugación correcta:\n{verbo['conjugacion']}")
        print("\n💡 Escríbela para practicar (presiona Enter para continuar)")
        input()

def main():
    c = ConjugacionVerbosSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    
    while True:
        print("\n1. Practicar verbo")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            c.practicar()
        else:
            break

if __name__ == '__main__':
    main()
