import sys
import json


class Objeto:
    def __init__(self, nombre, categoria, descripcion, uso=None, cantidad=1, equipado=False):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.uso = uso
        self.cantidad = cantidad
        self.equipado = equipado

    def usar(self):
        if self.uso:
            print(f"{self.nombre}: {self.uso}")
            if self.cantidad > 1:
                self.cantidad -= 1
                print(f"Quedan {self.cantidad} de {self.nombre}.")
            else:
                print(f"Has usado el último {self.nombre}.")
        else:
            print(f"No sabes cómo usar el {self.nombre}.")

    def equipar(self):
        if not self.equipado:
            self.equipado = True
            print(f"Has equipado '{self.nombre}'.")
        else:
            print(f"'{self.nombre}' ya está equipado.")

    def desequipar(self):
        if self.equipado:
            self.equipado = False
            print(f"Has desequipado '{self.nombre}'.")
        else:
            print(f"'{self.nombre}' no está equipado.")


def agregar_objeto(inventario, objeto):
    categoria = objeto.categoria
    # Buscar si el objeto ya existe en la categoría
    for obj in inventario.get(categoria, []):
        if obj.nombre.lower() == objeto.nombre.lower():
            obj.cantidad += objeto.cantidad
            print(f"Has agregado {obj.cantidad} más de '{obj.nombre}' al inventario bajo '{categoria}'.\n")
            return
    # Si no existe, agregar como nuevo
    if categoria in inventario:
        inventario[categoria].append(objeto)
    else:
        inventario[categoria] = [objeto]
    print(f"Has agregado '{objeto.nombre}' al inventario bajo '{categoria}'.\n")


def eliminar_objeto(inventario, nombre_objeto):
    for categoria, objetos in inventario.items():
        for objeto in objetos:
            if objeto.nombre.lower() == nombre_objeto.lower():
                if objeto.cantidad > 1:
                    objeto.cantidad -= 1
                    print(f"Has eliminado una unidad de '{objeto.nombre}'. Quedan {objeto.cantidad}.\n")
                else:
                    objetos.remove(objeto)
                    print(f"Has eliminado '{objeto.nombre}' del inventario.\n")
                return
    print(f"No se encontró '{nombre_objeto}' en el inventario.\n")


def usar_objeto(inventario, nombre_objeto):
    for categoria, objetos in inventario.items():
        for objeto in objetos:
            if objeto.nombre.lower() == nombre_objeto.lower():
                objeto.usar()
                return
    print(f"No tienes '{nombre_objeto}' en tu inventario.\n")


def mostrar_inventario(inventario):
    print("\nInventario del jugador:")
    for categoria, objetos in inventario.items():
        if objetos:
            print(f"\n{categoria}:")
            for idx, objeto in enumerate(objetos, 1):
                equipado = " [Equipado]" if objeto.equipado else ""
                print(f"  {idx}. {objeto.nombre} x{objeto.cantidad}{equipado}: {objeto.descripcion}")
    print()


class Room:
    def __init__(self, nombre, descripcion_es, descripcion_en):
        """
        Inicializa una nueva habitación con descripciones en español e inglés.

        :param nombre: Nombre de la habitación.
        :param descripcion_es: Descripción en español.
        :param descripcion_en: Descripción en inglés.
        """
        self.nombre = nombre
        self.descripcion_es = descripcion_es
        self.descripcion_en = descripcion_en
        self.salidas = {}  # dirección: nombre de la habitación
        self.objetos = []  # lista de objetos en la habitación
        self.personajes = []  # lista de personajes en la habitación
        self.eventos = []  # lista de eventos en la habitación

    def agregar_salida(self, direccion, nombre_habitacion):
        self.salidas[direccion] = nombre_habitacion

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def remover_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)

    def agregar_evento(self, evento):
        self.eventos.append(evento)


class Character:
    def __init__(self, nombre, descripcion, dialogos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.dialogos = dialogos  # diccionario con diálogos según el estado del juego
        self.activo = True

    def hablar(self, estado_juego):
        return self.dialogos.get(estado_juego,
                                 self.dialogos.get('default', f"{self.nombre} no tiene nada que decir ahora."))


class Event:
    def __init__(self, trigger, descripcion, accion):
        self.trigger = trigger  # función que retorna True/False
        self.descripcion = descripcion
        self.accion = accion  # función a ejecutar cuando el evento se desencadena


class Game:
    def __init__(self):
        self.habitaciones = {}
        self.habitacion_actual = None
        self.inventario = {}
        self.estado_juego = "inicio"
        self.game_over = False
        self.comandos = {
            'ir': self.mover,
            'agarrar': self.agarrar,
            'usar': self.usar,
            'hablar': self.hablar,
            'inventario': self.mostrar_inventario_jugador,
            'guardar': self.guardar_partida,
            'cargar': self.cargar_partida,
            'ayuda': self.mostrar_ayuda,
            'salir': self.salir_juego,
            'equipar': self.equipar_objeto,
            'desequipar': self.desequipar_objeto
        }
        self.traducciones_comandos = {
            "ir": "go",
            "agarrar": "grab",
            "usar": "use",
            "hablar": "talk",
            "inventario": "inventory",
            "guardar": "save",
            "cargar": "load",
            "ayuda": "help",
            "salir": "exit",
            "equipar": "equip",
            "desequipar": "unequip"
        }
        self.traducciones_direcciones = {
            "norte": "north",
            "sur": "south",
            "este": "east",
            "oeste": "west",
            "abajo": "down",
            "arriba": "up",
            "izquierda": "left",
            "derecha": "right",
            "noreste": "northeast",
            "noroeste": "northwest",
            "sureste": "southeast",
            "suroeste": "southwest"
        }
        self.traducciones_objetos = {
            "cuchillo de hoja fija": "fixed-blade knife",
            "sierra plegable": "folding saw",
            "linterna frontal": "headlamp",
            "hacha": "axe",
            "cuerda resistente": "strong rope",
            "filtro de agua": "water filter",
            "saco de dormir": "sleeping bag",
            "estufa portátil": "portable stove",
            "kit de primeros auxilios": "first aid kit"
        }
        self.configurar_juego()

    def configurar_juego(self):
        # Crear objetos de supervivencia
        cuchillo = Objeto(
            nombre="Cuchillo de hoja fija",
            categoria="Herramientas",
            descripcion="Un cuchillo afilado, útil para cortar ramas o preparar alimentos.",
            uso="Has utilizado el cuchillo para cortar algunas ramas y construir un refugio sencillo.",
            cantidad=1
        )
        sierra = Objeto(
            nombre="Sierra plegable",
            categoria="Herramientas",
            descripcion="Pequeña y portátil, perfecta para cortar leña o despejar caminos.",
            uso="Has utilizado la sierra para cortar leña y mantener el fuego encendido.",
            cantidad=1
        )
        filtro_agua = Objeto(
            nombre="Filtro de agua",
            categoria="Cocción e Hidratación",
            descripcion="Purifica el agua de ríos o arroyos, esencial para mantenerse hidratado.",
            uso="Has purificado el agua con el filtro. Ahora tienes agua potable.",
            cantidad=1
        )
        saco_dormir = Objeto(
            nombre="Saco de dormir",
            categoria="Refugio y Equipo de Sueño",
            descripcion="Ligero y cálido, ideal para pasar una noche en el bosque.",
            uso="Te has acomodado en el saco de dormir, recuperando energía para el día siguiente.",
            cantidad=1
        )
        linterna = Objeto(
            nombre="Linterna frontal",
            categoria="Ropa y Equipo Personal",
            descripcion="Ilumina tu camino y deja tus manos libres para trabajar en la oscuridad.",
            uso="Has encendido la linterna frontal, iluminando el camino por la noche.",
            cantidad=1
        )
        cuerda = Objeto(
            nombre="Cuerda resistente",
            categoria="Herramientas",
            descripcion="Fuerte y útil para construir refugios o escalar.",
            uso="Has utilizado la cuerda para asegurar el refugio contra el viento.",
            cantidad=1
        )
        hacha = Objeto(
            nombre="Hacha",
            categoria="Herramientas",
            descripcion="Un hacha resistente, perfecta para cortar leña o defenderte.",
            uso="Has utilizado el hacha para cortar leña y mantener el fuego encendido.",
            cantidad=1
        )
        estufa_portatil = Objeto(
            nombre="Estufa portátil",
            categoria="Cocción e Hidratación",
            descripcion="Ideal para cocinar alimentos de manera eficiente en la naturaleza.",
            uso="Has encendido la estufa portátil y preparado una comida caliente.",
            cantidad=1
        )
        kit_primeros_auxilios = Objeto(
            nombre="Kit de Primeros Auxilios",
            categoria="Seguridad y Primeros Auxilios",
            descripcion="Contiene vendajes, antisépticos y medicamentos básicos para emergencias.",
            uso="Has utilizado el kit para tratar una herida, evitando una infección.",
            cantidad=1
        )

        # Crear habitaciones con descripciones en español e inglés
        plaza = Room(
            nombre="Plaza Central",
            descripcion_es="Una amplia plaza con fuentes y estatuas abandonadas.",
            descripcion_en="A spacious plaza with abandoned fountains and statues."
        )
        supermercado = Room(
            nombre="Supermercado Abandonado",
            descripcion_es="Estantes vacíos y pasillos oscuros.",
            descripcion_en="Empty shelves and dark corridors."
        )
        refugio = Room(
            nombre="Refugio Subterráneo",
            descripcion_es="Un refugio seguro con suministros básicos.",
            descripcion_en="A safe shelter with basic supplies."
        )
        calle = Room(
            nombre="Calle Desierta",
            descripcion_es="Calles vacías con edificios deteriorados.",
            descripcion_en="Empty streets with dilapidated buildings."
        )
        parque = Room(
            nombre="Parque Olvidado",
            descripcion_es="Áreas verdes descuidadas y caminos de tierra.",
            descripcion_en="Neglected green areas and dirt paths."
        )
        habitacion_oculta = Room(
            nombre="Habitación Oculta",
            descripcion_es="Una habitación secreta con suministros adicionales.",
            descripcion_en="A secret room with additional supplies."
        )

        # Definir salidas
        plaza.agregar_salida("norte", "Supermercado Abandonado")
        plaza.agregar_salida("este", "Calle Desierta")
        plaza.agregar_salida("oeste", "Parque Olvidado")
        supermercado.agregar_salida("sur", "Plaza Central")
        calle.agregar_salida("oeste", "Plaza Central")
        parque.agregar_salida("este", "Plaza Central")
        refugio.agregar_salida("abajo", "Calle Desierta")
        habitacion_oculta.agregar_salida("sur", "Plaza Central")

        # Agregar objetos a habitaciones
        plaza.agregar_objeto(cuchillo)
        supermercado.agregar_objeto(sierra)
        supermercado.agregar_objeto(linterna)
        refugio.agregar_objeto(filtro_agua)
        calle.agregar_objeto(cuerda)
        parque.agregar_objeto(saco_dormir)
        supermercado.agregar_objeto(hacha)
        refugio.agregar_objeto(estufa_portatil)
        parque.agregar_objeto(kit_primeros_auxilios)

        # Crear personajes
        ana_dialogues = {
            "inicio": "Ana: Hola, Tomson. Gracias por venir. Necesitamos encontrar más suministros.",
            "after_collect_supplies": "Ana: ¡Excelente! Con estos suministros podemos sobrevivir más tiempo.",
            "default": "Ana: Estamos en una situación difícil."
        }
        ana = Character("Ana", "Una sobreviviente inteligente y valiente.", ana_dialogues)
        plaza.agregar_personaje(ana)

        # Crear eventos
        def trigger_carlos(game):
            return any(obj.nombre == "Linterna frontal" for obj in
                       game.inventario.get("Ropa y Equipo Personal", [])) and not any(
                c.nombre == "Carlos" for c in game.habitacion_actual.personajes)

        def accion_carlos(game):
            carlos_dialogues = {
                "inicio": "Carlos: ¡Gracias por la linterna! Estaba perdido en el Supermercado.",
                "after_collect_supplies": "Carlos: Con tus suministros, podemos mejorar nuestro refugio.",
                "default": "Carlos: Estoy aquí para ayudarte."
            }
            carlos = Character("Carlos", "Un técnico con conocimientos en electricidad.", carlos_dialogues)
            game.habitacion_actual.agregar_personaje(carlos)
            print("*** Evento: Carlos ha aparecido en la habitación. ***\n")

        evento_carlos = Event(trigger_carlos, "Carlos ha encontrado su camino al refugio gracias a la linterna.",
                              accion_carlos)
        plaza.agregar_evento(evento_carlos)

        # Guardar habitaciones en el diccionario
        self.habitaciones = {
            "Plaza Central": plaza,
            "Supermercado Abandonado": supermercado,
            "Refugio Subterráneo": refugio,
            "Calle Desierta": calle,
            "Parque Olvidado": parque,
            "Habitación Oculta": habitacion_oculta
        }

        # Establecer habitación inicial
        self.habitacion_actual = plaza

    def traducir_comando(self, comando_espanol):
        """
        Solicita al usuario que traduzca el comando al inglés y proporciona retroalimentación.
        """
        partes = comando_espanol.split()
        verbo_es = partes[0].lower()
        traduccion_verbo = self.traducciones_comandos.get(verbo_es, None)

        if not traduccion_verbo:
            print("Comando desconocido para traducir.\n")
            return False  # No se puede traducir, permite continuar el juego

        # Solicitar traducción del verbo
        traduccion_usuario_verbo = input(f"Por favor, traduce el comando '{verbo_es}': ").strip().lower()
        if traduccion_usuario_verbo == traduccion_verbo:
            print("¡Traducción correcta!\n")
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_verbo}'.\n")

        # Si hay argumentos, intentar traducirlos
        if len(partes) > 1:
            argumento_es = ' '.join(partes[1:]).lower()
            traduccion_arg_usuario = input(f"Por favor, traduce '{argumento_es}': ").strip().lower()
            # Primero, verificar si el argumento es una dirección conocida
            traduccion_arg_esperada = self.traducciones_direcciones.get(argumento_es, None)
            if traduccion_arg_esperada:
                if traduccion_arg_usuario == traduccion_arg_esperada:
                    print("¡Traducción correcta!\n")
                else:
                    print(f"Traducción incorrecta. La traducción correcta es '{traduccion_arg_esperada}'.\n")
            else:
                # Si el argumento no es una dirección conocida, verificar si es un objeto
                traduccion_objeto_esperada = self.traducciones_objetos.get(argumento_es, None)
                if traduccion_objeto_esperada:
                    if traduccion_arg_usuario == traduccion_objeto_esperada:
                        print("¡Traducción correcta!\n")
                    else:
                        print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")
                else:
                    # Si el argumento no es una dirección ni un objeto conocido, no se traduce
                    print(f"No se necesita traducir '{argumento_es}'.\n")

        return True  # Continúa con la ejecución del comando

    def solicitar_traduccion(self, descripcion_en):
        """
        Solicita al usuario que traduzca la descripción al inglés y valida la traducción.

        :param descripcion_en: Descripción en inglés que el usuario debe reescribir.
        """
        print("Para continuar la aventura, por favor, reescribe la traducción al inglés de la descripción mostrada.")
        traduccion_usuario = input("Escribe la traducción aquí: ").strip().lower()
        traduccion_correcta = descripcion_en.lower()

        if traduccion_usuario == traduccion_correcta:
            print("¡Traducción correcta! Puedes continuar.\n")
        else:
            print(f"Traducción incorrecta. La traducción correcta es:\n'{descripcion_en}'\n")
            # Opcional: permitir intentos adicionales o finalizar el juego
            print("Intentemos nuevamente.\n")
            self.solicitar_traduccion(descripcion_en)  # Recursividad para reintentar

    def equipar_objeto(self, args):
        if not args:
            print("¿Qué objeto quieres equipar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if not traduccion_objeto_esperada:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para equipar.\n")
            return
        traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
        if traduccion_usuario_objeto == traduccion_objeto_esperada:
            print("¡Traducción correcta!\n")
            # Proceder a equipar el objeto
            for categoria, objetos in self.inventario.items():
                for objeto in objetos:
                    if objeto.nombre.lower() == nombre_objeto_es:
                        objeto.equipar()
                        return
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")

    def desequipar_objeto(self, args):
        if not args:
            print("¿Qué objeto quieres desequipar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if not traduccion_objeto_esperada:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para desequipar.\n")
            return
        traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
        if traduccion_usuario_objeto == traduccion_objeto_esperada:
            print("¡Traducción correcta!\n")
            # Proceder a desequipar el objeto
            for categoria, objetos in self.inventario.items():
                for objeto in objetos:
                    if objeto.nombre.lower() == nombre_objeto_es:
                        objeto.desequipar()
                        return
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")

    def play(self):
        print("¡Bienvenido a 'Tomson en la Ciudad Salvaje'!")
        print("Eres Tomson, un sobreviviente que ha llegado a una ciudad post-apocalíptica.")
        print("Tu objetivo es sobrevivir, encontrar suministros y descubrir qué causó el colapso de la civilización.")
        print("Escribe 'ayuda' para ver los comandos disponibles.\n")
        self.mostrar_habitacion_actual()

        while not self.game_over:
            comando_usuario = input("> ").strip()
            if not comando_usuario:
                continue
            partes = comando_usuario.split()
            comando = partes[0].lower()
            args = partes[1:]

            # Solicitar traducción al inglés del comando
            self.traducir_comando(comando_usuario)

            accion = self.comandos.get(comando)
            if accion:
                accion(args)
                # Verificar condiciones para finalizar el juego
                if self.estado_juego == "after_collect_supplies" and any(
                        c.nombre == "Carlos" for c in self.habitacion_actual.personajes):
                    self.end_game()
            else:
                print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.\n")

    def mostrar_inventario_jugador(self, args=None):
        mostrar_inventario(self.inventario)

    def agarrar(self, args):
        if not args:
            print("¿Qué quieres agarrar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if traduccion_objeto_esperada:
            traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
            if traduccion_usuario_objeto == traduccion_objeto_esperada:
                print("¡Traducción correcta!\n")
            else:
                print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")
        else:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para agarrar.\n")
            return

        # Buscar el objeto en la habitación
        objeto_encontrado = None
        for objeto in self.habitacion_actual.objetos:
            if objeto.nombre.lower() == nombre_objeto_es:
                objeto_encontrado = objeto
                break
        if objeto_encontrado:
            agregar_objeto(self.inventario, objeto_encontrado)
            self.habitacion_actual.remover_objeto(objeto_encontrado)
        else:
            print(f"No ves '{nombre_objeto_es}' aquí.\n")

    def usar(self, args):
        if not args:
            print("¿Qué quieres usar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if traduccion_objeto_esperada:
            traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
            if traduccion_usuario_objeto == traduccion_objeto_esperada:
                print("¡Traducción correcta!\n")
            else:
                print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")
        else:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para usar.\n")
            return

        usar_objeto(self.inventario, nombre_objeto_es)

    def mover(self, args):
        if not args:
            print("¿A dónde quieres ir?\n")
            return
        direccion_es = args[0].lower()
        traduccion_direccion_esperada = self.traducciones_direcciones.get(direccion_es, None)
        if not traduccion_direccion_esperada:
            print(f"Dirección desconocida '{direccion_es}'.\n")
            return
        traduccion_usuario_direccion = input(f"Por favor, traduce la dirección '{direccion_es}': ").strip().lower()
        if traduccion_usuario_direccion == traduccion_direccion_esperada:
            print("¡Traducción correcta!\n")
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_direccion_esperada}'.\n")

        # Verificar si la dirección es válida
        if direccion_es in self.habitacion_actual.salidas:
            nombre_nueva_habitacion = self.habitacion_actual.salidas[direccion_es]
            self.habitacion_actual = self.habitaciones.get(nombre_nueva_habitacion)
            print(f"\nTe has movido hacia el {direccion_es}.\n")
            self.mostrar_habitacion_actual()
        else:
            print("No puedes ir en esa dirección desde aquí.\n")

    def hablar(self, args):
        if not args:
            print("¿Con quién quieres hablar?\n")
            return
        nombre_personaje_es = ' '.join(args).lower()
        # Opcional: agregar traducción de personajes si se desea
        # Para simplificar, asumimos que los nombres de personajes están en español y no requieren traducción
        # Puedes extender esto si los nombres tienen traducción al inglés

        nombre_personaje_traduccion = nombre_personaje_es  # Sin traducción por ahora
        # Buscar el personaje en la habitación
        personaje_encontrado = None
        for personaje in self.habitacion_actual.personajes:
            if personaje.nombre.lower() == nombre_personaje_traduccion:
                personaje_encontrado = personaje
                break
        if not personaje_encontrado:
            print(f"No hay a '{nombre_personaje_es}' aquí para hablar.\n")
            return

        # Solicitar traducción del nombre del personaje
        traduccion_usuario_personaje = input(
            f"Por favor, traduce el nombre del personaje '{nombre_personaje_es}': ").strip().lower()
        # Asumimos que los nombres de personajes no requieren traducción; pueden mantenerse iguales
        # Si deseas traducirlos, añade las traducciones en un diccionario similar a los comandos
        traduccion_personaje_esperada = nombre_personaje_es  # Sin traducción por ahora

        if traduccion_usuario_personaje == traduccion_personaje_esperada:
            print("¡Traducción correcta!\n")
        else:
            print(f"Traducción incorrecta. El nombre del personaje se mantiene como '{nombre_personaje_es}'.\n")

        # Hablar con el personaje
        dialogo = personaje_encontrado.hablar(self.estado_juego)
        print(f"\n{dialogo}\n")
        # Actualizar estado del juego basado en la conversación
        if personaje_encontrado.nombre == "Ana" and self.estado_juego == "usa_comida":
            print("Ana: ¡Gracias por compartir la comida! Ahora estamos más fuertes juntos.\n")
            self.estado_juego = "after_collect_supplies"

    def solicitar_traduccion(self, descripcion_en):
        """
        Solicita al usuario que traduzca la descripción al inglés y valida la traducción.

        :param descripcion_en: Descripción en inglés que el usuario debe reescribir.
        """
        print("Para continuar la aventura, por favor, reescribe la traducción al inglés de la descripción mostrada.")
        traduccion_usuario = input("Escribe la traducción aquí: ").strip().lower()
        traduccion_correcta = descripcion_en.lower()

        if traduccion_usuario == traduccion_correcta:
            print("¡Traducción correcta! Puedes continuar.\n")
        else:
            print(f"Traducción incorrecta. La traducción correcta es:\n'{descripcion_en}'\n")
            # Opcional: permitir intentos adicionales o finalizar el juego
            print("Intentemos nuevamente.\n")
            self.solicitar_traduccion(descripcion_en)  # Recursividad para reintentar

    def mostrar_habitacion_actual(self):
        print(f"\nEstás en la {self.habitacion_actual.nombre}.")
        print(f"Descripción en español: {self.habitacion_actual.descripcion_es}")
        print(f"Description in English: {self.habitacion_actual.descripcion_en}\n")

        # Solicitar al usuario que reescriba la traducción al inglés
        self.solicitar_traduccion(self.habitacion_actual.descripcion_en)

        if self.game_over:
            return  # Si el juego ha terminado durante la traducción

        # Mostrar personajes y objetos
        if self.habitacion_actual.personajes:
            for personaje in self.habitacion_actual.personajes:
                if personaje.activo:
                    print(f"Ves a {personaje.nombre}: {personaje.descripcion}")
        if self.habitacion_actual.objetos:
            print("Ves los siguientes objetos:")
            for objeto in self.habitacion_actual.objetos:
                print(f"- {objeto.nombre}")
        print(f"Salidas disponibles: {', '.join(self.habitacion_actual.salidas.keys())}\n")

        self.procesar_eventos()

    def procesar_eventos(self):
        for evento in self.habitacion_actual.eventos:
            if evento.trigger(self):
                print(f"*** Evento: {evento.descripcion} ***\n")
                evento.accion(self)

    def mostrar_ayuda(self, args=None):
        print("\nComandos disponibles:")
        print("ir [dirección] - Moverse a otra habitación (norte, sur, este, oeste, abajo)")
        print("agarrar [nombre del objeto] - Agarrar un objeto de la habitación")
        print("usar [nombre del objeto] - Usar un objeto de tu inventario")
        print("hablar [nombre] - Hablar con un personaje en la habitación")
        print("equipar [nombre del objeto] - Equipar un objeto de tu inventario")
        print("desequipar [nombre del objeto] - Desequipar un objeto de tu inventario")
        print("inventario - Mostrar tu inventario")
        print("guardar [nombre_archivo] - Guardar el juego")
        print("cargar [nombre_archivo] - Cargar una partida guardada")
        print("ayuda - Mostrar esta ayuda")
        print("salir - Salir del juego\n")

    def guardar_partida(self, args):
        if not args:
            print("¿Cómo quieres llamar al archivo de guardado?\n")
            return
        nombre_archivo = args[0] + ".json"
        estado_juego = {
            "habitacion_actual": self.habitacion_actual.nombre,
            "inventario": {
                categoria: [
                    {
                        "nombre": obj.nombre,
                        "categoria": obj.categoria,
                        "descripcion": obj.descripcion,
                        "uso": obj.uso,
                        "cantidad": obj.cantidad,
                        "equipado": obj.equipado
                    } for obj in objetos
                ] for categoria, objetos in self.inventario.items()
            },
            "estado_juego": self.estado_juego
        }
        try:
            with open(nombre_archivo, 'w') as archivo:
                json.dump(estado_juego, archivo, indent=4)
            print(f"Juego guardado en '{nombre_archivo}'.\n")
        except Exception as e:
            print(f"Error al guardar la partida: {e}\n")

    def cargar_partida(self, args):
        if not args:
            print("¿Qué archivo de guardado quieres cargar?\n")
            return
        nombre_archivo = args[0] + ".json"
        try:
            with open(nombre_archivo, 'r') as archivo:
                estado_juego = json.load(archivo)
            # Cargar habitación actual
            nombre_habitacion = estado_juego.get("habitacion_actual", "Plaza Central")
            self.habitacion_actual = self.habitaciones.get(nombre_habitacion, self.habitaciones["Plaza Central"])
            # Cargar inventario
            self.inventario = {}
            for categoria, objetos in estado_juego.get("inventario", {}).items():
                self.inventario[categoria] = []
                for obj_data in objetos:
                    objeto = Objeto(
                        nombre=obj_data["nombre"],
                        categoria=obj_data["categoria"],
                        descripcion=obj_data["descripcion"],
                        uso=obj_data["uso"],
                        cantidad=obj_data.get("cantidad", 1),
                        equipado=obj_data.get("equipado", False)
                    )
                    self.inventario[categoria].append(objeto)
            # Cargar estado del juego
            self.estado_juego = estado_juego.get("estado_juego", "inicio")
            print(f"Juego cargado desde '{nombre_archivo}'.\n")
            self.mostrar_habitacion_actual()
        except FileNotFoundError:
            print(f"No se encontró el archivo '{nombre_archivo}'.\n")
        except json.JSONDecodeError:
            print(f"El archivo '{nombre_archivo}' está corrupto o tiene un formato inválido.\n")
        except Exception as e:
            print(f"Error al cargar la partida: {e}\n")

    def salir_juego(self, args=None):
        print("¡Gracias por jugar! ¡Hasta la próxima!\n")
        sys.exit()

    def end_game(self):
        print(
            "¡Has completado tu misión y sobrevivido en la Ciudad Salvaje! Elysius está a salvo gracias a tu valentía y habilidades.")
        print("¡Felicidades! Has completado el juego.\n")
        self.game_over = True
        sys.exit()

    def equipar_objeto(self, args):
        if not args:
            print("¿Qué objeto quieres equipar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if not traduccion_objeto_esperada:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para equipar.\n")
            return
        traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
        if traduccion_usuario_objeto == traduccion_objeto_esperada:
            print("¡Traducción correcta!\n")
            # Proceder a equipar el objeto
            for categoria, objetos in self.inventario.items():
                for objeto in objetos:
                    if objeto.nombre.lower() == nombre_objeto_es:
                        objeto.equipar()
                        return
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")

    def desequipar_objeto(self, args):
        if not args:
            print("¿Qué objeto quieres desequipar?\n")
            return
        nombre_objeto_es = ' '.join(args).lower()
        traduccion_objeto_esperada = self.traducciones_objetos.get(nombre_objeto_es, None)
        if not traduccion_objeto_esperada:
            print(f"No se reconoce el objeto '{nombre_objeto_es}' para desequipar.\n")
            return
        traduccion_usuario_objeto = input(f"Por favor, traduce el objeto '{nombre_objeto_es}': ").strip().lower()
        if traduccion_usuario_objeto == traduccion_objeto_esperada:
            print("¡Traducción correcta!\n")
            # Proceder a desequipar el objeto
            for categoria, objetos in self.inventario.items():
                for objeto in objetos:
                    if objeto.nombre.lower() == nombre_objeto_es:
                        objeto.desequipar()
                        return
        else:
            print(f"Traducción incorrecta. La traducción correcta es '{traduccion_objeto_esperada}'.\n")
