#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Palabras con prefijos - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class PrefijosSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS prefijos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prefijo TEXT NOT NULL,
            significado TEXT NOT NULL,
            ejemplo TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM prefijos")[0] == 0:
            prefijos = [
                ('anti', 'contra', 'antidoto, antídoto'),
                ('auto', 'propio', 'automóvil, autónomo'),
                ('bi', 'dos', 'bicicleta, bilingüe'),
                ('contra', 'opuesto', 'contradecir'),
                ('des', 'negación', 'deshacer, desarmar'),
                ('ex', 'fuera', 'exterior, exportar'),
                ('extra', 'más allá', 'extraordinario'),
                ('inter', 'entre', 'internacional'),
                ('mal', 'malo', 'maltratar'),
                ('micro', 'pequeño', 'microondas'),
                ('multi', 'muchos', 'multicolor'),
                ('pre', 'antes', 'prehistoria, predecir'),
                ('pro', 'a favor', 'progreso, promover'),
                ('re', 'repetir', 'rehacer, renovar'),
                ('sub', 'debajo', 'submarino, subterráneo'),
                ('super', 'más', 'superhéroe'),
                ('trans', 'a través', 'transparente'),
                ('uni', 'uno', 'uniforme'),
            ]
            for p in prefijos:
                db.ejecutar('INSERT OR IGNORE INTO prefijos (prefijo, significado, ejemplo) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        prefijo = db.consultar_uno('SELECT * FROM prefijos ORDER BY RANDOM() LIMIT 1')
        if not prefijo:
            print("❌ No hay prefijos disponibles")
            return
        
        print(f"\n🔤 PREFIJOS")
        print("=" * 40)
        print(f"📖 Prefijo: {prefijo['prefijo']}")
        print(f"📝 Significado: {prefijo['significado']}")
        print(f"💡 Ejemplo: {prefijo['ejemplo']}")

def main():
    p = PrefijosSQL()
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
