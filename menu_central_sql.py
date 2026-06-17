#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MENÚ CENTRAL SQL - Ecosistema Educativo Unificado
Autor: @Hernank10
"""

import os
import sys
import subprocess
from db_manager import db

class MenuCentralSQL:
    def __init__(self):
        self.usuario_id = None
        self.username = None
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def login(self):
        """Sistema de inicio de sesión unificado"""
        self.limpiar_pantalla()
        print("=" * 60)
        print("  🐍 LMS EDUCATIVO - ECOSISTEMA SQL")
        print("=" * 60)
        
        # Mostrar usuarios disponibles
        usuarios = db.consultar('SELECT id, username, rol FROM usuarios WHERE activo = 1')
        print("\n📋 Usuarios disponibles:")
        for u in usuarios:
            print(f"  • {u['username']} ({u['rol']})")
        
        print("\n1. Iniciar sesión")
        print("2. Crear nuevo usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '0':
            return False
        
        if opcion == '2':
            username = input("Nuevo usuario: ").strip()
            if db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username]):
                print(f"⚠️ El usuario '{username}' ya existe")
                input("Presiona Enter...")
                return self.login()
            
            password = input("Contraseña: ").strip()
            email = input("Email: ").strip()
            
            db.ejecutar('''
            INSERT INTO usuarios (username, password, email, rol)
            VALUES (?, ?, ?, ?)
            ''', [username, password, email, 'estudiante'])
            print(f"✅ Usuario '{username}' creado")
            self.username = username
            self.usuario_id = db.consultar_uno('SELECT id FROM usuarios WHERE username = ?', [username])[0]
            return True
        
        username = input("Usuario: ").strip()
        user = db.consultar_uno('SELECT id, username, rol FROM usuarios WHERE username = ? AND activo = 1', [username])
        
        if not user:
            print(f"❌ Usuario '{username}' no encontrado")
            input("Presiona Enter...")
            return self.login()
        
        self.username = user['username']
        self.usuario_id = user['id']
        print(f"\n✅ ¡Bienvenido, {self.username}!")
        input("Presiona Enter para continuar...")
        return True
    
    def mostrar_menu(self):
        """Mostrar menú principal"""
        self.limpiar_pantalla()
        print("=" * 60)
        print(f"  📚 ECOSISTEMA EDUCATIVO - {self.username}")
        print("=" * 60)
        print("\n📖 PROGRAMAS DE APRENDIZAJE:")
        print("  1. 🏛️  Latín - Declinaciones")
        print("  2. 🇬🇧  Inglés - Entrenador")
        print("  3. 🎮  Juegos de Texto")
        print("  4. 📖  Gramática Española (RAE)")
        print("  5. 📚  Vocabulario (ES/EN/LA)")
        print("  6. 📋  Cuestionarios")
        print("  7. 📖  Lectura Comprensiva")
        print("  8. ✍️  Escritura Creativa")
        print("  9. 🗣️  Pronunciación")
        print(" 10. 🔤  Conjugación de Verbos")
        print(" 11. 📝  Sinónimos y Antónimos")
        print(" 12. 🔍  Análisis Sintáctico")
        print(" 13. ⏳  Tiempos Verbales")
        print(" 14. 📜  Refranes y Expresiones")
        print(" 15. 📝  Exámenes de Práctica
 16. 🎯  Dictado Interactivo
 17. 🧩  Sopa de Letras
 18. 🎯  Ahorcado
 19. 🎯  Trivia Cultural
 20. 📝  Completar Oraciones
 21. 🔤  Ordenar Palabras
 22. 🔤  Palabras Compuestas
 23. 📝  Palabra Correcta
 24. 🔤  Prefijos
 25. 📚  Sustantivos Colectivos")
        print(" 16. 📊  Ver mi progreso")
        print("  0. ❌  Salir")
        print("-" * 60)
    
    def ejecutar_programa(self, script):
        """Ejecutar un programa Python con el usuario actual"""
        cmd = f'python3 {script}'
        os.system(cmd)
        input("\nPresiona Enter para volver al menú...")
    
    def ver_progreso(self):
        """Ver progreso general del usuario"""
        print("\n📊 MI PROGRESO GENERAL")
        print("=" * 60)
        
        # Estadísticas generales
        stats = db.consultar_uno('''
            SELECT 
                COUNT(DISTINCT curso_id) as cursos,
                SUM(CASE WHEN completado = 1 THEN 1 ELSE 0 END) as lecciones,
                SUM(puntaje) as puntos
            FROM progreso
            WHERE usuario_id = ?
        ''', [self.usuario_id])
        
        if stats:
            print(f"📚 Cursos iniciados: {stats[0] or 0}")
            print(f"📖 Lecciones completadas: {stats[1] or 0}")
            print(f"🏆 Puntos totales: {stats[2] or 0}")
        
        # Progreso por idioma/módulo
        print("\n📊 PROGRESO POR MÓDULO:")
        modulos = [
            ('Latín', 'progreso_latin'),
            ('Inglés', 'progreso_ingles'),
            ('Gramática', 'progreso_gramatica'),
            ('Vocabulario', 'progreso_vocabulario'),
        ]
        
        for nombre, tabla in modulos:
            try:
                count = db.consultar_uno(f'SELECT COUNT(*) FROM {tabla} WHERE usuario_id = ?', [self.usuario_id])
                if count and count[0] > 0:
                    print(f"  • {nombre}: {count[0]} ejercicios practicados")
                else:
                    print(f"  • {nombre}: ⏳ Sin progreso aún")
            except:
                print(f"  • {nombre}: ⏳ Sin progreso aún")
    
    def run(self):
        """Ejecutar el menú principal"""
        if not self.login():
            print("👋 ¡Hasta luego!")
            return
        
        programas = {
            '1': 'adaptados/latin_declinaciones_sql.py',
            '2': 'adaptados/ingles_tutor_sql.py',
            '3': 'adaptados/juegos_texto_sql.py',
            '4': 'adaptados/gramatica_rae_sql.py',
            '5': 'adaptados/vocabulario_sql.py',
            '6': 'adaptados/masivos/cuestionarios_sql.py',
            '7': 'adaptados/masivos/lectura_comprensiva_sql.py',
            '8': 'adaptados/masivos/escritura_creativa_sql.py',
            '9': 'adaptados/masivos/pronunciacion_sql.py',
            '10': 'adaptados/masivos/conjugacion_verbos_sql.py',
            '11': 'adaptados/masivos/sinonimos_antonimos_sql.py',
            '12': 'adaptados/masivos/analisis_sintactico_sql.py',
            '13': 'adaptados/masivos/tiempos_verbales_sql.py',
            '14': 'adaptados/masivos/refranes_sql.py',
            '15': 'adaptados/masivos/examenes_practica_sql.py',
            '16': 'adaptados/masivos2/dictado_sql.py',
            '17': 'adaptados/masivos2/sopa_letras_sql.py',
            '18': 'adaptados/masivos2/ahorcado_sql.py',
            '19': 'adaptados/masivos2/trivia_cultural_sql.py',
            '20': 'adaptados/masivos2/completar_oraciones_sql.py',
            '21': 'adaptados/masivos2/ordenar_palabras_sql.py',
            '22': 'adaptados/masivos2/palabras_compuestas_sql.py',
            '23': 'adaptados/masivos2/palabra_correcta_sql.py',
            '24': 'adaptados/masivos2/prefijos_sql.py',
            '25': 'adaptados/masivos2/sustantivos_colectivos_sql.py',
        }
        
        while True:
            self.mostrar_menu()
            opcion = input("\nElige una opción: ").strip()
            
            if opcion == '0':
                print("👋 ¡Hasta luego!")
                break
            elif opcion == '16':
                self.ver_progreso()
                input("\nPresiona Enter para continuar...")
            elif opcion in programas:
                self.ejecutar_programa(programas[opcion])
            else:
                print("❌ Opción no válida")
                input("Presiona Enter para continuar...")

if __name__ == '__main__':
    menu = MenuCentralSQL()
    menu.run()
