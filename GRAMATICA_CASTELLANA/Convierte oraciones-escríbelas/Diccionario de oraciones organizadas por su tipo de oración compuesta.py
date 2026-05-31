import random

# Diccionario de oraciones organizadas por su tipo de oración compuesta
oraciones = {
    "Yuxtapuestas": [
        "Llegué tarde, ya había comenzado la clase.",
        "El sol se ocultaba, las estrellas comenzaron a brillar.",
        "Llegué tarde, ya había comenzado la clase.",
        "El sol se ocultaba, las estrellas comenzaron a brillar.",
        "No dijo nada, simplemente se fue."
        "Juan estudia mucho, saca buenas notas.",
        "Fui al mercado, no había lo que buscaba.",
        "Escuché la noticia, me preocupé mucho.",
        "Está lloviendo, no podré salir.",
        "Caminé por la playa, recordé momentos felices.",
        "Los niños jugaban, los adultos conversaban.",
        "Te vi llegar, no quise interrumpir.",
],
    "Coordinadas Copulativas": [
        "Me gusta leer y escribir.",
        "María canta y baila en la fiesta.",
        "Estudié toda la tarde y después descansé.",
        "Pedro trabaja mucho y también estudia en la noche.",
        "La computadora es rápida y tiene buen almacenamiento.",
        "Juan corre todos los días y sigue una dieta saludable.",
        "El perro ladraba y el gato se escondía.",
        "Visitamos el museo y luego fuimos al cine.",
        "Carmen dibuja bien y le encanta pintar.",
        "Compramos frutas y verduras frescas en el mercado.",
    ],
    "Coordinadas Disyuntivas": [
        "Puedes venir a la fiesta o quedarte en casa.",
        "Juan llamará esta noche o nos verá mañana.",
        "Puedes venir a la fiesta o quedarte en casa.",
        "Juan llamará esta noche o nos verá mañana.",
        "O haces tu tarea o tendrás problemas con el profesor.",
        "Compra el libro hoy o espera hasta la próxima semana.",
        "O hablas ahora o callas para siempre.",
        "Iré al cine mañana o el domingo por la tarde.",
        "¿Prefieres comer pizza o pasta?",
        "Puedes elegir entre ir al parque o visitar el museo.",
        "O estudias para el examen o no podrás aprobar.",
        "Llama a tus amigos o mándales un mensaje.",
    ],
    "Coordinadas Adversativas": [
        "Juan estudió mucho, pero no aprobó el examen.",
        "Compramos entradas para el concierto, aunque ya no había buenos asientos.",
        "Juan estudió mucho, pero no aprobó el examen.",
        "Compramos entradas para el concierto, aunque ya no había buenos asientos.",
        "Me esforcé mucho en el proyecto, sin embargo, no obtuve el resultado esperado.",
        "Quería ir al cine, pero tenía demasiado trabajo.",
        "Comimos temprano, aunque no teníamos hambre.",
        "Estuvo cerca de ganar, pero falló en el último momento.",
        "Me invitaron a la fiesta, sin embargo, no pude asistir.",
        "Hace mucho frío, pero aún así salimos a caminar.",
        "Me ofrecieron el trabajo, aunque no estoy seguro de aceptarlo.",
        "Quise hablarle, pero me dio vergüenza.",
    ],
    "Coordinadas Distributivas": [
        "Ya estudias tú, ya estudio yo, siempre estamos ocupados.",
        "Bien vas tú, bien voy yo, no dejamos de trabajar.",
        "Ya estudias tú, ya estudio yo, siempre estamos ocupados.",
        "Bien vas tú, bien voy yo, no dejamos de trabajar.",
        "Unas veces se ríe, otras veces se enoja.",
        "Tan pronto habla él, tan pronto hablo yo.",
        "Unos días llueve, otros días sale el sol.",
        "Bien salimos de paseo, bien nos quedamos en casa.",
        "Unos piensan una cosa, otros piensan lo contrario.",
        "Ya gana uno, ya gana el otro, la competencia está reñida.",
        "Bien cocinamos en casa, bien salimos a cenar.",
        "Tan pronto acaba el trabajo, tan pronto comienza el descanso.",
    ],
    "Subordinadas Sustantivas": [
        "Quiero que vengas a la reunión.",
        "Me alegra que hayas aprobado el examen.",
        "Quiero que vengas a la reunión.",
        "Me alegra que hayas aprobado el examen.",
        "No sé si pueda asistir mañana."
        "Pienso que deberías descansar más.",
        "Me dijo que llegaría tarde.",
        "Creo que podemos resolver el problema juntos.",
        "Espero que todos estén de acuerdo.",
        "Dudo que lo puedan solucionar a tiempo.",
        "Me pidió que lo acompañara al evento.",
        "Sabía que el proyecto iba a ser exitoso.",
    ],
    "Subordinadas Adjetivas": [
        "El libro que leí es muy interesante.",
        "La casa donde crecí está en la ciudad.",
        "La casa donde crecí está en la ciudad.",
        "Las personas que asistieron a la conferencia fueron muchas.",
        "El auto que compré es de color rojo.",
        "La película que vimos anoche fue emocionante.",
        "Los amigos con los que viajé son muy divertidos.",
        "La canción que me gusta siempre suena en la radio.",
        "El profesor que enseña matemáticas es muy amable.",
        "La tienda donde compro ropa tiene buenas ofertas.",
        "El perro que encontramos en la calle es muy cariñoso.",...
    ],
    "Subordinadas Adverbiales": [
        "Cuando llegues a casa, avísame.",
        "Salimos de la oficina después de que terminamos el proyecto.",
        "Cuando llegues a casa, avísame.",
        "Salimos de la oficina después de que terminamos el proyecto.",
        "Me llamó mientras estaba en el tren.",
        "Aunque estaba cansado, siguió trabajando.",
        "Saldré a correr tan pronto como termine de llover.",
        "Haré la tarea antes de ir al cine.",
        "Como no encontré lo que buscaba, decidí ir a otra tienda.",
        "Me levantaré temprano para aprovechar el día.",
        "Mientras estudiaba, sonaba mi teléfono constantemente.",
        "Cuando termines, podemos salir a caminar.",
    ],
    "Subordinadas Causales": [
        "No fuimos al parque porque estaba lloviendo.",
        "Llegué tarde porque el tráfico estaba muy pesado.",
         "No fuimos al parque porque estaba lloviendo.",
        "Llegué tarde porque el tráfico estaba muy pesado.",
        "No pude asistir a la reunión debido a un compromiso previo.",
        "Ella está cansada porque ha trabajado todo el día.",
        "No salí a correr porque me dolía el pie.",
        "No compré el libro porque era muy caro.",
        "No fui a la fiesta porque tenía un examen al día siguiente.",
        "No dormí bien porque hubo mucho ruido en la calle.",
        "Está feliz porque ganó el concurso.",
        "No salimos a tiempo porque el coche no arrancaba.",
    ],
    "Subordinadas Condicionales": [
        "Si estudias, aprobarás el examen.",
        "Si tienes tiempo, llámame por la tarde.",
        "Si estudias, aprobarás el examen.",
        "Si tienes tiempo, llámame por la tarde.",
        "Si no llueve, podemos ir al parque.",
        "Si me ayudas, terminaremos más rápido.",
        "Si quieres, podemos cenar juntos esta noche.",
        "Si no llegas a tiempo, perderás el tren.",
        "Si te sientes mal, avísame de inmediato."
        "Si hubiera sabido, habría ido contigo.",
        "Si no encuentras el libro, te lo presto.",
        "Si sigues así, lograrás tus metas.",
    ]
}

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú de Clasificación de Oraciones Compuestas ---")
    for idx, tipo in enumerate(oraciones.keys(), 1):
        print(f"{idx}. {tipo}")
    print("0. Salir")

# Función principal del programa
def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("\nElige un tipo de oración (ingresa el número): ")

        if opcion == '0':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            try:
                # Convertir opción a índice válido
                tipo_oracion = list(oraciones.keys())[int(opcion) - 1]
                oracion_elegida = random.choice(oraciones[tipo_oracion])

                print(f"\n--- Tipo de oración: {tipo_oracion} ---")
                print(f"Oración: {oracion_elegida}")
                
                # Pedir al usuario que repita la oración
                oracion_usuario = input("\nEscribe la oración nuevamente: ")

                # Verificar si la oración fue escrita correctamente
                if oracion_usuario == oracion_elegida:
                    print("¡Correcto! Escribiste la oración correctamente.")
                else:
                    print(f"Incorrecto. La oración correcta es: {oracion_elegida}")
                
                # Preguntar si el usuario quiere repetir
                repetir = input("\n¿Quieres intentarlo de nuevo? (s/n): ")
                if repetir.lower() != 's':
                    break

            except (ValueError, IndexError):
                print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
ejecutar_programa()

