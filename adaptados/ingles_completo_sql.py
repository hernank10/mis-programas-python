#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador completo de Inglés - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class InglesCompletoSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n🇬🇧 INGLÉS COMPLETO")
        print("=" * 40)
        print("1. Ver todos los programas")
        print("2. Ver por categoría")
        print("3. Ver entrenadores")
        print("4. Ver juegos")
        print("5. Programa aleatorio")
        print("6. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_todos()
        elif opcion == '2':
            self.ver_por_categoria()
        elif opcion == '3':
            self.ver_entrenadores()
        elif opcion == '4':
            self.ver_juegos()
        elif opcion == '5':
            self.aleatorio()
        elif opcion == '6':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_todos(self):
        programas = db.consultar('SELECT id, nombre, categoria FROM programas_ingles')
        print("\n📋 PROGRAMAS DE INGLÉS")
        print("=" * 50)
        for p in programas:
            print(f"  {p['id']}. {p['nombre'][:50]} ({p['categoria']})")
    
    def ver_por_categoria(self):
        categorias = db.consultar('SELECT DISTINCT categoria FROM programas_ingles')
        print("\n📂 CATEGORÍAS:")
        for c in categorias:
            count = db.consultar_uno('SELECT COUNT(*) FROM programas_ingles WHERE categoria = ?', [c[0]])[0]
            print(f"  • {c[0]}: {count} programas")
        
        cat = input("\nElige una categoría: ").strip()
        programas = db.consultar('SELECT id, nombre FROM programas_ingles WHERE categoria = ?', [cat])
        if programas:
            print(f"\n📋 Programas de '{cat}':")
            for p in programas:
                print(f"  • {p['nombre']}")
    
    def ver_entrenadores(self):
        programas = db.consultar('SELECT id, nombre FROM programas_ingles WHERE categoria = "entrenador"')
        print("\n📖 ENTRENADORES DE INGLÉS:")
        for p in programas:
            print(f"  • {p['nombre']}")
    
    def ver_juegos(self):
        programas = db.consultar('SELECT id, nombre FROM programas_ingles WHERE categoria = "juego"')
        print("\n🎮 JUEGOS DE INGLÉS:")
        for p in programas:
            print(f"  • {p['nombre']}")
    
    def aleatorio(self):
        programa = db.consultar_uno('SELECT * FROM programas_ingles ORDER BY RANDOM() LIMIT 1')
        if programa:
            print(f"\n🎯 PROGRAMA ALEATORIO:")
            print(f"📌 Nombre: {programa['nombre']}")
            print(f"📂 Categoría: {programa['categoria']}")
            print(f"💻 Tipo: {programa['tipo']}")
    
    def estadisticas(self):
        total = db.consultar_uno('SELECT COUNT(*) FROM programas_ingles')[0]
        print(f"\n📊 ESTADÍSTICAS DE INGLÉS")
        print("=" * 40)
        print(f"📚 Total programas: {total}")
        
        categorias = db.consultar('SELECT categoria, COUNT(*) FROM programas_ingles GROUP BY categoria')
        print("\n📂 Por categoría:")
        for c in categorias:
            print(f"  • {c[0]}: {c[1]}")

def main():
    i = InglesCompletoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    i.set_usuario(username)
    
    while True:
        if not i.ver_menu():
            break

if __name__ == '__main__':
    main()
