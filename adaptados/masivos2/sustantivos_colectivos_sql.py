#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sustantivos colectivos - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class SustantivosColectivosSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS sustantivos_colectivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concepto TEXT NOT NULL,
            colectivo TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM sustantivos_colectivos")[0] == 0:
            colectivos = [
                ('abejas', 'enjambre'),
                ('peces', 'cardumen'),
                ('pájaros', 'bandada'),
                ('ganado', 'rebaño'),
                ('ovejas', 'rebaño'),
                ('caballos', 'manada'),
                ('lobos', 'manada'),
                ('árboles', 'bosque'),
                ('flores', 'ramo'),
                ('estrellas', 'constelación'),
                ('islas', 'archipiélago'),
                ('personas', 'muchedumbre'),
                ('alumnos', 'alumnado'),
                ('profesores', 'claustro'),
                ('músicos', 'orquesta'),
            ]
            for c in colectivos:
                db.ejecutar('INSERT OR IGNORE INTO sustantivos_colectivos (concepto, colectivo) VALUES (?, ?)', c)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        colectivo = db.consultar_uno('SELECT * FROM sustantivos_colectivos ORDER BY RANDOM() LIMIT 1')
        if not colectivo:
            print("❌ No hay sustantivos colectivos disponibles")
            return
        
        print(f"\n📚 SUSTANTIVOS COLECTIVOS")
        print("=" * 40)
        print(f"📖 Concepto: {colectivo['concepto']}")
        
        respuesta = input("\n✍️ ¿Cuál es el colectivo? ").strip()
        
        if respuesta.lower() == colectivo['colectivo'].lower():
            print("✅ ¡Correcto! 🎉")
        else:
            print(f"❌ El colectivo es: {colectivo['colectivo']}")

def main():
    s = SustantivosColectivosSQL()
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
