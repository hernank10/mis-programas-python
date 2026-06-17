#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Practicar tiempos verbales - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class TiemposVerbalesSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS tiempos_verbales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            verbo TEXT NOT NULL,
            tiempo TEXT NOT NULL,
            ejemplo TEXT NOT NULL
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM tiempos_verbales")[0] == 0:
            tiempos = [
                ('hablar', 'presente', 'hablo, hablas, habla, hablamos, habláis, hablan'),
                ('hablar', 'pretérito perfecto', 'he hablado, has hablado, ha hablado, hemos hablado...'),
                ('hablar', 'futuro', 'hablaré, hablarás, hablará, hablaremos, hablaréis, hablarán'),
                ('comer', 'presente', 'como, comes, come, comemos, coméis, comen'),
                ('comer', 'pretérito perfecto', 'he comido, has comido, ha comido, hemos comido...'),
            ]
            for t in tiempos:
                db.ejecutar('INSERT OR IGNORE INTO tiempos_verbales (verbo, tiempo, ejemplo) VALUES (?, ?, ?)', t)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def practicar(self):
        tiempo = db.consultar_uno('SELECT * FROM tiempos_verbales ORDER BY RANDOM() LIMIT 1')
        if not tiempo:
            print("❌ No hay tiempos verbales disponibles")
            return
        
        print(f"\n⏳ TIEMPOS VERBALES")
        print("=" * 40)
        print(f"📖 Verbo: {tiempo['verbo']}")
        print(f"⏳ Tiempo: {tiempo['tiempo']}")
        print(f"📝 Ejemplo: {tiempo['ejemplo']}")

def main():
    t = TiemposVerbalesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    t.set_usuario(username)
    
    while True:
        print("\n1. Practicar tiempo verbal")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            t.practicar()
        else:
            break

if __name__ == '__main__':
    main()
