#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MENÚ PRINCIPAL UNIFICADO - Versión SQL
Autor: @Hernank10
"""

import os
import sys
from db_manager import db

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_cursos():
    """Ver cursos disponibles"""
    print("\n📚 CURSOS DISPONIBLES")
    print("=" * 50)
    cursos = db.consultar('''
        SELECT c.id, c.titulo, n.codigo, 
               (SELECT COUNT(*) FROM lecciones WHERE curso_id = c.id) as total_lecciones
        FROM cursos c
        LEFT JOIN niveles n ON c.nivel_id = n.id
        WHERE c.activo = 1
    ''')
    
    if not cursos:
        print("❌ No hay cursos disponibles")
        return
    
    for c in cursos:
        nivel = c['codigo'] or 'Sin nivel'
        print(f"  {c['id']}. {c['titulo']} ({nivel}) - {c['total_lecciones']} lecciones")

def ver_progreso(usuario_id):
    """Ver progreso del usuario"""
    print("\n📊 MI PROGRESO")
    print("=" * 50)
    
    # Estadísticas generales
    stats = db.consultar_uno('''
        SELECT 
            COUNT(DISTINCT curso_id) as cursos_iniciados,
            SUM(CASE WHEN completado = 1 THEN 1 ELSE 0 END) as lecciones_completadas,
            SUM(puntaje) as puntos_totales
        FROM progreso
        WHERE usuario_id = ?
    ''', [usuario_id])
    
    if stats:
        print(f"📚 Cursos iniciados: {stats[0] or 0}")
        print(f"📖 Lecciones completadas: {stats[1] or 0}")
        print(f"🏆 Puntos totales: {stats[2] or 0}")
    
    # Progreso por curso
    progreso_cursos = db.consultar('''
        SELECT 
            c.titulo,
            COUNT(DISTINCT p.id) as completadas,
            (SELECT COUNT(*) FROM lecciones WHERE curso_id = c.id) as total_lecciones
        FROM progreso p
        JOIN cursos c ON p.curso_id = c.id
        WHERE p.usuario_id = ?
        GROUP BY c.id
    ''', [usuario_id])
    
    if progreso_cursos:
        print("\n📋 DETALLE POR CURSO:")
        for pc in progreso_cursos:
            total = pc['total_lecciones'] or 1
            porcentaje = pc['completadas'] * 100 // total
            barra = '█' * (porcentaje // 10) + '░' * (10 - porcentaje // 10)
            print(f"  {pc['titulo'][:30]:<30} {barra} {porcentaje}%")

def main():
    limpiar_pantalla()
    
    print("=" * 50)
    print("  🐍 LMS EDUCATIVO - VERSIÓN SQL")
    print("=" * 50)
    
    # Login
    print("\n🔑 INICIAR SESIÓN")
    username = input("Usuario: ").strip()
    
    user = db.consultar_uno(
        'SELECT id, username, rol FROM usuarios WHERE username = ? AND activo = 1',
        [username]
    )
    
    if not user:
        print(f"❌ Usuario '{username}' no encontrado")
        return
    
    usuario_id = user['id']
    print(f"\n✅ ¡Bienvenido, {user['username']}!")
    
    while True:
        print("\n" + "=" * 50)
        print(f"  📚 MENÚ PRINCIPAL - {user['username']}")
        print("=" * 50)
        print("1. 📚 Ver cursos")
        print("2. 📊 Ver mi progreso")
        print("3. 🏛️ Entrenador de Latín")
        print("4. 🇬🇧 Entrenador de Inglés
       5. 📖 Gramática Española (RAE)")
        print("6. 🎮 Juegos de Texto
       7. 📚 Vocabulario (ES/EN/LA)")
        print("0. ❌ Salir")
        print("-" * 50)
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            ver_cursos()
        elif opcion == '2':
            ver_progreso(usuario_id)
        elif opcion == '3':
            os.system(f'python3 adaptados/latin_declinaciones_sql.py')
        elif opcion == '4':
            os.system(f'python3 adaptados/ingles_tutor_sql.py')
        elif opcion == '5':
            os.system(f'python3 adaptados/gramatica_rae_sql.py')
        
            os.system(f'python3 adaptados/juegos_texto_sql.py')
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        if opcion != '0':
            input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    main()
