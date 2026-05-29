class Teoria:
    def __init__(self):
        self.contenido = {
            "Percepción no epistémica": "Se refiere a la percepción directa de eventos dinámicos y físicamente observables.",
            "Percepción epistémica": "Expresa una inferencia basada en la percepción, no un evento directamente observable.",
            "Predicados estativos": "Son aquellos que describen estados y no pueden usarse con verbos de percepción en infinitivo."
        }

    def mostrar_teoria(self):
        for tema, explicacion in self.contenido.items():
            print(f"{tema}: {explicacion}\n")

class Ejercicios:
    def __init__(self):
        self.ejercicios = [
            ("¿Cuál de las siguientes oraciones es gramatical?", [
                "Juan vio estar nerviosa a María.",
                "Juan vio que María estaba nerviosa."], 1),
            ("¿Qué tipo de percepción se usa en 'Juan oyó cantar a Pedro'?", [
                "Percepción epistémica", "Percepción no epistémica"], 1),
            ("¿Cuál es un ejemplo de predicado estativo?", [
                "Correr", "Estar feliz"], 1)
        ]
        self.oraciones_incompletas = [
            "Juan ___ que Pedro estaba cansado.",
            "María ___ ver a su amigo saltar la cuerda.",
            "Nosotros ___ que el coche estaba en el garaje."
        ]
        self.redaccion = [
            "Redacta una oración utilizando un verbo de percepción no epistémica.",
            "Escribe una oración con un verbo de percepción epistémica.",
            "Crea una oración con un predicado estativo."
        ]

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
                print("Incorrecto.\n")
        print(f"Tu puntaje final es: {puntaje}/{len(self.ejercicios)}")
        
        print("\nCompleta las siguientes oraciones:")
        for oracion in self.oraciones_incompletas:
            print(oracion)
            input("Tu respuesta: ")
        
        print("\nEjercicios de redacción:")
        for ejercicio in self.redaccion:
            print(ejercicio)
            input("Escribe tu oración: ")

if __name__ == "__main__":
    print("Bienvenido al programa sobre percepción y predicados estativos\n")
    teoria = Teoria()
    teoria.mostrar_teoria()
    input("Presiona Enter para continuar a los ejercicios...\n")
    ejercicios = Ejercicios()
    ejercicios.realizar_ejercicios()
