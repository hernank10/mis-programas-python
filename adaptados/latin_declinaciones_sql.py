#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRENADOR DE DECLINACIONES LATINAS - Versión SQL
Adaptado para usar la base de datos central
Autor: @Hernank10
"""

import random
import sqlite3
import os
import sys

# Añadir el directorio padre para importar db_manager
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class DeclinacionesLatinasSQL:
    """Entrenador interactivo de declinaciones latinas con SQL"""
    
    def __init__(self):
        self.usuario_id = None
        self._verificar_tablas()
    
    def _verificar_tablas(self):
        """Verificar que las tablas existen"""
        try:
            db.consultar("SELECT 1 FROM declinaciones LIMIT 1")
        except:
            print("⚠️ Tabla 'declinaciones' no encontrada. Ejecuta primero el script SQL.")
    
    def set_usuario(self, username):
        """Establecer usuario actual"""
        user = db.consultar_uno(
            'SELECT id FROM usuarios WHERE username = ? AND activo = 1',
            [username]
        )
        if user:
            self.usuario_id = user[0]
            return True
        print(f"❌ Usuario '{username}' no encontrado o inactivo")
        return False
    
    def obtener_palabra(self, declinacion=None):
        """Obtener una palabra aleatoria de una declinación"""
        sql = 'SELECT * FROM declinaciones'
        params = []
        
        if declinacion and declinacion != 0:
            sql += ' WHERE declinacion = ?'
            params.append(declinacion)
        
        sql += ' ORDER BY RANDOM() LIMIT 1'
        
        return db.consultar_uno(sql, params)
    
    def practicar(self):
        """Iniciar práctica interactiva"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión con: set_usuario('nombre')")
            return
        
        print("\n" + "=" * 60)
        print("  🏛️ ENTRENADOR DE DECLINACIONES LATINAS (SQL)")
        print("=" * 60)
        
        # Mostrar opciones de declinación
        print("\n📋 Selecciona una declinación:")
        print("  1. Primera declinación")
        print("  2. Segunda declinación")
        print("  3. Tercera declinación")
        print("  4. Cuarta declinación")
        print("  5. Quinta declinación")
        print("  6. Todas las declinaciones")
        print("  0. Volver al menú principal")
        
        try:
            opcion = input("\nElige una opción: ").strip()
            if opcion == '0':
                return
            
            declinacion = int(opcion) if opcion in '123456' else None
            if opcion == '6':
                declinacion = None
            
            if declinacion and declinacion not in range(1, 6):
                print("❌ Opción no válida")
                return
                
        except ValueError:
            print("❌ Opción no válida")
            return
        
        # Casos para practicar
        casos = [
            ('Nominativo', 'nominativo'),
            ('Genitivo', 'genitivo'),
            ('Dativo', 'dativo'),
            ('Acusativo', 'acusativo'),
            ('Ablativo', 'ablativo'),
        ]
        
        print("\n" + "=" * 60)
        print("  📝 PRACTICANDO (escribe 'salir' para terminar)")
        print("=" * 60)
        
        aciertos = 0
        total = 0
        
        while True:
            palabra = self.obtener_palabra(declinacion)
            if not palabra:
                print("❌ No hay palabras disponibles en esta declinación")
                break
            
            # Seleccionar caso aleatorio
            caso_nombre, caso_columna = random.choice(casos)
            
            print(f"\n📖 Palabra: {palabra['palabra']}")
            print(f"   Declinación: {palabra['declinacion']}ª")
            if palabra['genero']:
                print(f"   Género: {palabra['genero']}")
            print(f"   Traducción: {palabra['traduccion']}")
            
            print(f"\n❓ ¿Cuál es el {caso_nombre} singular?")
            respuesta = input("Tu respuesta: ").strip()
            
            if respuesta.lower() == 'salir':
                break
            
            correcta = palabra[caso_columna] or "No disponible"
            
            if respuesta.lower().strip() == correcta.lower().strip():
                print("✅ ¡Correcto! 🎉")
                aciertos += 1
                self._guardar_progreso(palabra['id'], True)
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {correcta}")
                self._guardar_progreso(palabra['id'], False)
            
            total += 1
            
            # Mostrar todos los casos de la palabra
            print("\n📋 Tabla completa de la palabra:")
            print(f"   Nominativo: {palabra['nominativo']}")
            print(f"   Genitivo:   {palabra['genitivo']}")
            print(f"   Dativo:     {palabra['dativo']}")
            print(f"   Acusativo:  {palabra['acusativo']}")
            print(f"   Ablativo:   {palabra['ablativo']}")
            print("-" * 40)
        
        if total > 0:
            print(f"\n📊 Resultado final: {aciertos} aciertos de {total} ({aciertos*100//total}%)")
    
    def _guardar_progreso(self, palabra_id, acertado):
        """Guardar progreso en la base de datos"""
        if not self.usuario_id:
            return
        
        # Buscar registro existente
        progreso = db.consultar_uno(
            'SELECT id, aciertos, intentos FROM progreso_latin WHERE usuario_id = ? AND palabra_id = ?',
            [self.usuario_id, palabra_id]
        )
        
        if progreso:
            aciertos = progreso[1] + (1 if acertado else 0)
            intentos = progreso[2] + 1
            db.ejecutar(
                'UPDATE progreso_latin SET aciertos = ?, intentos = ? WHERE id = ?',
                [aciertos, intentos, progreso[0]]
            )
        else:
            db.ejecutar(
                'INSERT INTO progreso_latin (usuario_id, palabra_id, aciertos, intentos) VALUES (?, ?, ?, ?)',
                [self.usuario_id, palabra_id, 1 if acertado else 0, 1]
            )
    
    def ver_progreso(self):
        """Ver progreso del usuario"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        resultados = db.consultar('''
            SELECT 
                d.palabra,
                d.traduccion,
                p.aciertos,
                p.intentos,
                ROUND(p.aciertos * 100.0 / p.intentos, 1) as porcentaje
            FROM progreso_latin p
            JOIN declinaciones d ON p.palabra_id = d.id
            WHERE p.usuario_id = ?
            ORDER BY porcentaje DESC
        ''', [self.usuario_id])
        
        if not resultados:
            print("📊 No hay datos de progreso aún.")
            return
        
        print("\n📊 PROGRESO EN LATÍN")
        print("=" * 60)
        print(f"{'Palabra':<15} {'Traducción':<15} {'Aciertos':<10} {'Intentos':<10} {'%':<8}")
        print("-" * 60)
        
        total_aciertos = 0
        total_intentos = 0
        
        for r in resultados:
            print(f"{r['palabra']:<15} {r['traduccion']:<15} {r['aciertos']:<10} {r['intentos']:<10} {r['porcentaje']:<8}%")
            total_aciertos += r['aciertos']
            total_intentos += r['intentos']
        
        if total_intentos > 0:
            print("-" * 60)
            print(f"{'TOTAL':<15} {'':<15} {total_aciertos:<10} {total_intentos:<10} {total_aciertos*100//total_intentos:<8}%")
    
    def _menu_usuario(self):
        """Menú de usuario para elegir o crear usuario"""
        print("\n👤 SELECCIÓN DE USUARIO")
        print("=" * 40)
        usuarios = db.consultar('SELECT username, rol FROM usuarios WHERE activo = 1')
        print("\n📋 Usuarios disponibles:")
        for u in usuarios:
            print(f"  • {u['username']} ({u['rol']})")
        
        print("\n1. Usar un usuario existente")
        print("2. Crear nuevo usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '0':
            return False
        
        if opcion == '2':
            username = input("Nuevo usuario: ").strip()
            if db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username]):
                print(f"⚠️ El usuario '{username}' ya existe")
                return self._menu_usuario()
            
            password = input("Contraseña: ").strip()
            email = input("Email: ").strip()
            
            db.ejecutar('''
            INSERT INTO usuarios (username, password, email, rol)
            VALUES (?, ?, ?, ?)
            ''', [username, password, email, 'estudiante'])
            print(f"✅ Usuario '{username}' creado")
            self.set_usuario(username)
            return True
        
        username = input("Usuario: ").strip()
        return self.set_usuario(username)

def main():
    entrenador = DeclinacionesLatinasSQL()
    
    print("\n🔑 INICIAR SESIÓN")
    if not entrenador._menu_usuario():
        return
    
    print(f"✅ Bienvenido, {entrenador.usuario_id}!")
    
    while True:
        print("\n" + "=" * 40)
        print("  🏛️ ENTRENADOR DE LATÍN")
        print("=" * 40)
        print("1. Practicar declinaciones")
        print("2. Ver mi progreso")
        print("3. Cambiar usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            entrenador.practicar()
        elif opcion == '2':
            entrenador.ver_progreso()
        elif opcion == '3':
            entrenador._menu_usuario()
            if entrenador.usuario_id:
                print(f"✅ Usuario cambiado a ID: {entrenador.usuario_id}")
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")

if __name__ == '__main__':
    main()
