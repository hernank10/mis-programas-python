#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explorador de Bello Gramar - Versión SQL"""

import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class BelloGramarSQL:
    def __init__(self):
        self.usuario_id = None
    
    def set_usuario(self, username):
        user = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_menu(self):
        print("\n📚 BELLO GRAMAR - SINTaxis ESPAÑOLA")
        print("=" * 40)
        print("1. Ver ejercicios de sintaxis")
        print("2. Ver comparación de igualdad")
        print("3. Ver enumeración sintáctica")
        print("4. Elemento aleatorio")
        print("5. Estadísticas")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            self.ver_sintaxis()
        elif opcion == '2':
            self.ver_comparacion()
        elif opcion == '3':
            self.ver_enumeracion()
        elif opcion == '4':
            self.aleatorio()
        elif opcion == '5':
            self.estadisticas()
        elif opcion == '0':
            return False
        return True
    
    def ver_sintaxis(self):
        ejercicios = db.consultar('SELECT id, titulo, categoria FROM ejercicios_sintaxis_bello')
        print("\n📖 EJERCICIOS DE SINTAXIS:")
        for e in ejercicios:
            print(f"  {e['id']}. {e['titulo'][:50]}... ({e['categoria']})")
    
    def ver_comparacion(self):
        ejercicios = db.consultar('SELECT id, titulo, tecnologia FROM comparacion_igualdad')
        print("\n📚 COMPARACIÓN DE IGUALDAD:")
        for e in ejercicios:
            print(f"  {e['id']}. {e['titulo'][:50]}... ({e['tecnologia']})")
    
    def ver_enumeracion(self):
        ejercicios = db.consultar('SELECT id, titulo, tipo FROM enumeracion_sintactica')
        print("\n📚 ENUMERACIÓN SINTÁCTICA:")
        for e in ejercicios:
            print(f"  {e['id']}. {e['titulo'][:50]}... ({e['tipo']})")
    
    def aleatorio(self):
        tablas = ['ejercicios_sintaxis_bello', 'comparacion_igualdad', 'enumeracion_sintactica']
        tabla = random.choice(tablas)
        
        item = db.consultar_uno(f'SELECT * FROM {tabla} ORDER BY RANDOM() LIMIT 1')
        if item:
            print(f"\n🎯 ELEMENTO ALEATORIO:")
            print(f"📌 Tabla: {tabla}")
            for key in item.keys():
                if key not in ['contenido']:
                    print(f"  {key}: {item[key]}")
    
    def estadisticas(self):
        total1 = db.consultar_uno('SELECT COUNT(*) FROM ejercicios_sintaxis_bello')[0]
        total2 = db.consultar_uno('SELECT COUNT(*) FROM comparacion_igualdad')[0]
        total3 = db.consultar_uno('SELECT COUNT(*) FROM enumeracion_sintactica')[0]
        
        print(f"\n📊 ESTADÍSTICAS DE BELLO GRAMAR")
        print("=" * 40)
        print(f"📖 Ejercicios de sintaxis: {total1}")
        print(f"📚 Comparación de igualdad: {total2}")
        print(f"📚 Enumeración sintáctica: {total3}")
        print(f"📊 Total: {total1 + total2 + total3}")

def main():
    b = BelloGramarSQL()
    print("\n🔑 Iniciar sesión")
    username = input("Usuario: ").strip()
    b.set_usuario(username)
    
    while True:
        if not b.ver_menu():
            break

if __name__ == '__main__':
    main()
