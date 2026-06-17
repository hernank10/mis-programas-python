#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRENADOR DE GRAMÁTICA ESPAÑOLA - Versión SQL
Basado en las normas de la RAE
Adaptado para usar la base de datos central
Autor: @Hernank10
"""

import random
import sys
import os
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class GramaticaRAESQL:
    """Entrenador interactivo de gramática española con SQL"""
    
    def __init__(self):
        self.usuario_id = None
        self._verificar_tablas()
    
    def _verificar_tablas(self):
        """Verificar que las tablas existen"""
        try:
            db.consultar("SELECT 1 FROM ejercicios_gramatica LIMIT 1")
        except:
            print("⚠️ Tabla 'ejercicios_gramatica' no encontrada. Creando ejercicios...")
            self._crear_ejercicios()
        
        try:
            db.consultar("SELECT 1 FROM reglas_rae LIMIT 1")
        except:
            print("⚠️ Tabla 'reglas_rae' no encontrada. Creando reglas...")
            self._crear_reglas()
    
    def _crear_reglas(self):
        """Crear reglas gramaticales de la RAE"""
        reglas = [
            # Reglas de acentuación
            ('Acentuación de agudas', 'Llevan tilde las palabras agudas terminadas en vocal, -n o -s.', 'Ejemplo: "canción", "está", "comerás".', 1),
            ('Acentuación de graves', 'Llevan tilde las palabras graves que NO terminan en vocal, -n o -s.', 'Ejemplo: "árbol", "cárcel", "débil".', 1),
            ('Acentuación de esdrújulas', 'Todas las palabras esdrújulas llevan tilde.', 'Ejemplo: "pájaro", "cántaro", "teléfono".', 1),
            ('Acentuación de sobresdrújulas', 'Todas las palabras sobresdrújulas llevan tilde.', 'Ejemplo: "dígamelo", "cómetelo".', 2),
            
            # Uso de B y V
            ('Uso de la B', 'Se escribe B después de las sílabas "bu", "bur", "bus", y antes de "l" o "r".', 'Ejemplo: "burro", "blando", "abrigo".', 1),
            ('Uso de la V', 'Se escribe V después de las sílabas "an", "en", "in", "on", "un".', 'Ejemplo: "envase", "investigar".', 1),
            
            # Uso de G y J
            ('Uso de la G', 'Se escribe G antes de "e" e "i" en verbos terminados en -ger, -gir.', 'Ejemplo: "coger", "recoger", "corregir".', 2),
            ('Uso de la J', 'Se escribe J en verbos terminados en -jar, -jer, -jir.', 'Ejemplo: "trabajar", "tejer", "crujir".', 2),
            
            # Uso de la H
            ('Uso de la H', 'Se escribe H en palabras que comienzan por "hi", "hu" seguidos de vocal.', 'Ejemplo: "hielo", "hueso", "huevo".', 1),
            
            # Dequeísmo y queísmo
            ('Dequeísmo', 'Se usa "de que" cuando la preposición "de" es requerida por el verbo.', 'Ejemplo: "Me alegro de que vengas" (correcto).', 2),
            ('Queísmo', 'Es incorrecto omitir la preposición "de" cuando es requerida.', 'Ejemplo: "Me alegro que vengas" (incorrecto).', 2),
            
            # Conectores
            ('Uso de "porque"', 'Porque: causa o razón (junto, sin tilde).', 'Ejemplo: "No fui porque estaba enfermo."', 1),
            ('Uso de "por qué"', 'Por qué: interrogativo (separado, con tilde).', 'Ejemplo: "¿Por qué no viniste?"', 1),
            ('Uso de "porqué"', 'Porqué: sustantivo (sin tilde).', 'Ejemplo: "No entiendo el porqué."', 2),
            ('Uso de "por que"', 'Por que: preposición "por" + conjunción "que".', 'Ejemplo: "Luchó por que lo escucharan."', 2),
        ]
        
        for r in reglas:
            db.ejecutar('''
            INSERT OR IGNORE INTO reglas_rae (categoria, descripcion, ejemplo, nivel)
            VALUES (?, ?, ?, ?)
            ''', r)
        
        print(f"✅ Creadas {len(reglas)} reglas de la RAE")
    
    def _crear_ejercicios(self):
        """Crear ejercicios de gramática"""
        ejercicios = [
            # Acentuación
            ('acentuacion', '¿Cuál de estas palabras es esdrújula?', 'pájaro', 'pajaro|pájaro|pajáro|pájaró', 'Las esdrújulas siempre llevan tilde.', 1),
            ('acentuacion', '¿Cuál de estas palabras es aguda con tilde?', 'canción', 'cancion|canción|cáncion|cancíon', 'Las agudas terminadas en -n llevan tilde.', 1),
            ('acentuacion', '¿Cuál de estas palabras es grave sin tilde?', 'casa', 'casa|cása|casá|casà', 'Las graves terminadas en vocal no llevan tilde.', 1),
            
            # B vs V
            ('byv', 'Completa: "El ____ero" (que mueve objetos pesados)', 'buey', 'buey|vuey|buej|vuej', 'Se escribe B después de "bu".', 1),
            ('byv', 'Completa: "____estir"', 'vestir', 'bestir|vestir|bvestir|vbestir', 'Se escribe V después de "es".', 1),
            
            # G vs J
            ('gyj', 'Completa: "____irar" (persona que vigila)', 'vigilar', 'gigilar|vigilar|jigilar|vigelar', 'Se escribe G delante de "i".', 2),
            ('gyj', 'Completa: "____erar" (trabajar en el campo)', 'labrar', 'labrar|gabrar|jabrar|labrarr', 'Se escribe B en esta palabra.', 2),
            
            # Dequeísmo / Queísmo
            ('dequeismo', 'Completa: "Me alegro ____ vengas"', 'de que', 'de que|que|en que|con que', 'El verbo "alegrarse" requiere la preposición "de".', 2),
            ('dequeismo', 'Completa: "Espero ____ venga"', 'que', 'de que|que|a que|con que', 'El verbo "esperar" no requiere preposición.', 2),
            
            # Porque / Por qué / Porqué / Por que
            ('porque', 'Completa: "No sé ____ no vino"', 'por qué', 'porque|por qué|porqué|por que', 'Pregunta indirecta, lleva tilde y separado.', 1),
            ('porque', 'Completa: "____ llegaste tarde, no entraste"', 'porque', 'porque|por qué|porqué|por que', 'Causa, junto y sin tilde.', 1),
            ('porque', 'Completa: "No entiendo el ____"', 'porqué', 'porque|por qué|porqué|por que', 'Sustantivo, lleva tilde.', 2),
            ('porque', 'Completa: "Luchó ____ lo lograran"', 'por que', 'porque|por qué|porqué|por que', 'Preposición "por" + conjunción "que"', 2),
            
            # Ortografía general
            ('ortografia', '¿Cuál es la forma correcta?', 'había', 'había|havía|abía|havia', 'El verbo haber se escribe con H.', 1),
            ('ortografia', '¿Cuál es la forma correcta?', 'hay', 'hay|ai|ay|hai', 'Del verbo haber.', 1),
            
            # Sintaxis
            ('sintaxis', 'Identifica el sujeto: "El perro ladra"', 'El perro', 'El perro|perro|ladra|El', 'El sujeto es quien realiza la acción.', 1),
            ('sintaxis', 'Identifica el predicado: "María estudia en la biblioteca"', 'estudia en la biblioteca', 'estudia|estudia en la biblioteca|María|biblioteca', 'El predicado es lo que se dice del sujeto.', 1),
            ('sintaxis', 'Completa: "A Juan le gusta el fútbol" - ¿qué tipo de oración es?', 'impersonal', 'personal|impersonal|pasiva|activa', 'No tiene sujeto gramatical.', 2),
        ]
        
        for e in ejercicios:
            db.ejecutar('''
            INSERT OR IGNORE INTO ejercicios_gramatica 
            (categoria, pregunta, respuesta_correcta, opciones, explicacion, nivel)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', e)
        
        print(f"✅ Creados {len(ejercicios)} ejercicios de gramática")
    
    def set_usuario(self, username):
        """Establecer usuario actual"""
        user = db.consultar_uno(
            'SELECT id FROM usuarios WHERE username = ? AND activo = 1',
            [username]
        )
        if user:
            self.usuario_id = user[0]
            return True
        return False
    
    def ver_categorias(self):
        """Ver categorías disponibles"""
        categorias = db.consultar('''
            SELECT DISTINCT categoria, COUNT(*) as total 
            FROM ejercicios_gramatica 
            GROUP BY categoria
        ''')
        
        print("\n📚 CATEGORÍAS DE GRAMÁTICA:")
        print("-" * 40)
        for c in categorias:
            print(f"  • {c['categoria']}: {c['total']} ejercicios")
    
    def ver_reglas(self, categoria=None):
        """Ver reglas de la RAE"""
        sql = 'SELECT * FROM reglas_rae'
        params = []
        
        if categoria and categoria != 'todas':
            sql += ' WHERE categoria = ?'
            params.append(categoria)
        
        sql += ' ORDER BY nivel'
        
        reglas = db.consultar(sql, params)
        
        if not reglas:
            print("❌ No hay reglas disponibles")
            return
        
        print("\n📖 REGLAS DE LA RAE")
        print("=" * 60)
        
        for r in reglas:
            print(f"\n📌 {r['categoria']}")
            print(f"   {r['descripcion']}")
            print(f"   📝 {r['ejemplo']}")
            print(f"   Nivel: {'⭐' * r['nivel']}")
            print("-" * 40)
    
    def practicar(self, categoria=None, num_preguntas=10):
        """Practicar ejercicios de gramática"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        sql = 'SELECT * FROM ejercicios_gramatica'
        params = []
        
        if categoria and categoria != 'todas':
            sql += ' WHERE categoria = ?'
            params.append(categoria)
        
        sql += ' ORDER BY RANDOM() LIMIT ?'
        params.append(num_preguntas)
        
        ejercicios = db.consultar(sql, params)
        
        if not ejercicios:
            print("❌ No hay ejercicios disponibles")
            return
        
        aciertos = 0
        total = len(ejercicios)
        
        print("\n" + "=" * 60)
        print(f"  📝 PRACTICANDO GRAMÁTICA ({total} ejercicios)")
        if categoria and categoria != 'todas':
            print(f"  Categoría: {categoria}")
        print("=" * 60)
        print("  Escribe 'salir' para terminar\n")
        
        for i, e in enumerate(ejercicios, 1):
            print(f"\n{i}/{total} - {e['pregunta']}")
            
            # Mostrar opciones si existen
            if e['opciones']:
                opciones = e['opciones'].split('|')
                random.shuffle(opciones)
                for j, opt in enumerate(opciones, 1):
                    print(f"  {j}. {opt}")
                
                try:
                    respuesta = input("\nElige una opción (número o texto): ").strip()
                    if respuesta.isdigit():
                        idx = int(respuesta) - 1
                        if 0 <= idx < len(opciones):
                            respuesta = opciones[idx]
                except:
                    respuesta = input("Tu respuesta: ").strip()
            else:
                respuesta = input("Tu respuesta: ").strip()
            
            if respuesta.lower() == 'salir':
                break
            
            if respuesta.lower() == e['respuesta_correcta'].lower():
                print("✅ ¡Correcto! 🎉")
                aciertos += 1
                self._guardar_progreso(e['id'], True)
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {e['respuesta_correcta']}")
                self._guardar_progreso(e['id'], False)
            
            if e['explicacion']:
                print(f"💡 {e['explicacion']}")
        
        if total > 0:
            porcentaje = aciertos * 100 // total
            print("\n" + "=" * 60)
            print(f"📊 Resultado: {aciertos}/{total} correctas ({porcentaje}%)")
            
            if porcentaje >= 80:
                print("🏆 ¡Excelente! Dominas la gramática.")
            elif porcentaje >= 60:
                print("👍 Buen trabajo. Sigue practicando.")
            else:
                print("📚 Consulta las reglas de la RAE y vuelve a intentarlo.")
    
    def _guardar_progreso(self, ejercicio_id, acertado):
        """Guardar progreso en la base de datos"""
        if not self.usuario_id:
            return
        
        progreso = db.consultar_uno(
            'SELECT id, aciertos, intentos FROM progreso_gramatica WHERE usuario_id = ? AND ejercicio_id = ?',
            [self.usuario_id, ejercicio_id]
        )
        
        if progreso:
            aciertos = progreso[1] + (1 if acertado else 0)
            intentos = progreso[2] + 1
            db.ejecutar(
                'UPDATE progreso_gramatica SET aciertos = ?, intentos = ? WHERE id = ?',
                [aciertos, intentos, progreso[0]]
            )
        else:
            db.ejecutar('''
            INSERT INTO progreso_gramatica (usuario_id, ejercicio_id, aciertos, intentos)
            VALUES (?, ?, ?, ?)
            ''', [self.usuario_id, ejercicio_id, 1 if acertado else 0, 1])
    
    def ver_progreso(self):
        """Ver progreso del usuario"""
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
            FROM progreso_gramatica p
            JOIN ejercicios_gramatica e ON p.ejercicio_id = e.id
            WHERE p.usuario_id = ?
            ORDER BY porcentaje DESC
        ''', [self.usuario_id])
        
        if not resultados:
            print("📊 No hay datos de progreso aún.")
            return
        
        print("\n📊 PROGRESO EN GRAMÁTICA")
        print("=" * 60)
        print(f"{'Categoría':<15} {'Pregunta':<25} {'Aciertos':<10} {'%':<8}")
        print("-" * 60)
        
        for r in resultados:
            pregunta_corta = r['pregunta'][:25] + '...' if len(r['pregunta']) > 25 else r['pregunta']
            print(f"{r['categoria']:<15} {pregunta_corta:<25} {r['aciertos']}/{r['intentos']:<7} {r['porcentaje']:<8}%")
    
    def _menu_usuario(self):
        """Menú de usuario"""
        print("\n👤 SELECCIÓN DE USUARIO")
        print("=" * 40)
        usuarios = db.consultar('SELECT username, rol FROM usuarios WHERE activo = 1')
        print("\n📋 Usuarios disponibles:")
        for u in usuarios:
            print(f"  • {u['username']} ({u['rol']})")
        
        print("\n1. Usar usuario existente")
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
    tutor = GramaticaRAESQL()
    
    print("\n🔑 INICIAR SESIÓN")
    if not tutor._menu_usuario():
        return
    
    print(f"✅ Bienvenido!")
    
    while True:
        print("\n" + "=" * 40)
        print("  📖 GRAMÁTICA ESPAÑOLA (RAE)")
        print("=" * 40)
        print("1. Practicar ejercicios")
        print("2. Ver reglas de la RAE")
        print("3. Ver categorías")
        print("4. Ver mi progreso")
        print("5. Cambiar usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            tutor.ver_categorias()
            categoria = input("\nElige categoría (o 'todas'): ").strip()
            num = input("Número de preguntas (Enter para 10): ").strip()
            try:
                num_preguntas = int(num) if num else 10
            except:
                num_preguntas = 10
            tutor.practicar(categoria if categoria else None, num_preguntas)
        elif opcion == '2':
            tutor.ver_categorias()
            categoria = input("\nElige categoría (o 'todas'): ").strip()
            tutor.ver_reglas(categoria if categoria else None)
        elif opcion == '3':
            tutor.ver_categorias()
        elif opcion == '4':
            tutor.ver_progreso()
        elif opcion == '5':
            tutor._menu_usuario()
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")

if __name__ == '__main__':
    main()
