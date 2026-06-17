#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JUEGOS DE TEXTO - Versión SQL
Adaptado para usar la base de datos central
Autor: @Hernank10
"""

import random
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class JuegoTextoSql:
    """Juegos de texto interactivos con SQL"""
    
    def __init__(self):
        self.usuario_id = None
        self._verificar_tablas()
    
    def _verificar_tablas(self):
        """Verificar que las tablas existen"""
        try:
            db.consultar("SELECT 1 FROM juegos_texto LIMIT 1")
        except:
            print("⚠️ Tabla 'juegos_texto' no encontrada. Creando juegos de ejemplo...")
            self._crear_juegos_ejemplo()
    
    def _crear_juegos_ejemplo(self):
        """Crear juegos de ejemplo"""
        # Aventura en el Espacio
        juego_id = db.ejecutar('''
        INSERT INTO juegos_texto (titulo, descripcion, escenario_inicial, puntos)
        VALUES (?, ?, ?, ?)
        ''', ('🚀 Aventura en el Espacio', 
              'Explora el espacio exterior y toma decisiones cruciales.', 
              'Estás en una nave espacial. Tu misión es explorar el sistema solar.', 
              20))
        
        decisiones = [
            (juego_id, 'Encuentras un planeta desconocido. ¿Qué haces?',
             'Aterrizar para explorar', 'Seguir viajando',
             'Aterrizas y encuentras vida inteligente. ¡Ganas 15 puntos! 🌟',
             'Sigues viajando y encuentras un agujero negro. ¡Cuidado! ⚠️'),
            (juego_id, 'Tu nave tiene un fallo técnico. ¿Qué haces?',
             'Intentar repararlo', 'Pedir ayuda por radio',
             'Logras repararlo a tiempo. ¡Bien hecho! 🔧',
             'Recibes ayuda de una nave amiga. ¡Salvado! 🆘'),
            (juego_id, 'Encuentras un asteroide con minerales valiosos. ¿Qué haces?',
             'Extraer minerales', 'Seguir explorando',
             'Obtienes minerales valiosos. ¡+10 puntos! 💎',
             'Continúas y encuentras un planeta habitable. 🌍'),
        ]
        
        for d in decisiones:
            db.ejecutar('''
            INSERT INTO decisiones_juego (juego_id, texto, opcion_a, opcion_b, resultado_a, resultado_b)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', d)
        
        # Aventura en la Ciudad
        juego_id2 = db.ejecutar('''
        INSERT INTO juegos_texto (titulo, descripcion, escenario_inicial, puntos)
        VALUES (?, ?, ?, ?)
        ''', ('🏙️ Ciudad Salvaje', 
              'Aventura en una ciudad peligrosa llena de misterios.', 
              'Estás en la calle principal de una ciudad desconocida.', 
              15))
        
        decisiones2 = [
            (juego_id2, 'Ves un callejón oscuro y una calle iluminada. ¿Qué eliges?',
             'Callejón oscuro', 'Calle iluminada',
             'Encuentras un tesoro escondido. ¡+15 puntos! 💰',
             'Llegas a un mercado lleno de vida. ¡+5 puntos! 🎪'),
            (juego_id2, 'Escuchas un ruido extraño. ¿Qué haces?',
             'Investigarlo', 'Ignorarlo y seguir caminando',
             'Encuentras a alguien que necesita ayuda. ¡+10 puntos! 🤝',
             'Te pierdes y pierdes tiempo. ⏰'),
            (juego_id2, 'Ves a un personaje sospechoso. ¿Qué haces?',
             'Seguirlo', 'Alejarte',
             'Descubres una conspiración. ¡+20 puntos! 🕵️',
             'Te escapas a tiempo. 😅'),
        ]
        
        for d in decisiones2:
            db.ejecutar('''
            INSERT INTO decisiones_juego (juego_id, texto, opcion_a, opcion_b, resultado_a, resultado_b)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', d)
        
        # Aventura Medieval
        juego_id3 = db.ejecutar('''
        INSERT INTO juegos_texto (titulo, descripcion, escenario_inicial, puntos)
        VALUES (?, ?, ?, ?)
        ''', ('🏰 Aventura Medieval', 
              'Vive una aventura en la época de caballeros y castillos.', 
              'Eres un caballero en el reino de Arturia.', 
              25))
        
        decisiones3 = [
            (juego_id3, 'El rey te pide una misión. ¿Qué eliges?',
             'Rescatar a la princesa', 'Derrotar al dragón',
             'Rescatas a la princesa. ¡+20 puntos! 👑',
             'Derrotas al dragón. ¡+25 puntos! 🐉'),
            (juego_id3, 'Encuentras un objeto misterioso. ¿Qué haces?',
             'Tomarlo', 'Dejarlo',
             'Es una espada mágica. ¡+15 puntos! ⚔️',
             'Era un objeto maldito. ¡Te salvaste! 🧙'),
        ]
        
        for d in decisiones3:
            db.ejecutar('''
            INSERT INTO decisiones_juego (juego_id, texto, opcion_a, opcion_b, resultado_a, resultado_b)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', d)
        
        print("✅ Juegos de texto creados con éxito")
    
    def set_usuario(self, username):
        """Establecer usuario actual"""
        user = db.consultar_uno(
            'SELECT id FROM usuarios WHERE username = ? AND activo = 1',
            [username]
        )
        if user:
            self.usuario_id = user[0]
            return True
        print(f"❌ Usuario '{username}' no encontrado")
        return False
    
    def listar_juegos(self):
        """Listar juegos disponibles"""
        juegos = db.consultar('SELECT id, titulo, descripcion, puntos FROM juegos_texto')
        
        if not juegos:
            print("❌ No hay juegos disponibles")
            return []
        
        print("\n🎮 JUEGOS DISPONIBLES:")
        print("-" * 50)
        for j in juegos:
            # Contar decisiones del juego
            decisiones_count = db.consultar_uno(
                'SELECT COUNT(*) FROM decisiones_juego WHERE juego_id = ?', 
                [j['id']]
            )[0]
            print(f"  {j['id']}. {j['titulo']}")
            print(f"     📖 {j['descripcion']}")
            print(f"     🎯 Puntos base: {j['puntos']} | 📝 {decisiones_count} decisiones")
            print()
        
        return juegos
    
    def jugar(self, juego_id=None):
        """Iniciar un juego"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        if not juego_id:
            self.listar_juegos()
            try:
                juego_id = int(input("\nElige un juego (número): ").strip())
            except:
                print("❌ Opción no válida")
                return
        
        # Verificar que el juego existe
        juego = db.consultar_uno('SELECT * FROM juegos_texto WHERE id = ?', [juego_id])
        if not juego:
            print("❌ Juego no encontrado")
            return
        
        # Obtener decisiones
        decisiones = db.consultar(
            'SELECT * FROM decisiones_juego WHERE juego_id = ? ORDER BY id',
            [juego_id]
        )
        
        if not decisiones:
            print("❌ Este juego no tiene decisiones.")
            return
        
        print("\n" + "=" * 60)
        print(f"  🎮 {juego['titulo']}")
        print("=" * 60)
        print(f"\n📖 {juego['escenario_inicial']}")
        print(f"🎯 Puntos base: {juego['puntos']}\n")
        
        puntaje_total = juego['puntos'] or 0
        
        for i, dec in enumerate(decisiones, 1):
            print(f"\n🔀 Decisión {i}: {dec['texto']}")
            print(f"   [A] {dec['opcion_a']}")
            print(f"   [B] {dec['opcion_b']}")
            
            opcion = input("Elige (A/B): ").strip().upper()
            
            if opcion == 'A':
                resultado = dec['resultado_a']
                puntaje_total += 5
            elif opcion == 'B':
                resultado = dec['resultado_b']
                puntaje_total += 10
            else:
                print("❌ Opción no válida. Saltando...")
                continue
            
            print(f"\n📌 {resultado}")
            time.sleep(1)
        
        # Resumen final
        print("\n" + "=" * 60)
        print("🏆 FIN DEL JUEGO")
        print("=" * 60)
        print(f"\n📊 Puntaje final: {puntaje_total} puntos")
        
        # Calcular valoración
        if puntaje_total >= 50:
            print("🌟 ¡Excelente aventura! Eres un verdadero explorador.")
        elif puntaje_total >= 30:
            print("👍 Buen trabajo. Sigue practicando.")
        else:
            print("📚 ¡Inténtalo de nuevo!")
        
        # Guardar puntaje
        db.ejecutar('''
        INSERT INTO puntajes_juego (juego_id, usuario_id, puntaje)
        VALUES (?, ?, ?)
        ''', [juego_id, self.usuario_id, puntaje_total])
        
        # Actualizar progreso general
        db.ejecutar('''
        INSERT OR REPLACE INTO progreso (usuario_id, curso_id, leccion_id, completado, puntaje)
        VALUES (?, 0, ?, ?, ?)
        ''', [self.usuario_id, juego_id, 1, puntaje_total])
    
    def ver_puntajes(self):
        """Ver puntajes de juegos"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        puntajes = db.consultar('''
            SELECT 
                j.titulo,
                p.puntaje,
                p.fecha
            FROM puntajes_juego p
            JOIN juegos_texto j ON p.juego_id = j.id
            WHERE p.usuario_id = ?
            ORDER BY p.fecha DESC
        ''', [self.usuario_id])
        
        if not puntajes:
            print("📊 No hay puntajes aún. ¡Juega a algún juego!")
            return
        
        print("\n📊 MIS PUNTAJES")
        print("=" * 50)
        print(f"{'Juego':<30} {'Puntaje':<10} {'Fecha':<15}")
        print("-" * 50)
        for p in puntajes:
            fecha = p['fecha'][:10] if p['fecha'] else 'N/A'
            print(f"{p['titulo']:<30} {p['puntaje']:<10} {fecha:<15}")
    
    def ranking(self):
        """Ver ranking de jugadores"""
        ranking = db.consultar('''
            SELECT 
                u.username,
                SUM(p.puntaje) as total_puntos,
                COUNT(p.id) as partidas
            FROM puntajes_juego p
            JOIN usuarios u ON p.usuario_id = u.id
            WHERE u.activo = 1
            GROUP BY u.id
            ORDER BY total_puntos DESC
            LIMIT 10
        ''')
        
        if not ranking:
            print("📊 No hay datos de ranking aún.")
            return
        
        print("\n🏆 RANKING DE JUGADORES")
        print("=" * 50)
        print(f"{'#':<4} {'Jugador':<20} {'Puntos':<10} {'Partidas':<10}")
        print("-" * 50)
        
        for i, r in enumerate(ranking, 1):
            medalla = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"{medalla:<4} {r['username']:<20} {r['total_puntos']:<10} {r['partidas']:<10}")
    
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
    juego = JuegoTextoSql()
    
    print("\n🔑 INICIAR SESIÓN")
    if not juego._menu_usuario():
        return
    
    print(f"✅ Bienvenido!")
    
    while True:
        print("\n" + "=" * 40)
        print("  🎮 JUEGOS DE TEXTO")
        print("=" * 40)
        print("1. Jugar")
        print("2. Ver mis puntajes")
        print("3. Ver ranking")
        print("4. Cambiar usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            juego.jugar()
        elif opcion == '2':
            juego.ver_puntajes()
        elif opcion == '3':
            juego.ranking()
        elif opcion == '4':
            juego._menu_usuario()
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")

if __name__ == '__main__':
    main()
