#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicios de sinónimos y antónimos - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class SinonimosAntonimosSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS palabras_sinonimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            sinonimo TEXT NOT NULL,
            antonimo TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM palabras_sinonimos")[0] == 0:
            palabras = [
                ('rápido', 'veloz', 'lento'),
                ('alegre', 'feliz', 'triste'),
                ('grande', 'enorme', 'pequeño'),
                ('fuerte', 'robusto', 'débil'),
                ('inteligente', 'listo', 'tonto'),
            ]
            for p in palabras:
                db.ejecutar('INSERT OR IGNORE INTO palabras_sinonimos (palabra, sinonimo, antonimo) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        palabra = db.consultar_uno('SELECT * FROM palabras_sinonimos ORDER BY RANDOM() LIMIT 1')
        if not palabra:
            print("❌ No hay palabras disponibles")
            return
        
        print(f"\n📚 SINÓNIMOS Y ANTÓNIMOS")
        print("=" * 40)
        
        # Sinónimo
        print(f"📖 Palabra: {palabra['palabra']}")
        print(f"📝 Sinónimo: {palabra['sinonimo']}")
        print(f"📝 Antónimo: {palabra['antonimo']}")
        print("\n💡 Recuerda estos pares de palabras")

def main():
    s = SinonimosAntonimosSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    s.set_usuario(username)
    
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            s.practicar()
        else:
            break

if __name__ == '__main__':
    main()
