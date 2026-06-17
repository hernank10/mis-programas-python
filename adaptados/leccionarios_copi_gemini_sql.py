#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Leccionarios Copi y Gemini - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class LeccionariosCopiGeminiSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 LECCIONARIOS COPI Y GEMEINI")
        print("=" * 40)
        print("1. Ver lecciones por grado")
        print("2. Ver por versión (Copi/Gemini)")
        print("3. Ver Sintaxis Quest EDU")
        print("4. Lección aleatoria")
        print("5. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_por_grado()
        elif opcion == '2':
            self.ver_por_version()
        elif opcion == '3':
            self.ver_sintaxis_quest()
        elif opcion == '4':
            self.aleatorio()
        elif opcion == '5':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_por_grado(self):
        grados = db.consultar('SELECT DISTINCT grado FROM lecciones_copi_gemini')
        print("\n📂 GRADOS DISPONIBLES:")
        for g in grados:
            count = db.consultar_uno('SELECT COUNT(*) FROM lecciones_copi_gemini WHERE grado = ?', [g[0]])[0]
            print(f"  • {g[0]}: {count} lecciones")
        
        grado = input("\nElige un grado: ").strip()
        lecciones = db.consultar('''
            SELECT leccion_id, titulo, version FROM lecciones_copi_gemini WHERE grado = ?
        ''', [grado])
        if lecciones:
            print(f"\n📖 Lecciones de {grado}:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}... ({l['version']})")
    
    def ver_por_version(self):
        print("\n📂 VERSIONES:")
        versiones = db.consultar('SELECT DISTINCT version FROM lecciones_copi_gemini')
        for v in versiones:
            count = db.consultar_uno('SELECT COUNT(*) FROM lecciones_copi_gemini WHERE version = ?', [v[0]])[0]
            print(f"  • {v[0]}: {count} lecciones")
        
        version = input("\nElige una versión: ").strip()
        lecciones = db.consultar('SELECT leccion_id, grado, titulo FROM lecciones_copi_gemini WHERE version = ?', [version])
        if lecciones:
            print(f"\n📖 Lecciones de {version}:")
            for l in lecciones[:10]:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}... ({l['grado']})")
    
    def ver_sintaxis_quest(self):
        grados = db.consultar('SELECT DISTINCT grado FROM sintaxis_quest_edu')
        print("\n📚 SINTAXIS QUEST EDU:")
        for g in grados:
            count = db.consultar_uno('SELECT COUNT(*) FROM sintaxis_quest_edu WHERE grado = ?', [g[0]])[0]
            print(f"  • {g[0]}: {count} lecciones")
        
        grado = input("\nElige un grado: ").strip()
        lecciones = db.consultar('SELECT leccion_id, titulo FROM sintaxis_quest_edu WHERE grado = ?', [grado])
        if lecciones:
            print(f"\n📖 Lecciones de Sintaxis Quest {grado}:")
            for l in lecciones:
                print(f"  • Lección {l['leccion_id'] or '?'}: {l['titulo'][:50]}...")
    
    def aleatorio(self):
        leccion = db.consultar_uno('SELECT * FROM lecciones_copi_gemini ORDER BY RANDOM() LIMIT 1')
        if leccion:
            print(f"\n🎯 LECCIÓN ALEATORIA:")
            print(f"📌 Grado: {leccion['grado']}")
            print(f"📖 Lección: {leccion['leccion_id'] or 'N/A'}")
            print(f"📝 Título: {leccion['titulo'][:80]}...")
            print(f"📂 Versión: {leccion['version']}")
    
    def estadisticas(self):
        total = db.consultar_uno('SELECT COUNT(*) FROM lecciones_copi_gemini')[0]
        sintaxis = db.consultar_uno('SELECT COUNT(*) FROM sintaxis_quest_edu')[0]
        docs = db.consultar_uno('SELECT COUNT(*) FROM documentacion_castellano')[0]
        
        print(f"\n📊 ESTADÍSTICAS")
        print("=" * 40)
        print(f"📚 Lecciones Copi/Gemini: {total}")
        print(f"📚 Sintaxis Quest EDU: {sintaxis}")
        print(f"📄 Documentación: {docs}")
        
        grados = db.consultar('''
            SELECT grado, COUNT(*) FROM lecciones_copi_gemini 
            GROUP BY grado ORDER BY COUNT(*) DESC
        ''')
        print("\n📂 Distribución por grado:")
        for g in grados[:10]:
            print(f"  • {g[0]}: {g[1]} lecciones")

def main():
    l = LeccionariosCopiGeminiSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    l.set_usuario(username)
    
    while True:
        if not l.ver_menu():
            break

if __name__ == '__main__':
    main()
