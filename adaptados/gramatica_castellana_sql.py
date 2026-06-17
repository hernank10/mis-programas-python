#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Gramática Castellana - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class GramaticaCastellanaSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📖 GRAMÁTICA CASTELLANA")
        print("=" * 40)
        print("1. Ver reglas gramaticales")
        print("2. Ver ejercicios de ortografía")
        print("3. Ver lecciones")
        print("4. Practicar con un ejercicio aleatorio")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_reglas()
        elif opcion == '2':
            self.ver_ejercicios()
        elif opcion == '3':
            self.ver_lecciones()
        elif opcion == '4':
            self.practicar_aleatorio()
        elif opcion == '0':
            return False
        return True
    
    def ver_reglas(self):
        reglas = db.consultar('SELECT * FROM reglas_gramaticales')
        print("\n📚 REGLAS GRAMATICALES")
        print("=" * 40)
        for r in reglas:
            print(f"\n📌 {r['categoria']}: {r['regla']}")
            print(f"   💡 {r['ejemplo']}")
            print(f"   📊 Nivel: {'⭐' * r['nivel']}")
    
    def ver_ejercicios(self):
        ejercicios = db.consultar('SELECT id, titulo, categoria FROM ejercicios_gramatica_castellana LIMIT 20')
        print("\n✏️ EJERCICIOS DE ORTOGRAFÍA")
        print("=" * 40)
        for e in ejercicios:
            print(f"  {e['id']}. {e['titulo'][:50]} ({e['categoria']})")
    
    def ver_lecciones(self):
        lecciones = db.consultar('SELECT id, titulo FROM lecciones_castellano')
        print("\n📖 LECCIONES")
        print("=" * 40)
        for l in lecciones:
            print(f"  {l['id']}. {l['titulo'][:60]}...")
    
    def practicar_aleatorio(self):
        ejercicio = db.consultar_uno('SELECT * FROM ejercicios_gramatica_castellana ORDER BY RANDOM() LIMIT 1')
        if ejercicio:
            print(f"\n✏️ EJERCICIO: {ejercicio['titulo']}")
            print("=" * 40)
            contenido = ejercicio['contenido'][:500] if ejercicio['contenido'] else "Contenido no disponible"
            print(contenido)

def main():
    g = GramaticaCastellanaSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    g.set_usuario(username)
    
    while True:
        if not g.ver_menu():
            break

if __name__ == '__main__':
    main()
