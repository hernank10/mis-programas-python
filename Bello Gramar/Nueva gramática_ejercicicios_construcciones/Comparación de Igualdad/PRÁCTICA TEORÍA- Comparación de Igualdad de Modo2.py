import random
import time
import pyttsx3
import speech_recognition as sr

puntaje = 0
oraciones_usuario = []
nivel = 1

# Inicializa el motor de síntesis de voz
voz = pyttsx3.init()
voz.setProperty('rate', 150)

def decir(texto):
    print(f"🗣️ {texto}")
    voz.say(texto)
    voz.runAndWait()

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        decir("Habla ahora...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"🎤 Dijiste: {texto}")
            return texto
        except sr.UnknownValueError:
            print("❌ No entendí lo que dijiste.")
            return ""
        except sr.RequestError as e:
            print(f"❌ Error al conectar: {e}")
            return ""

# Preguntas por nivel
ejercicios = {
    1: [
        ("Lo encontré igual como lo dejé.", False, "‘igual como’ es vulgarismo. Debe usarse ‘igual que’ o ‘tal como’"),
        ("Tengo unas gafas igual que las tuyas.", True, "Correcto. ‘igual que’ es válido."),
    ],
    2: [
        ("Lo hice del mismo modo que tú.", True, "Correcto. Expresa igualdad de modo."),
        ("Tiene idéntico sombrero que yo.", False, "Incorrecto. Debe decirse ‘idéntico al mío’."),
    ]
}

def ejercicio_con_tiempo(nivel):
    global puntaje
    print(f"\n⏱️ EJERCICIO NIVEL {nivel} (Tienes 10 segundos por pregunta)")
    preguntas = ejercicios[nivel]
    random.shuffle(preguntas)

    for frase, correcta, explicacion in preguntas:
        print(f"\nFrase: {frase}")
        decir(frase)
        inicio = time.time()
        respuesta = input("¿Es correcta? (s/n): ").strip().lower()
        tiempo = time.time() - inicio

        if tiempo > 10:
            print("❌ Tiempo agotado!")
            decir("Tiempo agotado")
            continue

        if (respuesta == "s" and correcta) or (respuesta == "n" and not correcta):
            print("✅ ¡Correcto!")
            decir("Correcto")
            puntaje += 1
        else:
            print("❌ Incorrecto.")
            decir("Incorrecto")
        print(f"ℹ️ Explicación: {explicacion}")

    print(f"\n🔢 Puntaje hasta ahora: {puntaje}")

def escribir_oraciones():
    print("\n✍️ Escribe o dicta tus propias oraciones (máx. 50, 'salir' para terminar)")
    while len(oraciones_usuario) < 50:
        modo = input("¿Deseas escribir (e) o hablar (v)? ").strip().lower()
        if modo == 'v':
            oracion = reconocer_voz()
        else:
            oracion = input(f"Oración {len(oraciones_usuario)+1}: ")
        if oracion.lower() == 'salir':
            break
        elif oracion.strip():
            oraciones_usuario.append(oracion)
        else:
            print("⚠️ Oración vacía.")

    print(f"✅ Has guardado {len(oraciones_usuario)} oraciones.")

def exportar_oraciones():
    with open("oraciones_usuario.txt", "w", encoding="utf-8") as f:
        for oracion in oraciones_usuario:
            f.write(oracion + "\n")
    print("📁 Oraciones exportadas a 'oraciones_usuario.txt'")

def ver_oraciones():
    print("\n📄 ORACIONES GUARDADAS:")
    if oraciones_usuario:
        for i, oracion in enumerate(oraciones_usuario, 1):
            print(f"{i}. {oracion}")
    else:
        print("Aún no has escrito oraciones.")

def menu():
    global nivel
    while True:
        print(f"""
📚 MENÚ PRINCIPAL
Nivel actual: {nivel}
1. Realizar ejercicio con temporizador
2. Escribir o dictar oraciones
3. Ver oraciones guardadas
4. Exportar oraciones a .txt
5. Subir de nivel
6. Salir
        """)
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            ejercicio_con_tiempo(nivel)
        elif opcion == '2':
            escribir_oraciones()
        elif opcion == '3':
            ver_oraciones()
        elif opcion == '4':
            exportar_oraciones()
        elif opcion == '5':
            if nivel < max(ejercicios):
                nivel += 1
                print(f"🚀 Ahora estás en el nivel {nivel}")
            else:
                print("✅ Ya estás en el nivel más alto.")
        elif opcion == '6':
            decir("Gracias por usar el programa. Hasta pronto!")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu()
