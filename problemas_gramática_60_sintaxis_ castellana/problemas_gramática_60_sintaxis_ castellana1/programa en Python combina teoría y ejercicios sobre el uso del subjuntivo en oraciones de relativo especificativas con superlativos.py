class Teoria:
    def __init__(self):
        self.contenido = {
            "Uso del subjuntivo con superlativos": "El subjuntivo se emplea en oraciones de relativo especificativas cuando el antecedente está modificado por un superlativo. Esto ocurre porque el superlativo introduce un sentido de subjetividad o incertidumbre sobre la característica atribuida al antecedente.",
            "Ejemplo 1": "'Es el mejor profesor que haya tenido.' (Uso del subjuntivo para expresar una opinión subjetiva).",
            "Ejemplo 2": "'Es el mejor libro que he leído.' (Uso del indicativo cuando se afirma un hecho concreto)."
        }
    
    def mostrar_teoria(self):
        for tema, explicacion in self.contenido.items():
            print(f"{tema}: {explicacion}\n")

class Ejercicios:
    def __init__(self):
        self.ejercicios = [
            ("¿Cuál de las siguientes oraciones es gramatical?", [
                "Es el mejor artista que haya visto.",
                "Es el mejor artista que he visto."], 1),
            ("¿Por qué se usa el subjuntivo en 'Es la mejor película que haya existido'?", [
                "Porque el hablante expresa subjetividad.",
                "Porque es un hecho objetivo."], 0),
            ("¿Cuál es la diferencia entre 'Es el peor error que haya cometido' y 'Es el peor error que cometí' en términos de subjuntivo?", [
                "El primero enfatiza incertidumbre o subjetividad, el segundo es un hecho cierto.",
                "No hay diferencia."], 0)
        ]
        self.redaccion = [
            "Redacta una oración con un superlativo seguido de una oración de relativo con subjuntivo.",
            "Escribe una oración con un superlativo seguido de una oración de relativo con indicativo."
        ]
        self.ejemplos_guardados = {"Subjuntivo": [], "Indicativo": []}

    def realizar_ejercicios(self):
        puntaje = 0
        for i, (pregunta, opciones, respuesta_correcta) in enumerate(self.ejercicios, 1):
            print(f"{i}. {pregunta}")
            for j, opcion in enumerate(opciones, 1):
                print(f"   {j}. {opcion}")
            respuesta = int(input("Seleccione la opción correcta: "))
            if respuesta - 1 == respuesta_correcta:
                print("Correcto!\n")
                puntaje += 1
            else:
                print("Incorrecto. Explicación: "
                      "El subjuntivo se usa para expresar subjetividad o incertidumbre en relación con el superlativo.\n")
        print(f"Tu puntaje final es: {puntaje}/{len(self.ejercicios)}")
        
        print("\nEjercicios de redacción:")
        for ejercicio in self.redaccion:
            categoria = "Subjuntivo" if "subjuntivo" in ejercicio else "Indicativo"
            print(ejercicio)
            ejemplo = "Ejemplo: Es la mejor decisión que haya tomado." if categoria == "Subjuntivo" else "Ejemplo: Es la mejor decisión que tomé."
            print(ejemplo)
            oracion_usuario = input("Escribe tu oración: ")
            if len(self.ejemplos_guardados[categoria]) < 100:
                self.ejemplos_guardados[categoria].append(oracion_usuario)
                print("Oración guardada con éxito!\n")
            else:
                print("Has alcanzado el límite de 100 ejemplos guardados para esta categoría.\n")
        
        print("\nOraciones guardadas:")
        for categoria, oraciones in self.ejemplos_guardados.items():
            if oraciones:
                print(f"{categoria}:")
                for idx, oracion in enumerate(oraciones, 1):
                    print(f"  {idx}. {oracion}")

if __name__ == "__main__":
    print("Bienvenido al programa sobre el uso del subjuntivo con superlativos\n")
    teoria = Teoria()
    teoria.mostrar_teoria()
    input("Presiona Enter para continuar a los ejercicios...\n")
    ejercicios = Ejercicios()
    ejercicios.realizar_ejercicios()
