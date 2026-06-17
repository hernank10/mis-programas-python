#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador completo de Juegos Educativos - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class JuegosCompletosSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n🎮 JUEGOS EDUCATIVOS COMPLETOS")
        print("=" * 40)
        print("1. Juegos de sintaxis")
        print("2. Juegos bilingües")
        print("3. Juegos de consola")
        print("4. Juegos Pygame")
        print("5. Juego aleatorio")
        print("6. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_sintaxis()
        elif opcion == '2':
            self.ver_bilingues()
        elif opcion == '3':
            self.ver_consola()
        elif opcion == '4':
            self.ver_pygame()
        elif opcion == '5':
            self.aleatorio()
        elif opcion == '6':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_sintaxis(self):
        juegos = db.consultar('SELECT id, nombre, categoria FROM juegos_sintaxis')
        print("\n🎮 JUEGOS DE SINTAXIS:")
        for j in juegos:
            print(f"  {j['id']}. {j['nombre'][:50]}... ({j['categoria']})")
    
    def ver_bilingues(self):
        juegos = db.consultar('SELECT id, nombre, tecnologia FROM juegos_bilingues')
        print("\n🌐 JUEGOS BILINGÜES:")
        for j in juegos:
            print(f"  {j['id']}. {j['nombre'][:50]}... ({j['tecnologia']})")
    
    def ver_consola(self):
        juegos = db.consultar('SELECT id, nombre, num_ejercicios FROM juegos_consola')
        print("\n💻 JUEGOS DE CONSOLA:")
        for j in juegos:
            print(f"  {j['id']}. {j['nombre'][:50]}... ({j['num_ejercicios']} ejercicios)")
    
    def ver_pygame(self):
        juegos = db.consultar('SELECT id, nombre FROM juegos_pygame')
        print("\n🎨 JUEGOS PYGAME:")
        for j in juegos:
            print(f"  {j['id']}. {j['nombre'][:50]}...")
    
    def aleatorio(self):
        tablas = ['juegos_sintaxis', 'juegos_bilingues', 'juegos_consola', 'juegos_pygame']
        tabla = random.choice(tablas)
        
        item = db.consultar_uno(f'SELECT * FROM {tabla} ORDER BY RANDOM() LIMIT 1')
        if item:
            print(f"\n🎯 JUEGO ALEATORIO:")
            print(f"📌 Tabla: {tabla}")
            for key in item.keys():
                if key not in ['contenido']:
                    print(f"  {key}: {item[key]}")
    
    def estadisticas(self):
        total1 = db.consultar_uno('SELECT COUNT(*) FROM juegos_sintaxis')[0]
        total2 = db.consultar_uno('SELECT COUNT(*) FROM juegos_bilingues')[0]
        total3 = db.consultar_uno('SELECT COUNT(*) FROM juegos_consola')[0]
        total4 = db.consultar_uno('SELECT COUNT(*) FROM juegos_pygame')[0]
        
        print(f"\n📊 ESTADÍSTICAS DE JUEGOS")
        print("=" * 40)
        print(f"🎮 Juegos de sintaxis: {total1}")
        print(f"🌐 Juegos bilingües: {total2}")
        print(f"💻 Juegos de consola: {total3}")
        print(f"🎨 Juegos Pygame: {total4}")
        print(f"📊 Total: {total1 + total2 + total3 + total4}")

def main():
    j = JuegosCompletosSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    j.set_usuario(username)
    
    while True:
        if not j.ver_menu():
            break

if __name__ == '__main__':
    main()
