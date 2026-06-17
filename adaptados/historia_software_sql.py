#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Historia del Software Educativo - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class HistoriaSoftwareSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 HISTORIA DEL SOFTWARE EDUCATIVO")
        print("=" * 40)
        print("1. Ver todos los programas")
        print("2. Ver por tipo")
        print("3. Ver por tecnología")
        print("4. Programa aleatorio")
        print("5. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_todos()
        elif opcion == '2':
            self.ver_por_tipo()
        elif opcion == '3':
            self.ver_por_tecnologia()
        elif opcion == '4':
            self.aleatorio()
        elif opcion == '5':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_todos(self):
        programas = db.consultar('SELECT id, nombre, tipo, tecnologia FROM software_educativo')
        print("\n📋 PROGRAMAS EDUCATIVOS")
        print("=" * 50)
        for p in programas:
            print(f"  {p['id']}. {p['nombre'][:40]} ({p['tipo']}) - {p['tecnologia']}")
    
    def ver_por_tipo(self):
        tipos = db.consultar('SELECT DISTINCT tipo FROM software_educativo')
        print("\n📂 TIPOS DISPONIBLES:")
        for t in tipos:
            count = db.consultar_uno('SELECT COUNT(*) FROM software_educativo WHERE tipo = ?', [t[0]])[0]
            print(f"  • {t[0]}: {count} programas")
        
        tipo = input("\nElige un tipo: ").strip()
        programas = db.consultar('SELECT id, nombre, tecnologia FROM software_educativo WHERE tipo = ?', [tipo])
        if programas:
            print(f"\n📋 Programas de tipo '{tipo}':")
            for p in programas:
                print(f"  • {p['nombre']} ({p['tecnologia']})")
    
    def ver_por_tecnologia(self):
        tecnologias = db.consultar('SELECT DISTINCT tecnologia FROM software_educativo')
        print("\n💻 TECNOLOGÍAS:")
        for t in tecnologias:
            if t[0]:
                count = db.consultar_uno('SELECT COUNT(*) FROM software_educativo WHERE tecnologia LIKE ?', [f'%{t[0]}%'])[0]
                print(f"  • {t[0]}: {count} programas")
    
    def aleatorio(self):
        programa = db.consultar_uno('SELECT * FROM software_educativo ORDER BY RANDOM() LIMIT 1')
        if programa:
            print(f"\n🎯 PROGRAMA ALEATORIO:")
            print(f"📌 Nombre: {programa['nombre']}")
            print(f"📂 Tipo: {programa['tipo']}")
            print(f"💻 Tecnología: {programa['tecnologia']}")
            print(f"📄 Contenido: {programa['contenido'][:500]}..." if programa['contenido'] else "")
    
    def estadisticas(self):
        total = db.consultar_uno('SELECT COUNT(*) FROM software_educativo')[0]
        print(f"\n📊 ESTADÍSTICAS")
        print("=" * 40)
        print(f"📚 Total programas: {total}")
        
        tipos = db.consultar('SELECT tipo, COUNT(*) FROM software_educativo GROUP BY tipo')
        print("\n📂 Por tipo:")
        for t in tipos:
            print(f"  • {t[0]}: {t[1]}")

def main():
    h = HistoriaSoftwareSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    h.set_usuario(username)
    
    while True:
        if not h.ver_menu():
            break

if __name__ == '__main__':
    main()
