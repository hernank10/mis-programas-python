#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dictado interactivo - Versión SQL"""

import random, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class DictadoSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS dictados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            frase TEXT NOT NULL,
            dificultad INTEGER DEFAULT 1,
            pista TEXT
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM dictados")[0] == 0:
            frases = [
                ('El perro corre por el parque', 1, 'Animal y lugar'),
                ('La casa tiene una ventana grande', 1, 'Partes de una casa'),
                ('El árbol frondoso da sombra en verano', 2, 'Naturaleza'),
                ('La inteligencia emocional es clave para el éxito', 3, 'Habilidad personal'),
                ('Los dinosaurios dominaron la Tierra durante millones de años', 3, 'Prehistoria'),
                ('El chocolate caliente es mi bebida favorita', 2, 'Comida y bebida'),
                ('El sistema solar tiene ocho planetas principales', 2, 'Astronomía'),
                ('La universidad ofrece cursos en línea', 1, 'Educación'),
                ('El ajedrez desarrolla la capacidad estratégica', 3, 'Juego de mesa'),
                ('La buena alimentación mejora la calidad de vida', 2, 'Salud'),
            ]
            for f in frases:
                db.ejecutar('INSERT OR IGNORE INTO dictados (frase, dificultad, pista) VALUES (?, ?, ?)', f)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def dictar(self):
        dictado = db.consultar_uno('SELECT * FROM dictados ORDER BY RANDOM() LIMIT 1')
        if not dictado:
            print("❌ No hay dictados disponibles")
            return
        
        print(f"\n🎯 DICTADO")
        print("=" * 50)
        print(f"📊 Dificultad: {'⭐' * dictado['dificultad']}")
        print(f"💡 Pista: {dictado['pista']}")
        print("\n📢 Escucha atentamente y escribe lo que oyes...")
        print("\n📝 Frase (presiona Enter para continuar):")
        input()
        
        print(f"\n✍️ Escribe la frase:")
        respuesta = input().strip()
        
        # Mostrar frase correcta
        print(f"\n📖 Frase correcta: {dictado['frase']}")
        
        if respuesta.lower() == dictado['frase'].lower():
            print("✅ ¡Excelente! 🎉")
        else:
            print("❌ No es exactamente igual, pero sigue practicando.")
            print(f"📝 Errores: {len(set(respuesta.split()) & set(dictado['frase'].split()))} palabras correctas")

def main():
    d = DictadoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    d.set_usuario(username)
    
    while True:
        print("\n1. Dictado")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            d.dictar()
        else:
            break

if __name__ == '__main__':
    main()
