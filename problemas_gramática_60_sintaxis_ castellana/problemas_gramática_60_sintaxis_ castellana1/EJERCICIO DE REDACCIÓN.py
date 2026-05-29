import json
import os
import time
import pygame

def iniciar_sonido():
    pygame.mixer.init()
    global sonido_correcto, sonido_incorrecto
    sonido_correcto = pygame.mixer.Sound("correcto.wav")
    sonido_incorrecto = pygame.mixer.Sound("incorrecto.wav")

def mostrar_teoria():
    teoria = """
    📖 === TEORÍA: COORDINACIÓN Y SUBORDINACIÓN ===
    Los siguientes verbos requieren complemento y pueden usarse con coordinación y subordinación:
    - 📢 Decir: "Juan dijo que vendría."
    - 📝 Explicar: "El profesor explicó cómo resolver el problema."
    - 💬 Comentar: "Ana comentó que viajaría el próximo mes."
    - 👍 Afirmar: "Pedro afirmó que todo estaba bien."
    - ❌ Negar: "Ella negó haber roto el vaso."
    - 🤞 Prometer: "Luis prometió que ayudaría con la tarea."
    """
    print(teoria)
    input("\nPresiona Enter para continuar...")

def ejercicio_completacion():
    print("\n🎯 === EJERCICIO DE COMPLETACIÓN ===")
    ejercicios = [
        ("María ____ que no tenía tiempo. 🕒", "dijo"),
        ("El profesor ____ cómo resolver la ecuación. ➗", "explicó"),
        ("Ana ____ que estaba emocionada por su viaje. ✈️", "comentó"),
        ("Pedro ____ que todo estaba en orden. ✅", "afirmó"),
        ("Ella ____ haber visto al ladrón. 🚔", "negó"),
        ("Luis ____ ayudar con la mudanza. 📦", "prometió")
    ]
    puntuacion = 0
    
    for i, (oracion, respuesta) in enumerate(ejercicios, 1):
        while True:
            user_resp = input(f"{i}. {oracion} ").strip().lower()
            if user_resp == respuesta:
                print("✅ ¡Correcto!")
                sonido_correcto.play()
                puntuacion += 10
                break
            else:
                print("❌ Incorrecto. Inténtalo de nuevo.")
                sonido_incorrecto.play()
                time.sleep(1)
    
    print(f"\n🏆 Puntuación final: {puntuacion}/{len(ejercicios) * 10}")

def guardar_ejemplo(user_text, file="ejemplos.json"):
    try:
        with open(file, "r") as f:
            ejemplos = json.load(f)
    except FileNotFoundError:
        ejemplos = []
    
    if len(ejemplos) < 100:
        ejemplos.append(user_text)
        with open(file, "w") as f:
            json.dump(ejemplos, f, indent=4)
        print("✅ Ejemplo guardado!")
    else:
        print("⚠️ Límite de 100 ejemplos alcanzado.")

def ejercicio_redaccion():
    print("\n✍️ === EJERCICIO DE REDACCIÓN ===")
    user_input = input("Escribe una oración usando uno de los verbos con coordinación o subordinación: ")
    guardar_ejemplo(user_input)

def menu():
    iniciar_sonido()
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("\n📚 === MENÚ ===")
        print("1️⃣ Ver teoría")
        print("2️⃣ Ejercicios de completación")
        print("3️⃣ Ejercicio de redacción")
        print("4️⃣ Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_teoria()
        elif opcion == "2":
            ejercicio_completacion()
        elif opcion == "3":
            ejercicio_redaccion()
        elif opcion == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
