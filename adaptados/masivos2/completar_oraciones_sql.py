#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Completar oraciones - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CompletarOracionesSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS oraciones_incompletas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            oracion TEXT NOT NULL,
            respuesta TEXT NOT NULL,
            pista TEXT,
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM oraciones_incompletas")[0] == 0:
            oraciones = [
                ('El ____ es el mejor amigo del hombre', 'perro', 'Animal doméstico', 1),
                ('La ____ es la capital de España', 'Madrid', 'Ciudad europea', 1),
                ('El ____ es un planeta del sistema solar', 'sol', 'Estrella central', 2),
                ('La ____ es la ciencia que estudia la vida', 'biología', 'Ciencia natural', 2),
                ('El ____ es el metal más abundante en la Tierra', 'hierro', 'Metal', 2),
                ('La ____ es la obra más famosa de Cervantes', 'Don Quijote', 'Novela española', 2),
                ('El ____ es el océano más grande', 'Pacífico', 'Océano', 2),
                ('La ____ es la capital de Francia', 'París', 'Ciudad europea', 1),
                ('El ____ es el río más largo del mundo', 'Amazonas', 'Río', 2),
                ('La ____ es la montaña más alta del mundo', 'Everest', 'Montaña', 2),
            ]
            for o in oraciones:
                db.ejecutar('INSERT OR IGNORE INTO oraciones_incompletas (oracion, respuesta, pista, nivel) VALUES (?, ?, ?, ?)', o)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        oracion = db.consultar_uno('SELECT * FROM oraciones_incompletas ORDER BY RANDOM() LIMIT 1')
        if not oracion:
            print("❌ No hay oraciones disponibles")
            return
        
        print(f"\n📝 COMPLETAR ORACIÓN")
        print("=" * 40)
        print(f"📖 {oracion['oracion']}")
        print(f"💡 Pista: {oracion['pista']}")
        print(f"📊 Nivel: {'⭐' * oracion['nivel']}")
        
        respuesta = input("\n✍️ Tu respuesta: ").strip()
        
        if respuesta.lower() == oracion['respuesta'].lower():
            print("✅ ¡Correcto! 🎉")
        else:
            print(f"❌ La respuesta era: {oracion['respuesta']}")

def main():
    c = CompletarOracionesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    c.set_usuario(username)
    
    while True:
        print("\n1. Practicar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            c.practicar()
        else:
            break

if __name__ == '__main__':
    main()
