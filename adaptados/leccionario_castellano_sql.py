#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador del Leccionario de Lengua Castellana - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class LeccionarioCastellanoSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 LECCIONARIO DE LA LENGUA CASTELLANA")
        print("=" * 40)
        print("1. Ver lecciones por grado")
        print("2. Ver programas educativos")
        print("3. Lección aleatoria")
        print("4. Estadísticas")
        print("5. Buscar por grado")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_por_grado()
        elif opcion == '2':
            self.ver_programas()
        elif opcion == '3':
            self.aleatorio()
        elif opcion == '4':
            self.estadisticas()
        elif opcion == '5':
            self.buscar_por_grado()
        elif opcion == '0':
            return False
        return True
    
    def ver_por_grado(self):
        grados = db.consultar('SELECT DISTINCT grado FROM lecciones_castellano_grados')
        print("\n📂 GRADOS DISPONIBLES:")
        for g in grados:
            count = db.consultar_uno('SELECT COUNT(*) FROM lecciones_castellano_grados WHERE grado = ?', [g[0]])[0]
            print(f"  • {g[0]}: {count} lecciones")
        
        grado = input("\nElige un grado: ").strip()
        lecciones = db.consultar('SELECT leccion_id, titulo FROM lecciones_castellano_grados WHERE grado = ?', [grado])
        if lecciones:
            print(f"\n📖 Lecciones de {grado}:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:60]}...")
    
    def ver_programas(self):
        programas = db.consultar('SELECT id, nombre FROM programas_castellano')
        print("\n📚 PROGRAMAS EDUCATIVOS:")
        for p in programas:
            print(f"  {p['id']}. {p['nombre'][:60]}...")
    
    def aleatorio(self):
        leccion = db.consultar_uno('SELECT * FROM lecciones_castellano_grados ORDER BY RANDOM() LIMIT 1')
        if leccion:
            print(f"\n🎯 LECCIÓN ALEATORIA:")
            print(f"📌 Grado: {leccion['grado']}")
            print(f"📖 Lección: {leccion['leccion_id'] or 'N/A'}")
            print(f"📝 Título: {leccion['titulo']}")
    
    def estadisticas(self):
        total = db.consultar_uno('SELECT COUNT(*) FROM lecciones_castellano_grados')[0]
        programas = db.consultar_uno('SELECT COUNT(*) FROM programas_castellano')[0]
        print(f"\n📊 ESTADÍSTICAS DEL LECCIONARIO")
        print("=" * 40)
        print(f"📚 Total lecciones: {total}")
        print(f"📚 Programas educativos: {programas}")
        
        grados = db.consultar('SELECT grado, COUNT(*) FROM lecciones_castellano_grados GROUP BY grado ORDER BY COUNT(*) DESC')
        print("\n📂 Distribución por grado:")
        for g in grados[:10]:
            print(f"  • {g[0]}: {g[1]} lecciones")
    
    def buscar_por_grado(self):
        grado = input("\n🔍 Ingresa el grado (ej: 5º Grado): ").strip()
        lecciones = db.consultar('''
            SELECT leccion_id, titulo FROM lecciones_castellano_grados 
            WHERE grado LIKE ? 
            LIMIT 20
        ''', [f'%{grado}%'])
        if lecciones:
            print(f"\n📖 Lecciones encontradas:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:60]}...")
        else:
            print("❌ No se encontraron lecciones para ese grado")

def main():
    l = LeccionarioCastellanoSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    
    while True:
        if not l.ver_menu():
            break

if __name__ == '__main__':
    main()
