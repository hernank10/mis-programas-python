#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRENADOR DE INGLÉS - Versión SQL
Adaptado para usar la base de datos central
Autor: @Hernank10
"""

import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class InglesTutorSQL:
    """Entrenador interactivo de inglés con SQL"""
    
    def __init__(self):
        self.usuario_id = None
        self._verificar_tablas()
    
    def _verificar_tablas(self):
        """Verificar que las tablas existen"""
        try:
            db.consultar("SELECT 1 FROM ejercicios_ingles LIMIT 1")
        except:
            print("⚠️ Tabla 'ejercicios_ingles' no encontrada. Ejecuta primero el script SQL.")
            self._crear_ejercicios_ejemplo()
    
    def _crear_ejercicios_ejemplo(self):
        """Crear ejercicios de ejemplo si la tabla está vacía"""
        ejercicios = [
            # Plurales
            ('plurales', '¿Cuál es el plural de "cat"?', 'cats', 'Los plurales regulares añaden -s', 1),
            ('plurales', '¿Cuál es el plural de "bus"?', 'buses', 'Los plurales terminados en -s, -x, -ch, -sh añaden -es', 1),
            ('plurales', '¿Cuál es el plural de "child"?', 'children', 'Plural irregular', 2),
            
            # Verbos
            ('verbos', '¿Cuál es el pasado de "go"?', 'went', 'Verbo irregular', 2),
            ('verbos', '¿Cuál es el pasado de "eat"?', 'ate', 'Verbo irregular', 2),
            ('verbos', '¿Cuál es el participio de "eat"?', 'eaten', 'Verbo irregular', 2),
            
            # Vocabulario
            ('vocabulario', '¿Cómo se dice "gato" en inglés?', 'cat', 'Animal común', 1),
            ('vocabulario', '¿Cómo se dice "perro" en inglés?', 'dog', 'Animal común', 1),
            ('vocabulario', '¿Cómo se dice "casa" en inglés?', 'house', 'Lugar donde se vive', 1),
            ('vocabulario', '¿Cómo se dice "libro" en inglés?', 'book', 'Objeto para leer', 1),
            
            # Tiempos verbales
            ('tiempos', 'Completa: "She ____ to school every day"', 'goes', 'Tercera persona singular del presente simple', 2),
            ('tiempos', 'Completa: "They ____ playing football now"', 'are', 'Presente continuo', 2),
            ('tiempos', 'Completa: "I ____ already eaten"', 'have', 'Presente perfecto', 2),
            
            # Preposiciones
            ('preposiciones', 'Completa: "I am interested ____ music"', 'in', 'Interesado en algo', 2),
            ('preposiciones', 'Completa: "She is good ____ math"', 'at', 'Bueno en algo', 2),
            
            # Adjetivos
            ('adjetivos', 'Completa: "This is the ____ (big) house"', 'biggest', 'Superlativo', 2),
            ('adjetivos', 'Completa: "She is ____ (tall) than me"', 'taller', 'Comparativo', 2),
        ]
        
        for e in ejercicios:
            db.ejecutar('''
            INSERT OR IGNORE INTO ejercicios_ingles 
            (categoria, pregunta, respuesta_correcta, explicacion, dificultad)
            VALUES (?, ?, ?, ?, ?)
            ''', e)
        
        print(f"✅ Creados {len(ejercicios)} ejercicios de inglés")
    
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
    
    def ver_categorias(self):
        """Ver categorías disponibles"""
        categorias = db.consultar('SELECT DISTINCT categoria, COUNT(*) as total FROM ejercicios_ingles GROUP BY categoria')
        print("\n📚 CATEGORÍAS DISPONIBLES:")
        print("-" * 40)
        for c in categorias:
            print(f"  • {c['categoria']}: {c['total']} ejercicios")
        print("  • todas: todos los ejercicios")
    
    def practicar(self, categoria=None, num_preguntas=10):
        """Practicar ejercicios de inglés"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        sql = 'SELECT * FROM ejercicios_ingles'
        params = []
        
        if categoria and categoria != 'todas':
            sql += ' WHERE categoria = ?'
            params.append(categoria)
        
        sql += ' ORDER BY RANDOM() LIMIT ?'
        params.append(num_preguntas)
        
        ejercicios = db.consultar(sql, params)
        
        if not ejercicios:
            print("❌ No hay ejercicios disponibles en esta categoría")
            return
        
        aciertos = 0
        total = len(ejercicios)
        
        print("\n" + "=" * 60)
        print(f"  📝 PRACTICANDO INGLÉS ({total} ejercicios)")
        if categoria and categoria != 'todas':
            print(f"  Categoría: {categoria}")
        print("=" * 60)
        print("  Escribe 'salir' para terminar\n")
        
        for i, e in enumerate(ejercicios, 1):
            print(f"\n{i}/{total} - {e['pregunta']}")
            
            if e['explicacion']:
                print(f"💡 Pista: {e['explicacion']}")
            
            respuesta = input("Tu respuesta: ").strip()
            
            if respuesta.lower() == 'salir':
                break
            
            if respuesta.lower() == e['respuesta_correcta'].lower():
                print("✅ ¡Correcto! 🎉")
                aciertos += 1
                self._guardar_progreso(e['id'], True)
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {e['respuesta_correcta']}")
                if e['explicacion']:
                    print(f"📚 {e['explicacion']}")
                self._guardar_progreso(e['id'], False)
        
        if total > 0:
            porcentaje = aciertos * 100 // total
            print("\n" + "=" * 60)
            print(f"📊 Resultado: {aciertos}/{total} correctas ({porcentaje}%)")
            
            if porcentaje >= 80:
                print("🏆 ¡Excelente! Sigue así.")
            elif porcentaje >= 60:
                print("👍 Buen trabajo. Practica un poco más.")
            else:
                print("📚 Sigue practicando, ¡tú puedes!")
    
    def _guardar_progreso(self, ejercicio_id, acertado):
        """Guardar progreso en la base de datos"""
        if not self.usuario_id:
            return
        
        # Buscar registro existente
        progreso = db.consultar_uno(
            'SELECT id, aciertos, intentos FROM progreso_ingles WHERE usuario_id = ? AND ejercicio_id = ?',
            [self.usuario_id, ejercicio_id]
        )
        
        if progreso:
            aciertos = progreso[1] + (1 if acertado else 0)
            intentos = progreso[2] + 1
            db.ejecutar(
                'UPDATE progreso_ingles SET aciertos = ?, intentos = ? WHERE id = ?',
                [aciertos, intentos, progreso[0]]
            )
        else:
            db.ejecutar('''
            INSERT INTO progreso_ingles (usuario_id, ejercicio_id, aciertos, intentos)
            VALUES (?, ?, ?, ?)
            ''', [self.usuario_id, ejercicio_id, 1 if acertado else 0, 1])
    
    def ver_progreso(self):
        """Ver progreso del usuario en inglés"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        resultados = db.consultar('''
            SELECT 
                e.categoria,
                e.pregunta,
                p.aciertos,
                p.intentos,
                ROUND(p.aciertos * 100.0 / p.intentos, 1) as porcentaje
            FROM progreso_ingles p
            JOIN ejercicios_ingles e ON p.ejercicio_id = e.id
            WHERE p.usuario_id = ?
            ORDER BY porcentaje DESC
        ''', [self.usuario_id])
        
        if not resultados:
            print("📊 No hay datos de progreso aún.")
            return
        
        print("\n📊 PROGRESO EN INGLÉS")
        print("=" * 60)
        print(f"{'Categoría':<15} {'Pregunta':<25} {'Aciertos':<10} {'%':<8}")
        print("-" * 60)
        
        total_aciertos = 0
        total_intentos = 0
        
        for r in resultados:
            pregunta_corta = r['pregunta'][:25] + '...' if len(r['pregunta']) > 25 else r['pregunta']
            print(f"{r['categoria']:<15} {pregunta_corta:<25} {r['aciertos']}/{r['intentos']:<7} {r['porcentaje']:<8}%")
            total_aciertos += r['aciertos']
            total_intentos += r['intentos']
        
        if total_intentos > 0:
            print("-" * 60)
            print(f"{'TOTAL':<15} {'':<25} {total_aciertos}/{total_intentos:<7} {total_aciertos*100//total_intentos:<8}%")
    
    def _menu_usuario(self):
        """Menú de usuario"""
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
    tutor = InglesTutorSQL()
    
    print("\n🔑 INICIAR SESIÓN")
    if not tutor._menu_usuario():
        return
    
    print(f"✅ Bienvenido!")
    
    while True:
        print("\n" + "=" * 40)
        print("  🇬🇧 ENTRENADOR DE INGLÉS")
        print("=" * 40)
        print("1. Practicar")
        print("2. Ver categorías")
        print("3. Ver mi progreso")
        print("4. Cambiar usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            tutor.ver_categorias()
            categoria = input("\nElige una categoría (o 'todas'): ").strip()
            num = input("Número de preguntas (Enter para 10): ").strip()
            try:
                num_preguntas = int(num) if num else 10
            except:
                num_preguntas = 10
            tutor.practicar(categoria if categoria else None, num_preguntas)
        elif opcion == '2':
            tutor.ver_categorias()
        elif opcion == '3':
            tutor.ver_progreso()
        elif opcion == '4':
            tutor._menu_usuario()
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")

if __name__ == '__main__':
    main()
