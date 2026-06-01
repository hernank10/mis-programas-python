import json
import os
import datetime
import random
from datetime import datetime, timedelta
import sys

class SistemaGramaticaEspanola:
    def __init__(self):
        self.usuario_actual = None
        self.archivo_usuarios = "usuarios.json"
        self.archivo_progreso = "progreso.json"
        self.lecciones = self.cargar_lecciones()
        self.usuarios = self.cargar_usuarios()
        self.progreso = self.cargar_progreso()
        
    def cargar_lecciones(self):
        """Carga las lecciones de gramática española"""
        return {
            "lecciones": [
                {
                    "id": 1,
                    "titulo": "Artículos definidos e indefinidos",
                    "contenido": """
📚 ARTÍCULOS DEFINIDOS E INDEFINIDOS

🎯 **Artículos definidos** (el, la, los, las):
- Se usan para referirse a algo específico o conocido
- Ejemplo: "El libro" (un libro específico), "La casa" (una casa específica)

🎯 **Artículos indefinidos** (un, una, unos, unas):
- Se usan para referirse a algo no específico o desconocido
- Ejemplo: "Un libro" (cualquier libro), "Una casa" (cualquier casa)

📹 **Video recomendado**: https://www.youtube.com/watch?v=nr6h7b4Mtxo (¡O busca "artículos español" en YouTube!)
                    """,
                    "ejercicios": [
                        {
                            "id": 1,
                            "tipo": "mcq",
                            "enunciado": "¿___ casa es muy bonita? (refiriéndose a una casa específica)",
                            "opciones": ["Un", "Una", "La", "El"],
                            "respuesta_correcta": "La",
                            "pistas": ["Es femenino singular", "Es algo específico"]
                        },
                        {
                            "id": 2,
                            "tipo": "write",
                            "enunciado": "Completa: Necesito comprar ___ libro para la escuela.",
                            "respuesta_correcta": "un",
                            "pistas": ["No es específico", "Libro es masculino"]
                        },
                        {
                            "id": 3,
                            "tipo": "mcq",
                            "enunciado": "¿___ perros están jugando en el parque? (varios perros específicos)",
                            "opciones": ["Unos", "Los", "Las", "El"],
                            "respuesta_correcta": "Los",
                            "pistas": ["Perros es masculino plural", "Son perros específicos"]
                        }
                    ]
                },
                {
                    "id": 2,
                    "titulo": "Sustantivos: género y número",
                    "contenido": """
📚 GÉNERO Y NÚMERO DE SUSTANTIVOS

🎯 **Género**:
- Masculino: generalmente terminan en -o (libro, perro)
- Femenino: generalmente terminan en -a (casa, mesa)
- Excepciones: día (masc.), mano (fem.)

🎯 **Número**:
- Singular: un elemento (libro, casa)
- Plural: varios elementos (+s, +es)
- Ejemplos: libro → libros, papel → papeles

📹 **Video recomendado**: https://www.youtube.com/watch?v=zC7gL1VK5Po
                    """,
                    "ejercicios": [
                        {
                            "id": 1,
                            "tipo": "write",
                            "enunciado": "Escribe el plural de 'flor': _____",
                            "respuesta_correcta": "flores",
                            "pistas": ["Termina en consonante", "Agrega -es"]
                        },
                        {
                            "id": 2,
                            "tipo": "mcq",
                            "enunciado": "¿Cuál es el género de la palabra 'día'?",
                            "opciones": ["Masculino", "Femenino", "Neutro", "Ambos"],
                            "respuesta_correcta": "Masculino",
                            "pistas": ["Aunque termina en -a", "Es una excepción"]
                        },
                        {
                            "id": 3,
                            "tipo": "write",
                            "enunciado": "Escribe el singular de 'casas': _____",
                            "respuesta_correcta": "casa",
                            "pistas": ["Quita la -s", "Mantén la -a"]
                        }
                    ]
                },
                {
                    "id": 3,
                    "titulo": "Conjugación de verbos: presente",
                    "contenido": """
📚 PRESENTE DE INDICATIVO

🎯 **Verbos regulares**:
- AR: o, as, a, amos, áis, an (hablar)
- ER: o, es, e, emos, éis, en (comer)
- IR: o, es, e, imos, ís, en (vivir)

🎯 **Ejemplos**:
- Yo habl-o
- Tú com-es
- Él viv-e

📹 **Video recomendado**: https://www.youtube.com/watch?v=QM8qWsS3w94
                    """,
                    "ejercicios": [
                        {
                            "id": 1,
                            "tipo": "mcq",
                            "enunciado": "¿Cómo se conjuga 'yo' con el verbo 'comer'?",
                            "opciones": ["como", "comes", "come", "comemos"],
                            "respuesta_correcta": "como",
                            "pistas": ["Es verbo -ER", "Yo = -o"]
                        },
                        {
                            "id": 2,
                            "tipo": "write",
                            "enunciado": "Conjuga 'tú' con el verbo 'hablar': _____",
                            "respuesta_correcta": "hablas",
                            "pistas": ["Verbo -AR", "Tú = -as"]
                        },
                        {
                            "id": 3,
                            "tipo": "mcq",
                            "enunciado": "¿Cómo se dice 'nosotros vivimos'?",
                            "opciones": ["vivir", "vivimos", "viven", "vives"],
                            "respuesta_correcta": "vivimos",
                            "pistas": ["Nosotros = -imos", "Verbo -IR"]
                        }
                    ]
                },
                {
                    "id": 4,
                    "titulo": "Adjetivos calificativos",
                    "contenido": """
📚 ADJETIVOS CALIFICATIVOS

🎯 **Concordancia**:
- Deben concordar en género y número con el sustantivo
- Ejemplo: "casa bonita" (fem. sing.), "libros interesantes" (masc. pl.)

🎯 **Posición**:
- Generalmente después del sustantivo
- Excepciones: bueno, malo, grande, pequeño (pueden ir antes)

📹 **Video recomendado**: https://www.youtube.com/watch?v=K0h2zPvqH_c
                    """,
                    "ejercicios": [
                        {
                            "id": 1,
                            "tipo": "write",
                            "enunciado": "Completa: La casa es _____ (bonito)",
                            "respuesta_correcta": "bonita",
                            "pistas": ["Casa es femenino", "Singular"]
                        },
                        {
                            "id": 2,
                            "tipo": "mcq",
                            "enunciado": "¿Cómo se dice 'perros felices'?",
                            "opciones": ["perro feliz", "perros felices", "perro felices", "perros feliz"],
                            "respuesta_correcta": "perros felices",
                            "pistas": ["Ambos en plural", "Feliz → felices"]
                        }
                    ]
                }
            ]
        }
    
    def cargar_usuarios(self):
        """Carga los usuarios desde el archivo JSON"""
        try:
            with open(self.archivo_usuarios, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"usuarios": []}
    
    def cargar_progreso(self):
        """Carga el progreso desde el archivo JSON"""
        try:
            with open(self.archivo_progreso, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def guardar_datos(self):
        """Guarda todos los datos en los archivos JSON"""
        # Guardar usuarios
        with open(self.archivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(self.usuarios, f, indent=2, ensure_ascii=False)
        
        # Guardar progreso
        with open(self.archivo_progreso, 'w', encoding='utf-8') as f:
            json.dump(self.progreso, f, indent=2, ensure_ascii=False)
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        self.limpiar_pantalla()
        print("╔══════════════════════════════════════════╗")
        print("║    GRAMÁTICA ESPAÑOLA - KHAN STYLE      ║")
        print("╠══════════════════════════════════════════╣")
        
        if self.usuario_actual:
            usuario_data = self.obtener_usuario_data(self.usuario_actual)
            nivel = self.calcular_nivel(usuario_data.get('xp', 0))
            print(f"║  👤 Usuario: {self.usuario_actual}")
            print(f"║  ⭐ Nivel: {nivel}")
            print(f"║  💎 XP: {usuario_data.get('xp', 0)}")
        else:
            print("║  👤 No hay usuario seleccionado")
        
        print("╠══════════════════════════════════════════╣")
        print("║  1. 📚 Ver lecciones de gramática        ║")
        print("║  2. 🏋️  Practicar ejercicios             ║")
        print("║  3. 📊 Ver progreso                      ║")
        print("║  4. 👥 Gestión de usuarios               ║")
        print("║  5. 💾 Exportar progreso                 ║")
        print("║  6. 🚪 Salir                             ║")
        print("╚══════════════════════════════════════════╝")
    
    def gestion_usuarios(self):
        """Menú de gestión de usuarios"""
        while True:
            self.limpiar_pantalla()
            print("╔══════════════════════════════════════════╗")
            print("║        GESTIÓN DE USUARIOS              ║")
            print("╠══════════════════════════════════════════╣")
            print("║  1. 👤 Crear nuevo usuario              ║")
            print("║  2. 🔍 Seleccionar usuario              ║")
            print("║  3. 🗑️  Eliminar usuario                ║")
            print("║  4. 📋 Listar usuarios                  ║")
            print("║  5. ↩️  Volver al menú principal         ║")
            print("╚══════════════════════════════════════════╝")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.seleccionar_usuario()
                if self.usuario_actual:
                    return
            elif opcion == "3":
                self.eliminar_usuario()
            elif opcion == "4":
                self.listar_usuarios()
                input("\nPresiona Enter para continuar...")
            elif opcion == "5":
                return
            else:
                print("Opción no válida. Intenta nuevamente.")
                input("Presiona Enter para continuar...")
    
    def crear_usuario(self):
        """Crea un nuevo usuario"""
        self.limpiar_pantalla()
        print("╔══════════════════════════════════════════╗")
        print("║         CREAR NUEVO USUARIO             ║")
        print("╚══════════════════════════════════════════╝")
        
        while True:
            username = input("\nNombre de usuario: ").strip()
            
            if not username:
                print("El nombre no puede estar vacío.")
                continue
            
            # Verificar si el usuario ya existe
            usuario_existente = next((u for u in self.usuarios["usuarios"] if u["username"] == username), None)
            
            if usuario_existente:
                print("⚠️  Este usuario ya existe. Elige otro nombre.")
                continue
            
            # Crear nuevo usuario
            nuevo_usuario = {
                "username": username,
                "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "xp": 0,
                "lecciones_completadas": 0,
                "ejercicios_completados": 0,
                "racha_actual": 0,
                "mejor_racha": 0
            }
            
            self.usuarios["usuarios"].append(nuevo_usuario)
            
            # Crear estructura de progreso para el usuario
            self.progreso[username] = {
                "mastery": {},  # (leccion_id, ejercicio_id): mastery_level
                "ultima_practica": None,
                "ejercicios_resueltos_hoy": 0
            }
            
            # Inicializar mastery para todos los ejercicios
            for leccion in self.lecciones["lecciones"]:
                for ejercicio in leccion["ejercicios"]:
                    clave = f"{leccion['id']}-{ejercicio['id']}"
                    self.progreso[username]["mastery"][clave] = {
                        "mastery": 0,
                        "next_due": datetime.now().strftime("%Y-%m-%d"),
                        "intentos": 0,
                        "aciertos": 0
                    }
            
            self.guardar_datos()
            print(f"\n✅ Usuario '{username}' creado exitosamente!")
            
            seleccionar = input("\n¿Quieres seleccionar este usuario ahora? (s/n): ").lower()
            if seleccionar == 's':
                self.usuario_actual = username
                print(f"👤 Usuario '{username}' seleccionado.")
            
            input("\nPresiona Enter para continuar...")
            break
    
    def seleccionar_usuario(self):
        """Selecciona un usuario existente"""
        self.limpiar_pantalla()
        
        if not self.usuarios["usuarios"]:
            print("⚠️  No hay usuarios registrados.")
            input("Presiona Enter para continuar...")
            return
        
        print("╔══════════════════════════════════════════╗")
        print("║         SELECCIONAR USUARIO             ║")
        print("╠══════════════════════════════════════════╣")
        
        for i, usuario in enumerate(self.usuarios["usuarios"], 1):
            nivel = self.calcular_nivel(usuario["xp"])
            print(f"║  {i}. {usuario['username']} - Nivel {nivel} ({usuario['xp']} XP)")
        
        print("║  0. ↩️  Cancelar                          ║")
        print("╚══════════════════════════════════════════╝")
        
        try:
            seleccion = int(input("\nSelecciona un usuario (número): "))
            
            if seleccion == 0:
                return
            
            if 1 <= seleccion <= len(self.usuarios["usuarios"]):
                usuario_seleccionado = self.usuarios["usuarios"][seleccion - 1]
                self.usuario_actual = usuario_seleccionado["username"]
                print(f"\n✅ Usuario '{self.usuario_actual}' seleccionado.")
            else:
                print("⚠️  Selección no válida.")
        except ValueError:
            print("⚠️  Ingresa un número válido.")
        
        input("\nPresiona Enter para continuar...")
    
    def eliminar_usuario(self):
        """Elimina un usuario existente"""
        self.limpiar_pantalla()
        
        if not self.usuarios["usuarios"]:
            print("⚠️  No hay usuarios registrados.")
            input("Presiona Enter para continuar...")
            return
        
        print("╔══════════════════════════════════════════╗")
        print("║          ELIMINAR USUARIO               ║")
        print("╠══════════════════════════════════════════╣")
        
        for i, usuario in enumerate(self.usuarios["usuarios"], 1):
            print(f"║  {i}. {usuario['username']}")
        
        print("║  0. ↩️  Cancelar                          ║")
        print("╚══════════════════════════════════════════╝")
        
        try:
            seleccion = int(input("\nSelecciona un usuario para eliminar (número): "))
            
            if seleccion == 0:
                return
            
            if 1 <= seleccion <= len(self.usuarios["usuarios"]):
                usuario_eliminar = self.usuarios["usuarios"][seleccion - 1]
                
                confirmar = input(f"\n⚠️  ¿Estás seguro de eliminar a '{usuario_eliminar['username']}'? (s/n): ").lower()
                
                if confirmar == 's':
                    # Eliminar usuario
                    self.usuarios["usuarios"].pop(seleccion - 1)
                    
                    # Eliminar progreso del usuario
                    if usuario_eliminar["username"] in self.progreso:
                        del self.progreso[usuario_eliminar["username"]]
                    
                    # Si el usuario eliminado era el actual, deseleccionarlo
                    if self.usuario_actual == usuario_eliminar["username"]:
                        self.usuario_actual = None
                    
                    self.guardar_datos()
                    print(f"✅ Usuario '{usuario_eliminar['username']}' eliminado.")
                else:
                    print("❌ Eliminación cancelada.")
            else:
                print("⚠️  Selección no válida.")
        except ValueError:
            print("⚠️  Ingresa un número válido.")
        
        input("\nPresiona Enter para continuar...")
    
    def listar_usuarios(self):
        """Lista todos los usuarios con sus estadísticas"""
        self.limpiar_pantalla()
        
        if not self.usuarios["usuarios"]:
            print("⚠️  No hay usuarios registrados.")
            return
        
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                      LISTA DE USUARIOS                      ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        for usuario in self.usuarios["usuarios"]:
            nivel = self.calcular_nivel(usuario["xp"])
            print(f"║  👤 {usuario['username']}")
            print(f"║     ⭐ Nivel: {nivel}")
            print(f"║     💎 XP: {usuario['xp']}")
            print(f"║     📅 Registrado: {usuario['fecha_creacion']}")
            print(f"║     ✅ Ejercicios: {usuario['ejercicios_completados']}")
            print(f"║     🔥 Mejor racha: {usuario['mejor_racha']}")
            print("╠══════════════════════════════════════════════════════════════╣")
    
    def obtener_usuario_data(self, username):
        """Obtiene los datos de un usuario específico"""
        for usuario in self.usuarios["usuarios"]:
            if usuario["username"] == username:
                return usuario
        return None
    
    def calcular_nivel(self, xp):
        """Calcula el nivel basado en XP (fórmula simple)"""
        return xp // 100 + 1
    
    def ver_lecciones(self):
        """Muestra las lecciones disponibles"""
        while True:
            self.limpiar_pantalla()
            print("╔══════════════════════════════════════════╗")
            print("║          LECCIONES DE GRAMÁTICA         ║")
            print("╠══════════════════════════════════════════╣")
            
            for i, leccion in enumerate(self.lecciones["lecciones"], 1):
                # Calcular progreso si hay usuario
                progreso = 0
                if self.usuario_actual and self.usuario_actual in self.progreso:
                    mastery_data = self.progreso[self.usuario_actual]["mastery"]
                    ejercicios_leccion = [k for k in mastery_data.keys() if k.startswith(f"{leccion['id']}-")]
                    if ejercicios_leccion:
                        mastery_total = sum(mastery_data[e]["mastery"] for e in ejercicios_leccion)
                        progreso = min(100, (mastery_total / (len(ejercicios_leccion) * 10)) * 100)
                
                barra = self.crear_barra_progreso(progreso)
                print(f"║  {i}. {leccion['titulo']}")
                print(f"║     {barra} {progreso:.0f}%")
            
            print("╠══════════════════════════════════════════╣")
            print("║  0. ↩️  Volver                            ║")
            print("╚══════════════════════════════════════════╝")
            
            try:
                seleccion = int(input("\nSelecciona una lección (número): "))
                
                if seleccion == 0:
                    return
                
                if 1 <= seleccion <= len(self.lecciones["lecciones"]):
                    self.mostrar_leccion(seleccion - 1)
                else:
                    print("⚠️  Selección no válida.")
                    input("Presiona Enter para continuar...")
            except ValueError:
                print("⚠️  Ingresa un número válido.")
                input("Presiona Enter para continuar...")
    
    def crear_barra_progreso(self, porcentaje, ancho=20):
        """Crea una barra de progreso visual"""
        completado = int(porcentaje * ancho / 100)
        return "█" * completado + "░" * (ancho - completado)
    
    def mostrar_leccion(self, indice):
        """Muestra el contenido de una lección específica"""
        leccion = self.lecciones["lecciones"][indice]
        
        while True:
            self.limpiar_pantalla()
            print(f"╔══════════════════════════════════════════╗")
            print(f"║         {leccion['titulo'].center(38)}         ║")
            print(f"╠══════════════════════════════════════════╣")
            print(f"{leccion['contenido']}")
            print(f"╠══════════════════════════════════════════╣")
            print(f"║  1. 🏋️  Practicar ejercicios de esta lección ║")
            print(f"║  0. ↩️  Volver a lecciones                 ║")
            print(f"╚══════════════════════════════════════════╝")
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.practicar_leccion_especifica(indice)
            elif opcion == "0":
                return
            else:
                print("Opción no válida.")
    
    def practicar(self):
        """Sesión de práctica con spaced repetition"""
        if not self.usuario_actual:
            print("⚠️  Primero selecciona un usuario.")
            input("Presiona Enter para continuar...")
            return
        
        self.limpiar_pantalla()
        print("╔══════════════════════════════════════════╗")
        print("║          SESIÓN DE PRÁCTICA             ║")
        print("╠══════════════════════════════════════════╣")
        
        # Obtener ejercicios debidos (next_due <= hoy)
        hoy = datetime.now().strftime("%Y-%m-%d")
        ejercicios_debidos = []
        
        mastery_data = self.progreso[self.usuario_actual]["mastery"]
        
        for clave, data in mastery_data.items():
            if data["next_due"] <= hoy:
                leccion_id, ejercicio_id = map(int, clave.split("-"))
                ejercicios_debidos.append({
                    "clave": clave,
                    "leccion_id": leccion_id,
                    "ejercicio_id": ejercicio_id,
                    "mastery": data["mastery"]
                })
        
        if not ejercicios_debidos:
            print("║  🎉 ¡No hay ejercicios pendientes hoy!     ║")
            print("║  Todos están al día.                       ║")
            print("╚══════════════════════════════════════════╝")
            
            # Ofrecer practicar igual
            opcion = input("\n¿Quieres practicar ejercicios igualmente? (s/n): ").lower()
            if opcion == 's':
                self.practicar_cualquier_ejercicio()
            return
        
        print(f"║  📝 Ejercicios pendientes: {len(ejercicios_debidos)}")
        print("║  🔥 Ordenados por prioridad (menor mastery primero)")
        print("╚══════════════════════════════════════════╝")
        
        # Ordenar por mastery (menor primero)
        ejercicios_debidos.sort(key=lambda x: x["mastery"])
        
        # Limitar a 5 ejercicios por sesión
        ejercicios_practica = ejercicios_debidos[:5]
        
        input("\nPresiona Enter para comenzar la práctica...")
        
        ejercicios_resueltos = 0
        aciertos = 0
        
        for ejercicio_info in ejercicios_practica:
            resultado = self.resolver_ejercicio(
                ejercicio_info["leccion_id"],
                ejercicio_info["ejercicio_id"]
            )
            
            if resultado is not None:
                ejercicios_resueltos += 1
                if resultado:  # Si acertó
                    aciertos += 1
                
                # Actualizar mastery y next_due
                self.actualizar_mastery(
                    ejercicio_info["clave"],
                    resultado
                )
        
        # Actualizar estadísticas del usuario
        if ejercicios_resueltos > 0:
            usuario_data = self.obtener_usuario_data(self.usuario_actual)
            
            # XP por ejercicio resuelto
            xp_ganada = ejercicios_resueltos * 10 + aciertos * 5
            usuario_data["xp"] += xp_ganada
            usuario_data["ejercicios_completados"] += ejercicios_resueltos
            
            # Actualizar racha
            if aciertos == ejercicios_resueltos:  # Todos correctos
                usuario_data["racha_actual"] += 1
                usuario_data["mejor_racha"] = max(
                    usuario_data["mejor_racha"],
                    usuario_data["racha_actual"]
                )
            else:
                usuario_data["racha_actual"] = 0
            
            # Actualizar última práctica
            self.progreso[self.usuario_actual]["ultima_practica"] = hoy
            self.progreso[self.usuario_actual]["ejercicios_resueltos_hoy"] = ejercicios_resueltos
            
            self.guardar_datos()
            
            print(f"\n✅ Sesión completada!")
            print(f"📊 Resumen:")
            print(f"   Ejercicios resueltos: {ejercicios_resueltos}")
            print(f"   Aciertos: {aciertos}/{ejercicios_resueltos}")
            print(f"   XP ganada: +{xp_ganada}")
            print(f"   XP total: {usuario_data['xp']}")
            print(f"   Nivel: {self.calcular_nivel(usuario_data['xp'])}")
            print(f"   🔥 Racha actual: {usuario_data['racha_actual']}")
        
        input("\nPresiona Enter para continuar...")
    
    def practicar_leccion_especifica(self, indice_leccion):
        """Practica ejercicios de una lección específica"""
        leccion = self.lecciones["lecciones"][indice_leccion]
        
        print(f"\n🏋️  Practicando: {leccion['titulo']}")
        print(f"📝 {len(leccion['ejercicios'])} ejercicios disponibles")
        
        ejercicios_resueltos = 0
        aciertos = 0
        
        for ejercicio in leccion["ejercicios"]:
            resultado = self.resolver_ejercicio(leccion["id"], ejercicio["id"])
            
            if resultado is not None:
                ejercicios_resueltos += 1
                if resultado:
                    aciertos += 1
                
                # Actualizar mastery para este ejercicio si hay usuario
                if self.usuario_actual:
                    clave = f"{leccion['id']}-{ejercicio['id']}"
                    self.actualizar_mastery(clave, resultado)
        
        # Actualizar XP si hay usuario
        if self.usuario_actual and ejercicios_resueltos > 0:
            usuario_data = self.obtener_usuario_data(self.usuario_actual)
            xp_ganada = ejercicios_resueltos * 10 + aciertos * 5
            usuario_data["xp"] += xp_ganada
            usuario_data["ejercicios_completados"] += ejercicios_resueltos
            self.guardar_datos()
            
            print(f"\n📊 Resumen lección:")
            print(f"   Aciertos: {aciertos}/{ejercicios_resueltos}")
            print(f"   XP ganada: +{xp_ganada}")
        
        input("\nPresiona Enter para continuar...")
    
    def practicar_cualquier_ejercicio(self):
        """Practica ejercicios aleatorios"""
        print("\n🎲 Practicando ejercicios aleatorios...")
        
        # Seleccionar 3 ejercicios aleatorios
        ejercicios_seleccionados = []
        for _ in range(3):
            leccion = random.choice(self.lecciones["lecciones"])
            ejercicio = random.choice(leccion["ejercicios"])
            ejercicios_seleccionados.append((leccion["id"], ejercicio["id"]))
        
        ejercicios_resueltos = 0
        aciertos = 0
        
        for leccion_id, ejercicio_id in ejercicios_seleccionados:
            resultado = self.resolver_ejercicio(leccion_id, ejercicio_id)
            
            if resultado is not None:
                ejercicios_resueltos += 1
                if resultado:
                    aciertos += 1
                
                # Actualizar mastery
                if self.usuario_actual:
                    clave = f"{leccion_id}-{ejercicio_id}"
                    self.actualizar_mastery(clave, resultado)
        
        # Actualizar XP
        if self.usuario_actual and ejercicios_resueltos > 0:
            usuario_data = self.obtener_usuario_data(self.usuario_actual)
            xp_ganada = ejercicios_resueltos * 10 + aciertos * 5
            usuario_data["xp"] += xp_ganada
            usuario_data["ejercicios_completados"] += ejercicios_resueltos
            self.guardar_datos()
            
            print(f"\n📊 Resumen práctica aleatoria:")
            print(f"   Aciertos: {aciertos}/{ejercicios_resueltos}")
            print(f"   XP ganada: +{xp_ganada}")
        
        input("\nPresiona Enter para continuar...")
    
    def obtener_ejercicio(self, leccion_id, ejercicio_id):
        """Obtiene un ejercicio específico"""
        for leccion in self.lecciones["lecciones"]:
            if leccion["id"] == leccion_id:
                for ejercicio in leccion["ejercicios"]:
                    if ejercicio["id"] == ejercicio_id:
                        return ejercicio
        return None
    
    def resolver_ejercicio(self, leccion_id, ejercicio_id):
        """Presenta un ejercicio para resolver y verifica la respuesta"""
        ejercicio = self.obtener_ejercicio(leccion_id, ejercicio_id)
        
        if not ejercicio:
            print(f"⚠️  Ejercicio no encontrado.")
            return None
        
        self.limpiar_pantalla()
        print(f"╔══════════════════════════════════════════╗")
        print(f"║               EJERCICIO                 ║")
        print(f"╠══════════════════════════════════════════╣")
        print(f"║  📝 {ejercicio['enunciado']}")
        print(f"╠══════════════════════════════════════════╣")
        
        intentos = 0
        max_intentos = 3
        
        while intentos < max_intentos:
            if ejercicio["tipo"] == "mcq":
                print("║  Opciones:")
                for i, opcion in enumerate(ejercicio["opciones"], 1):
                    print(f"║    {i}. {opcion}")
                print(f"╠══════════════════════════════════════════╣")
                respuesta = input("║  Tu respuesta (número o texto): ").strip()
                
                # Verificar si respuesta es número
                if respuesta.isdigit():
                    num = int(respuesta)
                    if 1 <= num <= len(ejercicio["opciones"]):
                        respuesta_usuario = ejercicio["opciones"][num - 1]
                    else:
                        print("║  ⚠️  Número fuera de rango.")
                        intentos += 1
                        continue
                else:
                    respuesta_usuario = respuesta
            
            else:  # tipo write
                respuesta_usuario = input("║  Tu respuesta: ").strip()
            
            # Normalizar respuesta
            respuesta_usuario = respuesta_usuario.lower().strip()
            respuesta_correcta = ejercicio["respuesta_correcta"].lower().strip()
            
            # Verificar respuesta
            if respuesta_usuario == respuesta_correcta:
                print(f"║  ✅ ¡Correcto! {respuesta_correcta.capitalize()}")
                print(f"╚══════════════════════════════════════════╝")
                return True
            else:
                intentos += 1
                intentos_restantes = max_intentos - intentos
                
                if intentos_restantes > 0:
                    print(f"║  ❌ Incorrecto. Intentos restantes: {intentos_restantes}")
                    
                    # Mostrar pista después del primer error
                    if intentos == 1 and "pistas" in ejercicio and ejercicio["pistas"]:
                        print(f"║  💡 Pista: {ejercicio['pistas'][0]}")
                    
                    if intentos == 2 and len(ejercicio.get("pistas", [])) > 1:
                        print(f"║  💡 Otra pista: {ejercicio['pistas'][1]}")
                else:
                    print(f"║  ❌ La respuesta correcta era: {respuesta_correcta.capitalize()}")
                    print(f"╚══════════════════════════════════════════╝")
                    return False
        
        return False
    
    def actualizar_mastery(self, clave, acierto):
        """Actualiza el mastery y next_due basado en si acertó o no"""
        if self.usuario_actual not in self.progreso:
            return
        
        data = self.progreso[self.usuario_actual]["mastery"][clave]
        
        # Actualizar estadísticas
        data["intentos"] += 1
        if acierto:
            data["aciertos"] += 1
            # Aumentar mastery (máximo 10)
            data["mastery"] = min(10, data["mastery"] + 1)
        else:
            # Disminuir mastery (mínimo 0)
            data["mastery"] = max(0, data["mastery"] - 1)
        
        # Calcular next_due basado en mastery
        hoy = datetime.now()
        
        if data["mastery"] < 10:
            # Fórmula simple: más mastery = más días hasta la próxima revisión
            dias_para_proxima = 10 - data["mastery"]
        else:
            # Si mastery es 10, revisar en 30 días
            dias_para_proxima = 30
        
        next_due = hoy + timedelta(days=dias_para_proxima)
        data["next_due"] = next_due.strftime("%Y-%m-%d")
    
    def ver_progreso(self):
        """Muestra el progreso del usuario actual"""
        if not self.usuario_actual:
            print("⚠️  Primero selecciona un usuario.")
            input("Presiona Enter para continuar...")
            return
        
        usuario_data = self.obtener_usuario_data(self.usuario_actual)
        progreso_data = self.progreso.get(self.usuario_actual, {})
        
        self.limpiar_pantalla()
        print("╔══════════════════════════════════════════════════════════════╗")
        print(f"║               PROGRESO - {self.usuario_actual.center(30)}               ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        # Estadísticas generales
        nivel = self.calcular_nivel(usuario_data["xp"])
        xp_para_proximo_nivel = nivel * 100 - usuario_data["xp"]
        
        print(f"║  ⭐ Nivel: {nivel}")
        print(f"║  💎 XP: {usuario_data['xp']} (faltan {xp_para_proximo_nivel} para nivel {nivel + 1})")
        print(f"║  📅 Registrado: {usuario_data['fecha_creacion']}")
        print(f"║  ✅ Ejercicios completados: {usuario_data['ejercicios_completados']}")
        print(f"║  🔥 Racha actual: {usuario_data['racha_actual']}")
        print(f"║  🏆 Mejor racha: {usuario_data['mejor_racha']}")
        
        if "ultima_practica" in progreso_data:
            print(f"║  📍 Última práctica: {progreso_data['ultima_practica']}")
        
        print("╠══════════════════════════════════════════════════════════════╣")
        print("║                    PROGRESO POR LECCIÓN                     ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        # Progreso por lección
        for leccion in self.lecciones["lecciones"]:
            if "mastery" not in progreso_data:
                continue
            
            # Calcular mastery promedio para esta lección
            ejercicios_leccion = []
            for clave in progreso_data["mastery"]:
                if clave.startswith(f"{leccion['id']}-"):
                    ejercicios_leccion.append(progreso_data["mastery"][clave])
            
            if ejercicios_leccion:
                mastery_promedio = sum(e["mastery"] for e in ejercicios_leccion) / len(ejercicios_leccion)
                porcentaje = (mastery_promedio / 10) * 100
                barra = self.crear_barra_progreso(porcentaje, 15)
                
                # Contar ejercicios pendientes
                hoy = datetime.now().strftime("%Y-%m-%d")
                pendientes = sum(1 for e in ejercicios_leccion if e["next_due"] <= hoy)
                
                print(f"║  {leccion['titulo']}")
                print(f"║     {barra} {porcentaje:.0f}% - {pendientes} pendientes")
                print("╠══════════════════════════════════════════════════════════════╣")
        
        print("║  1. 📋 Ver detalles de mastery por ejercicio                  ║")
        print("║  0. ↩️  Volver                                                 ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            self.ver_detalles_mastery()
    
    def ver_detalles_mastery(self):
        """Muestra detalles del mastery por ejercicio"""
        if not self.usuario_actual:
            return
        
        progreso_data = self.progreso.get(self.usuario_actual, {})
        
        if "mastery" not in progreso_data:
            print("No hay datos de mastery.")
            return
        
        self.limpiar_pantalla()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║               DETALLES DE MASTERY                          ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        
        hoy = datetime.now().strftime("%Y-%m-%d")
        
        for leccion in self.lecciones["lecciones"]:
            print(f"║  📚 {leccion['titulo']}")
            print("╠══════════════════════════════════════════════════════════════╣")
            
            for ejercicio in leccion["ejercicios"]:
                clave = f"{leccion['id']}-{ejercicio['id']}"
                if clave in progreso_data["mastery"]:
                    data = progreso_data["mastery"][clave]
                    
                    # Icono según mastery
                    if data["mastery"] >= 8:
                        icono = "🔵"
                    elif data["mastery"] >= 5:
                        icono = "🟢"
                    elif data["mastery"] >= 3:
                        icono = "🟡"
                    else:
                        icono = "🔴"
                    
                    # Estado
                    if data["next_due"] <= hoy:
                        estado = "⏳ Pendiente"
                    else:
                        estado = "✅ Al día"
                    
                    print(f"║  {icono} Ejercicio {ejercicio['id']}: {ejercicio['enunciado'][:40]}...")
                    print(f"║     Mastery: {data['mastery']}/10 | {estado}")
                    print(f"║     Próxima revisión: {data['next_due']}")
                    print(f"║     Aciertos: {data['aciertos']}/{data['intentos']}")
                    print("╠══════════════════════════════════════════════════════════════╣")
        
        input("\nPresiona Enter para continuar...")
    
    def exportar_progreso(self):
        """Exporta el progreso del usuario actual a un archivo .txt"""
        if not self.usuario_actual:
            print("⚠️  Primero selecciona un usuario.")
            input("Presiona Enter para continuar...")
            return
        
        usuario_data = self.obtener_usuario_data(self.usuario_actual)
        progreso_data = self.progreso.get(self.usuario_actual, {})
        
        # Crear nombre de archivo
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"progreso_{self.usuario_actual}_{fecha}.txt"
        
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write(f"PROGRESO DE APRENDIZAJE - {self.usuario_actual}\n")
                f.write(f"Exportado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                # Estadísticas generales
                nivel = self.calcular_nivel(usuario_data["xp"])
                f.write("ESTADÍSTICAS GENERALES\n")
                f.write("-" * 40 + "\n")
                f.write(f"Nivel: {nivel}\n")
                f.write(f"XP: {usuario_data['xp']}\n")
                f.write(f"Ejercicios completados: {usuario_data['ejercicios_completados']}\n")
                f.write(f"Racha actual: {usuario_data['racha_actual']}\n")
                f.write(f"Mejor racha: {usuario_data['mejor_racha']}\n")
                f.write(f"Fecha de registro: {usuario_data['fecha_creacion']}\n\n")
                
                # Progreso por lección
                f.write("PROGRESO POR LECCIÓN\n")
                f.write("-" * 40 + "\n")
                
                hoy = datetime.now().strftime("%Y-%m-%d")
                
                for leccion in self.lecciones["lecciones"]:
                    if "mastery" not in progreso_data:
                        continue
                    
                    # Calcular para esta lección
                    ejercicios_leccion = []
                    for clave in progreso_data["mastery"]:
                        if clave.startswith(f"{leccion['id']}-"):
                            ejercicios_leccion.append(progreso_data["mastery"][clave])
                    
                    if ejercicios_leccion:
                        mastery_promedio = sum(e["mastery"] for e in ejercicios_leccion) / len(ejercicios_leccion)
                        pendientes = sum(1 for e in ejercicios_leccion if e["next_due"] <= hoy)
                        
                        f.write(f"\n{leccion['titulo']}:\n")
                        f.write(f"  Mastery promedio: {mastery_promedio:.1f}/10\n")
                        f.write(f"  Ejercicios pendientes: {pendientes}\n")
                        
                        # Detalle por ejercicio
                        for ejercicio in leccion["ejercicios"]:
                            clave = f"{leccion['id']}-{ejercicio['id']}"
                            if clave in progreso_data["mastery"]:
                                data = progreso_data["mastery"][clave]
                                f.write(f"  - Ejercicio {ejercicio['id']}: mastery={data['mastery']}/10, ")
                                f.write(f"próxima={data['next_due']}, ")
                                f.write(f"aciertos={data['aciertos']}/{data['intentos']}\n")
                
                # Ejercicios pendientes para hoy
                f.write("\n" + "=" * 60 + "\n")
                f.write("EJERCICIOS PENDIENTES PARA HOY\n")
                f.write("-" * 40 + "\n")
                
                pendientes_hoy = []
                for clave, data in progreso_data.get("mastery", {}).items():
                    if data["next_due"] <= hoy:
                        leccion_id, ejercicio_id = map(int, clave.split("-"))
                        ejercicio_obj = self.obtener_ejercicio(leccion_id, ejercicio_id)
                        if ejercicio_obj:
                            pendientes_hoy.append((clave, data, ejercicio_obj))
                
                if pendientes_hoy:
                    for clave, data, ejercicio in pendientes_hoy:
                        f.write(f"\n• {ejercicio['enunciado']}\n")
                        f.write(f"  Mastery: {data['mastery']}/10 | ")
                        f.write(f"Última revisión: {data['next_due']}\n")
                else:
                    f.write("\n🎉 ¡No hay ejercicios pendientes para hoy!\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("¡Sigue practicando! 💪\n")
                f.write("=" * 60 + "\n")
            
            print(f"✅ Progreso exportado a: {nombre_archivo}")
            print(f"📄 Total de líneas escritas: {sum(1 for _ in open(nombre_archivo, 'r', encoding='utf-8'))}")
            
        except Exception as e:
            print(f"❌ Error al exportar: {e}")
        
        input("\nPresiona Enter para continuar...")
    
    def ejecutar(self):
        """Ejecuta la aplicación principal"""
        while True:
            self.mostrar_menu_principal()
            
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == "1":
                self.ver_lecciones()
            elif opcion == "2":
                self.practicar()
            elif opcion == "3":
                self.ver_progreso()
            elif opcion == "4":
                self.gestion_usuarios()
            elif opcion == "5":
                self.exportar_progreso()
            elif opcion == "6":
                print("\n¡Hasta pronto! Guardando datos...")
                self.guardar_datos()
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
                input("Presiona Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    app = SistemaGramaticaEspanola()
    app.ejecutar()
