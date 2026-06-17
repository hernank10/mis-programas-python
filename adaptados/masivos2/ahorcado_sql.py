#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Juego del ahorcado - Versión SQL"""

import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_manager import db

class AhorcadoSQL:
    def __init__(self):
        self.usuario_id = None
        self._inicializar()
        self.intentos = 6
        self.letras_usadas = []
    
    def _inicializar(self):
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS palabras_ahorcado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            categoria TEXT DEFAULT 'general',
            nivel INTEGER DEFAULT 1
        )
        ''')
        if db.consultar_uno("SELECT COUNT(*) FROM palabras_ahorcado")[0] == 0:
            palabras = [
                ('casa', 'general', 1), ('perro', 'general', 1), ('gato', 'general', 1),
                ('computadora', 'tecnologia', 2), ('internet', 'tecnologia', 2), ('programa', 'tecnologia', 2),
                ('escuela', 'general', 1), ('maestro', 'general', 1), ('ciudad', 'general', 1),
                ('inteligencia', 'adjetivos', 3), ('responsabilidad', 'adjetivos', 3),
                ('felicidad', 'emociones', 2), ('amistad', 'emociones', 2),
            ]
            for p in palabras:
                db.ejecutar('INSERT OR IGNORE INTO palabras_ahorcado (palabra, categoria, nivel) VALUES (?, ?, ?)', p)
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def jugar(self):
        palabra = db.consultar_uno('SELECT * FROM palabras_ahorcado ORDER BY RANDOM() LIMIT 1')
        if not palabra:
            print("❌ No hay palabras disponibles")
            return
        
        palabra_secreta = palabra['palabra']
        self.intentos = 6
        self.letras_usadas = []
        letras_adivinadas = ['_'] * len(palabra_secreta)
        
        print(f"\n🎯 AHORCADO")
        print("=" * 40)
        print(f"💡 Categoría: {palabra['categoria']}")
        print(f"📊 Nivel: {palabra['nivel']}")
        
        while self.intentos > 0 and '_' in letras_adivinadas:
            print(f"\n📝 Palabra: {' '.join(letras_adivinadas)}")
            print(f"❌ Intentos restantes: {self.intentos}")
            print(f"🔤 Letras usadas: {', '.join(sorted(self.letras_usadas)) if self.letras_usadas else 'Ninguna'}")
            
            letra = input("🔤 Adivina una letra: ").strip().lower()
            
            if len(letra) != 1 or not letra.isalpha():
                print("❌ Ingresa una sola letra")
                continue
            
            if letra in self.letras_usadas:
                print("⚠️ Ya usaste esa letra")
                continue
            
            self.letras_usadas.append(letra)
            
            if letra in palabra_secreta:
                print("✅ ¡Bien!")
                for i, c in enumerate(palabra_secreta):
                    if c == letra:
                        letras_adivinadas[i] = letra
            else:
                print("❌ Incorrecto")
                self.intentos -= 1
        
        if '_' not in letras_adivinadas:
            print(f"\n🎉 ¡Felicidades! La palabra era: {palabra_secreta}")
        else:
            print(f"\n💀 ¡Ah, no! La palabra era: {palabra_secreta}")

def main():
    a = AhorcadoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    a.set_usuario(username)
    
    while True:
        print("\n1. Jugar")
        print("0. Salir")
        opcion = input("\nElige: ").strip()
        if opcion == '1':
            a.jugar()
        else:
            break

if __name__ == '__main__':
    main()
