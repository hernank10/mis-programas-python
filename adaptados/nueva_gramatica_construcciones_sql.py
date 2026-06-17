#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Nueva Gramática - Ejercicios Construcciones II - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class NuevaGramaticaConstruccionesSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 NUEVA GRAMÁTICA - EJERCICIOS CONSTRUCCIONES II")
        print("=" * 40)
        print("1. Ver ejercicios de sintaxis avanzada")
        print("2. Ver programas con interfaz")
        print("3. Ver ejercicios por categoría")
        print("4. Ejercicio aleatorio")
        print("5. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_sintaxis_avanzada()
        elif opcion == '2':
            self.ver_programas()
        elif opcion == '3':
            self.ver_por_categoria()
        elif opcion == '4':
            self.aleatorio()
        elif opcion == '5':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_sintaxis_avanzada(self):
        ejercicios = db.consultar('SELECT id, titulo, nivel FROM ejercicios_sintaxis_avanzada')
        print("\n📖 EJERCICIOS DE SINTAXIS AVANZADA:")
        for e in ejercicios:
            print(f"  {e['id']}. {e['titulo'][:50]}... ({e['nivel']})")
    
    def ver_programas(self):
        programas = db.consultar('SELECT id, nombre, tecnologia FROM programas_construcciones')
        print("\n📚 PROGRAMAS CON INTERFAZ:")
        for p in programas:
            print(f"  {p['id']}. {p['nombre'][:50]}... ({p['tecnologia']})")
    
    def ver_por_categoria(self):
        categorias = db.consultar('SELECT DISTINCT categoria FROM ejercicios_construcciones')
        print("\n📂 CATEGORÍAS:")
        for c in categorias:
            if c[0]:
                count = db.consultar_uno('SELECT COUNT(*) FROM ejercicios_construcciones WHERE categoria = ?', [c[0]])[0]
                print(f"  • {c[0]}: {count} ejercicios")
        
        cat = input("\nElige una categoría: ").strip()
        ejercicios = db.consultar('SELECT id, titulo FROM ejercicios_construcciones WHERE categoria = ?', [cat])
        if ejercicios:
            print(f"\n📖 Ejercicios de '{cat}':")
            for e in ejercicios:
                print(f"  • {e['titulo'][:60]}...")
    
    def aleatorio(self):
        # Elegir aleatoriamente entre los tres tipos
        opciones = ['ejercicios_construcciones', 'ejercicios_sintaxis_avanzada', 'programas_construcciones']
        tabla = random.choice(opciones)
        
        item = db.consultar_uno(f'SELECT * FROM {tabla} ORDER BY RANDOM() LIMIT 1')
        if item:
            print(f"\n🎯 ELEMENTO ALEATORIO:")
            print(f"📌 Tabla: {tabla}")
            if 'titulo' in item.keys():
                print(f"📝 Título: {item['titulo'][:80]}...")
            elif 'nombre' in item.keys():
                print(f"📝 Nombre: {item['nombre'][:80]}...")
    
    def estadisticas(self):
        total1 = db.consultar_uno('SELECT COUNT(*) FROM ejercicios_construcciones')[0]
        total2 = db.consultar_uno('SELECT COUNT(*) FROM programas_construcciones')[0]
        total3 = db.consultar_uno('SELECT COUNT(*) FROM ejercicios_sintaxis_avanzada')[0]
        total4 = db.consultar_uno('SELECT COUNT(*) FROM datos_construcciones')[0]
        
        print(f"\n📊 ESTADÍSTICAS")
        print("=" * 40)
        print(f"📖 Ejercicios generales: {total1}")
        print(f"📚 Programas con interfaz: {total2}")
        print(f"📖 Ejercicios de sintaxis avanzada: {total3}")
        print(f"📄 Datos (JSON): {total4}")
        print(f"📊 Total: {total1 + total2 + total3 + total4}")
        
        # Categorías más comunes
        categorias = db.consultar('''
            SELECT categoria, COUNT(*) FROM ejercicios_construcciones 
            GROUP BY categoria ORDER BY COUNT(*) DESC
        ''')
        print("\n📂 Categorías de ejercicios:")
        for c in categorias:
            if c[0]:
                print(f"  • {c[0]}: {c[1]}")

def main():
    n = NuevaGramaticaConstruccionesSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    n.set_usuario(username)
    
    while True:
        if not n.ver_menu():
            break

if __name__ == '__main__':
    main()
