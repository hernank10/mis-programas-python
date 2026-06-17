#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ENTRENADOR DE VOCABULARIO - Versión SQL
Aprende vocabulario en español, inglés y latín con la misma base de datos
Autor: @Hernank10
"""

import random
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

class VocabularioSQL:
    """Entrenador interactivo de vocabulario multilingüe con SQL"""
    
    def __init__(self):
        self.usuario_id = None
        self.idioma_actual = 'espanol'
        self._verificar_tablas()
    
    def _verificar_tablas(self):
        """Verificar que las tablas existen"""
        try:
            db.consultar("SELECT 1 FROM vocabulario LIMIT 1")
        except:
            print("⚠️ Tabla 'vocabulario' no encontrada. Creando vocabulario...")
            self._crear_vocabulario()
        
        try:
            db.consultar("SELECT 1 FROM progreso_vocabulario LIMIT 1")
        except:
            print("⚠️ Tabla 'progreso_vocabulario' no encontrada. Creando tabla de progreso...")
            self._crear_tabla_progreso()
    
    def _crear_tabla_progreso(self):
        """Crear tabla de progreso de vocabulario"""
        db.ejecutar('''
        CREATE TABLE IF NOT EXISTS progreso_vocabulario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            palabra_id INTEGER,
            aciertos INTEGER DEFAULT 0,
            intentos INTEGER DEFAULT 0,
            ultima_practica TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (palabra_id) REFERENCES vocabulario(id)
        )
        ''')
        print("✅ Tabla progreso_vocabulario creada")
    
    def _crear_vocabulario(self):
        """Crear vocabulario multilingüe"""
        palabras = [
            # Español - Inglés
            ('casa', 'house', 'espanol', 'Lugar donde se vive', 1),
            ('perro', 'dog', 'espanol', 'Animal doméstico', 1),
            ('gato', 'cat', 'espanol', 'Animal doméstico felino', 1),
            ('libro', 'book', 'espanol', 'Objeto para leer', 1),
            ('mesa', 'table', 'espanol', 'Mueble para comer', 1),
            ('silla', 'chair', 'espanol', 'Mueble para sentarse', 1),
            ('ventana', 'window', 'espanol', 'Abertura en la pared', 1),
            ('puerta', 'door', 'espanol', 'Acceso a un lugar', 1),
            ('amigo', 'friend', 'espanol', 'Persona cercana', 1),
            ('familia', 'family', 'espanol', 'Grupo de personas', 1),
            ('comida', 'food', 'espanol', 'Alimento', 1),
            ('agua', 'water', 'espanol', 'Líquido vital', 1),
            ('sol', 'sun', 'espanol', 'Estrella del sistema solar', 1),
            ('luna', 'moon', 'espanol', 'Satélite natural de la Tierra', 1),
            ('estrella', 'star', 'espanol', 'Cuerpo celeste', 1),
            ('feliz', 'happy', 'espanol', 'Estado de ánimo positivo', 2),
            ('triste', 'sad', 'espanol', 'Estado de ánimo negativo', 2),
            ('grande', 'big', 'espanol', 'De gran tamaño', 1),
            ('pequeño', 'small', 'espanol', 'De pequeño tamaño', 1),
            ('rápido', 'fast', 'espanol', 'Que se mueve con velocidad', 2),
            ('lento', 'slow', 'espanol', 'Que se mueve con poca velocidad', 2),
            ('fuerte', 'strong', 'espanol', 'Que tiene fuerza', 2),
            ('débil', 'weak', 'espanol', 'Que tiene poca fuerza', 2),
            ('inteligente', 'intelligent', 'espanol', 'Que tiene inteligencia', 2),
            ('bonito', 'beautiful', 'espanol', 'Que es agradable a la vista', 2),
            
            # Latín - Español
            ('rosa', 'rosa', 'latin', 'Flor', 1),
            ('puella', 'niña', 'latin', 'Niña pequeña', 1),
            ('servus', 'esclavo', 'latin', 'Persona sin libertad', 1),
            ('bellum', 'guerra', 'latin', 'Conflicto armado', 1),
            ('consul', 'cónsul', 'latin', 'Magistrado romano', 2),
            ('flumen', 'río', 'latin', 'Corriente de agua', 1),
            ('manus', 'mano', 'latin', 'Parte del cuerpo', 1),
            ('cornu', 'cuerno', 'latin', 'Apéndice óseo', 2),
            ('dies', 'día', 'latin', 'Período de 24 horas', 1),
            ('res', 'cosa', 'latin', 'Objeto', 1),
            ('magnus', 'grande', 'latin', 'De gran tamaño', 2),
            ('parvus', 'pequeño', 'latin', 'De pequeño tamaño', 2),
            ('pulcher', 'bonito', 'latin', 'Hermoso a la vista', 2),
            ('fortis', 'fuerte', 'latin', 'Que tiene fuerza', 2),
            ('sapiens', 'sabio', 'latin', 'Que tiene sabiduría', 2),
            
            # Inglés - Español (para práctica inversa)
            ('mother', 'madre', 'ingles', 'Parentesco femenino', 1),
            ('father', 'padre', 'ingles', 'Parentesco masculino', 1),
            ('brother', 'hermano', 'ingles', 'Hermano', 1),
            ('sister', 'hermana', 'ingles', 'Hermana', 1),
            ('apple', 'manzana', 'ingles', 'Fruta', 1),
            ('bread', 'pan', 'ingles', 'Alimento', 1),
            ('milk', 'leche', 'ingles', 'Líquido', 1),
            ('car', 'coche', 'ingles', 'Vehículo', 1),
            ('bus', 'autobús', 'ingles', 'Vehículo de transporte', 1),
            ('train', 'tren', 'ingles', 'Vehículo ferroviario', 1),
            ('happiness', 'felicidad', 'ingles', 'Estado de ánimo', 2),
            ('friendship', 'amistad', 'ingles', 'Relación entre amigos', 2),
            ('freedom', 'libertad', 'ingles', 'Estado de ser libre', 2),
            ('kindness', 'amabilidad', 'ingles', 'Cualidad de ser amable', 2),
            ('bravery', 'valentía', 'ingles', 'Cualidad de ser valiente', 2),
        ]
        
        for p in palabras:
            db.ejecutar('''
            INSERT OR IGNORE INTO vocabulario (palabra, traduccion, idioma, descripcion, nivel)
            VALUES (?, ?, ?, ?, ?)
            ''', p)
        
        print(f"✅ Creadas {len(palabras)} palabras de vocabulario")
    
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
    
    def ver_estadisticas(self):
        """Ver estadísticas de vocabulario"""
        print("\n📊 ESTADÍSTICAS DE VOCABULARIO")
        print("=" * 50)
        
        total = db.consultar_uno('SELECT COUNT(*) FROM vocabulario')[0]
        print(f"📚 Total de palabras: {total}")
        
        for idioma in ['espanol', 'ingles', 'latin']:
            count = db.consultar_uno(
                'SELECT COUNT(*) FROM vocabulario WHERE idioma = ?',
                [idioma]
            )[0]
            print(f"  • {idioma.capitalize()}: {count} palabras")
        
        # Niveles
        niveles = db.consultar('SELECT nivel, COUNT(*) FROM vocabulario GROUP BY nivel')
        print("\n📊 Por nivel:")
        for n in niveles:
            print(f"  • Nivel {n[0]}: {n[1]} palabras")
    
    def estudiar(self, idioma=None, nivel=None, num_palabras=10):
        """Estudiar vocabulario"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        sql = 'SELECT * FROM vocabulario WHERE 1=1'
        params = []
        
        if idioma and idioma != 'todos':
            sql += ' AND idioma = ?'
            params.append(idioma)
        
        if nivel:
            sql += ' AND nivel = ?'
            params.append(nivel)
        
        sql += ' ORDER BY RANDOM() LIMIT ?'
        params.append(num_palabras)
        
        palabras = db.consultar(sql, params)
        
        if not palabras:
            print("❌ No hay palabras disponibles con esos filtros")
            return
        
        print("\n" + "=" * 60)
        print(f"  📚 ESTUDIANDO VOCABULARIO ({len(palabras)} palabras)")
        print("=" * 60)
        print("  Escribe 'salir' para terminar\n")
        
        aciertos = 0
        
        for i, p in enumerate(palabras, 1):
            # Decidir dirección de la pregunta (50% cada una)
            if random.choice([True, False]):
                # De idioma base a traducción
                pregunta = f"Palabra: {p['palabra']} ({p['idioma']})"
                respuesta_correcta = p['traduccion']
                if p['idioma'] == 'espanol':
                    idioma_resp = 'español'
                elif p['idioma'] == 'ingles':
                    idioma_resp = 'inglés'
                else:
                    idioma_resp = 'español'  # latín a español
            else:
                # De traducción a idioma base
                pregunta = f"Traducción: {p['traduccion']}"
                respuesta_correcta = p['palabra']
                if p['idioma'] == 'espanol':
                    idioma_resp = 'español'
                else:
                    idioma_resp = p['idioma']
            
            print(f"\n{i}/{len(palabras)} - {pregunta}")
            if p['descripcion']:
                print(f"💡 Pista: {p['descripcion']}")
            
            respuesta = input(f"¿Cómo se dice en {idioma_resp}? ").strip()
            
            if respuesta.lower() == 'salir':
                break
            
            if respuesta.lower() == respuesta_correcta.lower():
                print("✅ ¡Correcto! 🎉")
                aciertos += 1
                self._guardar_progreso(p['id'], True)
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {respuesta_correcta}")
                self._guardar_progreso(p['id'], False)
        
        print("\n" + "=" * 60)
        print(f"📊 Resultado: {aciertos}/{len(palabras)} correctas")
        if len(palabras) > 0:
            porcentaje = aciertos * 100 // len(palabras)
            print(f"📈 Porcentaje: {porcentaje}%")
            
            if porcentaje >= 80:
                print("🏆 ¡Excelente! Sigue así.")
            elif porcentaje >= 60:
                print("👍 Buen trabajo. Sigue practicando.")
            else:
                print("📚 Repasa estas palabras.")
    
    def _guardar_progreso(self, palabra_id, acertado):
        """Guardar progreso en la base de datos"""
        if not self.usuario_id:
            return
        
        progreso = db.consultar_uno(
            'SELECT id, aciertos, intentos FROM progreso_vocabulario WHERE usuario_id = ? AND palabra_id = ?',
            [self.usuario_id, palabra_id]
        )
        
        if progreso:
            aciertos = progreso[1] + (1 if acertado else 0)
            intentos = progreso[2] + 1
            db.ejecutar(
                'UPDATE progreso_vocabulario SET aciertos = ?, intentos = ? WHERE id = ?',
                [aciertos, intentos, progreso[0]]
            )
        else:
            db.ejecutar('''
            INSERT INTO progreso_vocabulario (usuario_id, palabra_id, aciertos, intentos)
            VALUES (?, ?, ?, ?)
            ''', [self.usuario_id, palabra_id, 1 if acertado else 0, 1])
    
    def ver_progreso(self):
        """Ver progreso del usuario en vocabulario"""
        if not self.usuario_id:
            print("❌ Primero inicia sesión")
            return
        
        print("\n📊 MI PROGRESO EN VOCABULARIO")
        print("=" * 50)
        
        total_palabras = db.consultar_uno('SELECT COUNT(*) FROM vocabulario')[0]
        practicadas = db.consultar_uno(
            'SELECT COUNT(DISTINCT palabra_id) FROM progreso_vocabulario WHERE usuario_id = ?',
            [self.usuario_id]
        )[0]
        
        print(f"📚 Total de palabras: {total_palabras}")
        print(f"📖 Palabras practicadas: {practicadas}")
        
        if total_palabras > 0:
            porcentaje = practicadas * 100 // total_palabras
            print(f"📈 Progreso: {porcentaje}%")
        
        # Mejores palabras
        mejores = db.consultar('''
            SELECT 
                v.palabra,
                v.traduccion,
                v.idioma,
                p.aciertos,
                p.intentos,
                ROUND(p.aciertos * 100.0 / p.intentos, 1) as porcentaje
            FROM progreso_vocabulario p
            JOIN vocabulario v ON p.palabra_id = v.id
            WHERE p.usuario_id = ? AND p.intentos >= 2
            ORDER BY porcentaje DESC
            LIMIT 5
        ''', [self.usuario_id])
        
        if mejores:
            print("\n🏆 TUS MEJORES PALABRAS:")
            for m in mejores:
                print(f"  • {m['palabra']} ({m['idioma']}) -> {m['traduccion']}: {m['porcentaje']}%")
        
        # Palabras difíciles
        dificiles = db.consultar('''
            SELECT 
                v.palabra,
                v.traduccion,
                v.idioma,
                p.aciertos,
                p.intentos,
                ROUND(p.aciertos * 100.0 / p.intentos, 1) as porcentaje
            FROM progreso_vocabulario p
            JOIN vocabulario v ON p.palabra_id = v.id
            WHERE p.usuario_id = ? AND p.intentos >= 2
            ORDER BY porcentaje ASC
            LIMIT 5
        ''', [self.usuario_id])
        
        if dificiles:
            print("\n📚 PALABRAS PARA REPASAR:")
            for d in dificiles:
                print(f"  • {d['palabra']} ({d['idioma']}) -> {d['traduccion']}: {d['porcentaje']}%")
    
    def _menu_idioma(self):
        """Seleccionar idioma"""
        print("\n🌍 SELECCIONAR IDIOMA")
        print("=" * 40)
        print("1. Español")
        print("2. Inglés")
        print("3. Latín")
        print("4. Todos los idiomas")
        print("0. Volver")
        
        opcion = input("\nElige un idioma: ").strip()
        
        if opcion == '0':
            return None
        elif opcion == '1':
            return 'espanol'
        elif opcion == '2':
            return 'ingles'
        elif opcion == '3':
            return 'latin'
        elif opcion == '4':
            return 'todos'
        else:
            print("❌ Opción no válida")
            return self._menu_idioma()
    
    def _menu_nivel(self):
        """Seleccionar nivel"""
        print("\n📊 SELECCIONAR NIVEL")
        print("=" * 40)
        print("1. Principiante (Nivel 1)")
        print("2. Intermedio (Nivel 2)")
        print("3. Avanzado (Nivel 3)")
        print("4. Todos los niveles")
        print("0. Volver")
        
        opcion = input("\nElige un nivel: ").strip()
        
        if opcion == '0':
            return None
        elif opcion == '1':
            return 1
        elif opcion == '2':
            return 2
        elif opcion == '3':
            return 3
        elif opcion == '4':
            return None
        else:
            print("❌ Opción no válida")
            return self._menu_nivel()
    
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
    tutor = VocabularioSQL()
    
    print("\n🔑 INICIAR SESIÓN")
    if not tutor._menu_usuario():
        return
    
    print(f"✅ Bienvenido!")
    
    while True:
        print("\n" + "=" * 40)
        print("  📚 ENTRENADOR DE VOCABULARIO")
        print("=" * 40)
        print("1. Estudiar vocabulario")
        print("2. Ver estadísticas")
        print("3. Ver mi progreso")
        print("4. Cambiar idioma/nivel")
        print("5. Cambiar usuario")
        print("0. Salir")
        
        opcion = input("\nElige: ").strip()
        
        if opcion == '1':
            idioma = tutor._menu_idioma()
            if idioma is None:
                continue
            nivel = tutor._menu_nivel()
            if nivel is None:
                continue
            num = input("Número de palabras (Enter para 10): ").strip()
            try:
                num_palabras = int(num) if num else 10
            except:
                num_palabras = 10
            tutor.estudiar(idioma, nivel, num_palabras)
        elif opcion == '2':
            tutor.ver_estadisticas()
        elif opcion == '3':
            tutor.ver_progreso()
        elif opcion == '4':
            pass  # Ya se selecciona en la opción 1
        elif opcion == '5':
            tutor._menu_usuario()
        elif opcion == '0':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    main()
