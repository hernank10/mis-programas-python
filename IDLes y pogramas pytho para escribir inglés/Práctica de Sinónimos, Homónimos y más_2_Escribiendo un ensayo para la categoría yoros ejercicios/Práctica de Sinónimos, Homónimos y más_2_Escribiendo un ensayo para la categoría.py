import os

def escribir_ensayo(palabras, categoria):
    print(f"\n📝 Escribiendo un ensayo para la categoría: {categoria}")
    print("📌 Consejo: Usa al menos 5 palabras aprendidas de esta categoría en tu redacción.\n")

    ensayo = input("Escribe tu ensayo aquí:\n> ").strip()
    ensayo_palabras = ensayo.lower().split()

    # Verificar cuántas palabras aprendidas están en el ensayo
    coincidencias = [palabra for palabra in palabras if palabra.lower() in ensayo_palabras]
    cantidad = len(coincidencias)

    print(f"\n🔍 Palabras encontradas del conjunto aprendido: {cantidad}")
    if cantidad >= 5:
        print("✅ ¡Bien hecho! Has usado al menos 5 palabras aprendidas.")
    else:
        print("❌ Aún no usaste 5 palabras del conjunto. Intenta usar más.")

    # Guardar el ensayo en un archivo
    carpeta = "ensayos_guardados"
    os.makedirs(carpeta, exist_ok=True)
    nombre_archivo = f"{carpeta}/ensayo_{categoria.lower()}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Categoría: {categoria}\n")
        f.write("Palabras aprendidas: " + ", ".join(palabras) + "\n")
        f.write("Ensayo del usuario:\n" + ensayo + "\n")
        f.write(f"\nPalabras coincididas: {cantidad}\n")
        f.write("Resultado: " + ("Correcto" if cantidad >= 5 else "Incompleto") + "\n")

    print(f"💾 Ensayo guardado en: {nombre_archivo}")

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
