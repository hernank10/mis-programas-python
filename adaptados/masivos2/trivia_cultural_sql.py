#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trivia cultural - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class TriviaCulturalSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS trivia_preguntas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT NOT NULL,
            respuesta_correcta TEXT NOT NULL,
            opcion_a TEXT,
            opcion_b TEXT,
            opcion_c TEXT,
            categoria TEXT DEFAULT 'general'
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM trivia_preguntas")[0] == 0:
            preguntas = [
                ('¿Cuál es la capital de España?', 'Madrid', 'Barcelona', 'Madrid', 'Valencia', 'geografia'),
                ('¿Quién pintó la Mona Lisa?', 'Da Vinci', 'Da Vinci', 'Picasso', 'Dalí', 'arte'),
                ('¿En qué año llegó el hombre a la Luna?', '1969', '1965', '1969', '1972', 'historia'),
                ('¿Cuál es el río más largo del mundo?', 'Amazonas', 'Nilo', 'Amazonas', 'Misisipi', 'geografia'),
                ('¿Qué obra escribió Miguel de Cervantes?', 'Don Quijote', 'La Celestina', 'Don Quijote', 'El Lazarillo', 'literatura'),
                ('¿Cuántos planetas hay en el sistema solar?', '8', '8', '9', '7', 'ciencia'),
                ('¿Quién fue el primer presidente de EE.UU.?', 'Washington', 'Washington', 'Lincoln', 'Jefferson', 'historia'),
                ('¿Qué instrumento toca Mozart?', 'Piano', 'Violín', 'Piano', 'Flauta', 'musica'),
                ('¿Cuál es el océano más grande?', 'Pacífico', 'Atlántico', 'Pacífico', 'Índico', 'geografia'),
                ('¿Qué descubrió Fleming?', 'Penicilina', 'Penicilina', 'Vacuna', 'Radiactividad', 'ciencia'),
            ]
            for p in preguntas:
                db.ejecutar('''
                INSERT OR IGNORE INTO trivia_preguntas (pregunta, respuesta_correcta, opcion_a, opcion_b, opcion_c, categoria)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def jugar(self, num_preguntas=5):
        preguntas = db.consultar('SELECT * FROM trivia_preguntas ORDER BY RANDOM() LIMIT ?', [num_preguntas])
        if not preguntas:
            print("❌ No hay preguntas disponibles")
            return
        
        puntaje = 0
        
        print(f"\n🎯 TRIVIA CULTURAL")
        print("=" * 40)
        
        for i, p in enumerate(preguntas, 1):
            print(f"\n{i}. {p['pregunta']}")
            print(f"   A) {p['opcion_a']}")
            print(f"   B) {p['opcion_b']}")
            print(f"   C) {p['opcion_c']}")
            
            respuesta = input("Tu respuesta (A/B/C): ").strip().upper()
            
            if respuesta == 'A':
                if p['opcion_a'] == p['respuesta_correcta']:
                    print("✅ ¡Correcto!")
                    puntaje += 1
                else:
                    print(f"❌ Incorrecto. La respuesta era: {p['respuesta_correcta']}")
            elif respuesta == 'B':
                if p['opcion_b'] == p['respuesta_correcta']:
                    print("✅ ¡Correcto!")
                    puntaje += 1
                else:
                    print(f"❌ Incorrecto. La respuesta era: {p['respuesta_correcta']}")
            elif respuesta == 'C':
                if p['opcion_c'] == p['respuesta_correcta']:
                    print("✅ ¡Correcto!")
                    puntaje += 1
                else:
                    print(f"❌ Incorrecto. La respuesta era: {p['respuesta_correcta']}")
            else:
                print("❌ Opción no válida")
        
        print(f"\n🏆 Puntaje final: {puntaje}/{num_preguntas}")

def main():
    t = TriviaCulturalSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    t.set_usuario(username)
    
    while True:
        print("\n1. Jugar trivia")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            t.jugar()
        else:
            break

if __name__ == '__main__':
    main()
