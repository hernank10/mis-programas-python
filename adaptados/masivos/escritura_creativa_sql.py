#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de prompts de escritura creativa - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class EscrituraCreativaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS prompts_escritura (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tema TEXT NOT NULL,
            tipo TEXT DEFAULT 'narrativo',
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM prompts_escritura")[0] == 0:
            prompts = [
                ('Escribe una historia sobre un viaje en el tiempo', 'narrativo', 1),
                ('Describe tu lugar favorito', 'descriptivo', 1),
                ('Escribe una carta a tu yo del futuro', 'epistolar', 2),
                ('Crea un diálogo entre dos personajes', 'dialogo', 2),
            ]
            for p in prompts:
                db.ejecutar('INSERT OR IGNORE INTO prompts_escritura (tema, tipo, nivel) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def generar_prompt(self):
        prompt = db.consultar_uno('SELECT * FROM prompts_escritura ORDER BY RANDOM() LIMIT 1')
        if prompt:
            print(f"\n✍️ PROMPT DE ESCRITURA")
            print("=" * 40)
            print(f"📝 {prompt['tema']}")
            print(f"📌 Tipo: {prompt['tipo']}")
            print(f"📊 Nivel: {prompt['nivel']}")
            print("\n⏳ Escribe tu texto (escribe 'fin' para terminar):")
            
            lineas = []
            while True:
                linea = input()
                if linea.lower() == 'fin':
                    break
                lineas.append(linea)
            
            texto_completo = '\n'.join(lineas)
            print(f"\n📄 Tu texto:\n{texto_completo}")
            print(f"\n📊 Palabras: {len(texto_completo.split())}")

def main():
    e = EscrituraCreativaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    
    while True:
        print("\n1. Nuevo prompt")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            e.generar_prompt()
        else:
            break

if __name__ == '__main__':
    main()
