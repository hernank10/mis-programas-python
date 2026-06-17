#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sistema de cuestionarios - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class CuestionariosSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS cuestionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT,
            nivel INTEGER DEFAULT 1,
            preguntas TEXT
        )
        ''')
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS respuestas_cuestionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            cuestionario_id INTEGER,
            puntaje INTEGER DEFAULT 0,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (cuestionario_id) REFERENCES cuestionarios(id)
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM cuestionarios")[0] == 0:
            self._cargar_cuestionarios()
    
    def _cargar_cuestionarios(self):
        cuestionarios = [
            ('Gramática Básica', 'gramatica', 1, '¿Qué es un sustantivo?|¿Qué es un verbo?|¿Qué es un adjetivo?'),
            ('Ortografía', 'ortografia', 1, '¿Cómo se escribe "haber"?|¿Lleva tilde "casa"?|¿Qué es un diptongo?'),
            ('Vocabulario', 'vocabulario', 2, 'Sinónimo de "rápido"|Antónimo de "alegre"|Significado de "efímero"'),
        ]
        for c in cuestionarios:
            db.ejecutar('INSERT OR IGNORE INTO cuestionarios (titulo, categoria, nivel, preguntas) VALUES (?, ?, ?, ?)', c)
        print(f"✅ Cargados {len(cuestionarios)} cuestionarios")
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def listar(self):
        cuestionarios = db.consultar('SELECT id, titulo, categoria, nivel FROM cuestionarios')
        print("\n📋 CUESTIONARIOS DISPONIBLES:")
        for c in cuestionarios:
            print(f"  {c['id']}. {c['titulo']} ({c['categoria']}) - Nivel {c['nivel']}")
    
    def realizar(self, cuestionario_id):
        if not self.usuario_id:
            print("❌ Inicia sesión primero")
            return
        
        cuestionario = db.consultar_uno('SELECT * FROM cuestionarios WHERE id = ?', [cuestionario_id])
        if not cuestionario:
            print("❌ Cuestionario no encontrado")
            return
        
        preguntas = cuestionario['preguntas'].split('|')
        puntaje = 0
        
        print(f"\n📝 {cuestionario['titulo']}")
        print("=" * 40)
        
        for i, p in enumerate(preguntas, 1):
            print(f"\n{i}. {p}")
            respuesta = input("Tu respuesta: ").strip()
            if respuesta.lower() in ['si', 'sí', 'verdadero', 'v']:
                print("✅ ¡Correcto!")
                puntaje += 10
            elif respuesta.lower() in ['no', 'falso', 'n']:
                print("❌ Incorrecto")
            else:
                print("💡 Respuesta registrada")
        
        db.ejecutar('INSERT INTO respuestas_cuestionario (usuario_id, cuestionario_id, puntaje) VALUES (?, ?, ?)',
                    [self.usuario_id, cuestionario_id, puntaje])
        print(f"\n🏆 Puntaje: {puntaje}/{len(preguntas)*10}")

def main():
    c = CuestionariosSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    if not c.set_usuario(username):
        print("❌ Usuario no encontrado")
        return
    
    while True:
        print("\n" + "=" * 40)
        print("  📋 CUESTIONARIOS")
        print("=" * 40)
        print("1. Ver cuestionarios")
        print("2. Realizar cuestionario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            c.listar()
        elif opcion == '2':
            c.listar()
            try:
                qid = int(input("ID del cuestionario: "))
                c.realizar(qid)
            except:
                print("❌ ID inválido")
        elif opcion == '0':
            break

if __name__ == '__main__':
    main()
