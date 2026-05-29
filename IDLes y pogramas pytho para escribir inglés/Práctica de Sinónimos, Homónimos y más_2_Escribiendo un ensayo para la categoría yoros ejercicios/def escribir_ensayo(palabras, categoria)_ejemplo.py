def escribir_ensayo(palabras, categoria):
    print(f"\nEscribiendo un ensayo para la categoría {categoria}:")
    print("\n📌 Consejo: Usa al menos 5 palabras que hayas aprendido de esta categoría.")
    ensayo = input("Escribe un pequeño ensayo usando algunas de las palabras aprendidas: ")
    print("\nGracias por tu ensayo. Aquí está lo que escribiste:")
    print(ensayo)

    ver_ejemplo = input("\n¿Quieres ver un ejemplo de ensayo? (sí/no): ").strip().lower()
    if ver_ejemplo == "sí":
        ejemplos = {
            "Sinónimos": (
                "En mi casa siempre me siento alegre y contento cuando todos están reunidos. "
                "El ambiente es bello y hermoso, especialmente cuando mi madre prepara una comida "
                "rápida pero veloz para todos. Aunque a veces la tarea es difícil, intento no frustrarme "
                "y encontrar un método más complicado. Mi hermano me enseña y me instruye con paciencia."
            ),
            "Homónimos": (
                "Ayer vi una banda tocando en la plaza. Luego, mi primo se puso una banda en el brazo para entrenar. "
                "Me preguntó si la cura había pasado por el barrio, pero no entendí si hablaba de la cura de salud o del sacerdote."
            ),
            "Homófonas": (
                "Cuando fui al mar, observé cómo la ola golpeaba la orilla. Mi tío me contó la historia de una hola misteriosa "
                "que apareció escrita en una carta sin remitente. Mientras tanto, el viento soplaba con fuerza y escuché el ruido de la baca del coche, "
                "aunque mi prima creyó que hablaba de una vaca."
            ),
            "Isónimos": (
                "El médico recomendó al doctor una nueva técnica quirúrgica. La madre de Pedro, que también es una progenitora, escuchaba con atención. "
                "En el hospital, los niños o infantes juegan en la sala de espera, sin saber que son atendidos por un gran galeno."
            ),
            "Antónimos": (
                "En la vida hay momentos de alegría y de tristeza. A veces nos sentimos fuertes, otras veces débiles. "
                "Algunos prefieren el camino largo, otros el corto. Lo importante es no dejarse llevar por lo falso, "
                "sino buscar siempre lo verdadero."
            )
        }

        ejemplo = ejemplos.get(categoria, "Ejemplo no disponible para esta categoría.")
        print("\n📌 Ejemplo de ensayo:")
        print(ejemplo)
