#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Lecciones de Gramática-Cursos - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class LeccionesGramaticaCursosSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 LECCIONES DE GRAMÁTICA-CURSOS")
        print("=" * 40)
        print("1. Ver lecciones por grado")
        print("2. Ver por categoría")
        print("3. Ver Sintaxis Quest")
        print("4. Ver Menús de lecciones")
        print("5. Lección aleatoria")
        print("6. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_por_grado()
        elif opcion == '2':
            self.ver_por_categoria()
        elif opcion == '3':
            self.ver_sintaxis_quest()
        elif opcion == '4':
            self.ver_menus()
        elif opcion == '5':
            self.aleatorio()
        elif opcion == '6':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_por_grado(self):
        grados = db.consultar('SELECT DISTINCT grado FROM lecciones_gramatica_cursos')
        print("\n📂 GRADOS DISPONIBLES:")
        for g in grados:
            count = db.consultar_uno('SELECT COUNT(*) FROM lecciones_gramatica_cursos WHERE grado = ?', [g[0]])[0]
            print(f"  • {g[0]}: {count} lecciones")
        
        grado = input("\nElige un grado: ").strip()
        lecciones = db.consultar('''
            SELECT leccion_id, titulo, categoria FROM lecciones_gramatica_cursos WHERE grado = ?
        ''', [grado])
        if lecciones:
            print(f"\n📖 Lecciones de {grado}:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}... ({l['categoria']})")
    
    def ver_por_categoria(self):
        categorias = db.consultar('SELECT DISTINCT categoria FROM lecciones_gramatica_cursos')
        print("\n📂 CATEGORÍAS:")
        for c in categorias:
            count = db.consultar_uno('SELECT COUNT(*) FROM lecciones_gramatica_cursos WHERE categoria = ?', [c[0]])[0]
            print(f"  • {c[0]}: {count} lecciones")
        
        cat = input("\nElige una categoría: ").strip()
        lecciones = db.consultar('SELECT leccion_id, grado, titulo FROM lecciones_gramatica_cursos WHERE categoria = ?', [cat])
        if lecciones:
            print(f"\n📖 Lecciones de '{cat}':")
            for l in lecciones[:10]:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}... ({l['grado']})")
    
    def ver_sintaxis_quest(self):
        grados = db.consultar('SELECT DISTINCT grado FROM sintaxis_quest_cursos')
        print("\n📚 SINTAXIS QUEST:")
        for g in grados:
            count = db.consultar_uno('SELECT COUNT(*) FROM sintaxis_quest_cursos WHERE grado = ?', [g[0]])[0]
            print(f"  • {g[0]}: {count} lecciones")
        
        grado = input("\nElige un grado: ").strip()
        lecciones = db.consultar('''
            SELECT leccion_id, titulo, version FROM sintaxis_quest_cursos WHERE grado = ?
        ''', [grado])
        if lecciones:
            print(f"\n📖 Sintaxis Quest {grado}:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}... ({l['version']})")
    
    def ver_menus(self):
        menus = db.consultar('SELECT id, titulo, leccion_id, grado FROM menus_lecciones')
        print("\n📋 MENÚS DE LECCIONES:")
        for m in menus:
            print(f"  • {m['titulo'][:50]}... (Lección {m['leccion_id'] or '?'}, {m['grado']})")
    
    def aleatorio(self):
        leccion = db.consultar_uno('SELECT * FROM lecciones_gramatica_cursos ORDER BY RANDOM() LIMIT 1')
        if leccion:
            print(f"\n🎯 LECCIÓN ALEATORIA:")
            print(f"📌 Grado: {leccion['grado']}")
            print(f"📖 Lección: {leccion['leccion_id'] or 'N/A'}")
            print(f"📝 Título: {leccion['titulo'][:80]}...")
            print(f"📂 Categoría: {leccion['categoria']}")
    
    def estadisticas(self):
        total = db.consultar_uno('SELECT COUNT(*) FROM lecciones_gramatica_cursos')[0]
        sintaxis = db.consultar_uno('SELECT COUNT(*) FROM sintaxis_quest_cursos')[0]
        menus = db.consultar_uno('SELECT COUNT(*) FROM menus_lecciones')[0]
        
        print(f"\n📊 ESTADÍSTICAS")
        print("=" * 40)
        print(f"📚 Lecciones: {total}")
        print(f"📚 Sintaxis Quest: {sintaxis}")
        print(f"📋 Menús: {menus}")
        
        grados = db.consultar('''
            SELECT grado, COUNT(*) FROM lecciones_gramatica_cursos 
            GROUP BY grado ORDER BY COUNT(*) DESC
        ''')
        print("\n📂 Distribución por grado:")
        for g in grados[:10]:
            print(f"  • {g[0]}: {g[1]} lecciones")

def main():
    l = LeccionesGramaticaCursosSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    
    while True:
        if not l.ver_menu():
            break

if __name__ == '__main__':
    main()
