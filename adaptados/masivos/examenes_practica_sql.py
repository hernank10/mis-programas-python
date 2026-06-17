#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de exámenes de práctica - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class ExamenesPracticaSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS examenes_practica (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            preguntas TEXT NOT NULL,
            respuestas TEXT NOT NULL,
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM examenes_practica")[0] == 0:
            examenes = [
                ('Examen de Gramática', '¿Qué es un sustantivo?|¿Qué es un verbo?|¿Qué es un adjetivo?', 
                 'Persona, lugar o cosa|Acción o estado|Calidad o característica', 1),
                ('Examen de Ortografía', '¿Cómo se escribe "haber"?|¿Lleva tilde "casa"?', 
                 'haber|no', 1),
            ]
            for e in examenes:
                db.ejecutar('INSERT OR IGNORE INTO examenes_practica (titulo, preguntas, respuestas, nivel) VALUES (?, ?, ?, ?)', e)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def generar_examen(self):
        examen = db.consultar_uno('SELECT * FROM examenes_practica ORDER BY RANDOM() LIMIT 1')
        if not examen:
            print("❌ No hay exámenes disponibles")
            return
        
        preguntas = examen['preguntas'].split('|')
        respuestas = examen['respuestas'].split('|')
        puntaje = 0
        
        print(f"\n📝 EXAMEN: {examen['titulo']}")
        print("=" * 40)
        print(f"📊 Nivel: {examen['nivel']}")
        print(f"📌 Total preguntas: {len(preguntas)}\n")
        
        for i, (p, r) in enumerate(zip(preguntas, respuestas), 1):
            print(f"{i}. {p}")
            respuesta = input("Tu respuesta: ").strip()
            if respuesta.lower() == r.lower():
                print("✅ ¡Correcto!")
                puntaje += 1
            else:
                print(f"❌ Incorrecto. Respuesta: {r}")
            print()
        
        print("=" * 40)
        print(f"🏆 Puntaje final: {puntaje}/{len(preguntas)}")
        porcentaje = puntaje * 100 // len(preguntas)
        if porcentaje >= 80:
            print("🌟 ¡Excelente! Eres un experto.")
        elif porcentaje >= 60:
            print("👍 Bien, pero puedes mejorar.")
        else:
            print("📚 Estudia más y vuelve a intentarlo.")

def main():
    e = ExamenesPracticaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    e.set_usuario(username)
    
    while True:
        print("\n1. Generar examen")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            e.generar_examen()
        else:
            break

if __name__ == '__main__':
    main()
