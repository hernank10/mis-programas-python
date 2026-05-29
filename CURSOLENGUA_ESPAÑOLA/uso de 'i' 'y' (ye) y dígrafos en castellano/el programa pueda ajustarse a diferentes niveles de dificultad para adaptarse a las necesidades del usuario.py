import time

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.respuestas_correctas = 0
        self.respuestas_incorrectas = 0
        self.tiempo_total = 0
        self.historial = []

    def registrar_respuesta(self, correcta, tiempo):
        if correcta:
            self.respuestas_correctas += 1
        else:
            self.respuestas_incorrectas += 1
        self.tiempo_total += tiempo
        self.historial.append((correcta, tiempo))

    def mostrar_estadisticas(self):
        total_respuestas = self.respuestas_correctas + self.respuestas_incorrectas
        if total_respuestas == 0:
            print("No hay estadísticas disponibles.")
            return
        porcentaje_correctas = (self.respuestas_correctas / total_respuestas) * 100
        tiempo_promedio = self.tiempo_total / total_respuestas
        print(f"Estadísticas de {self.nombre}:")
        print(f"Respuestas correctas: {self.respuestas_correctas}")
        print(f"Respuestas incorrectas: {self.respuestas_incorrectas}")
        print(f"Porcentaje de aciertos: {porcentaje_correctas:.2f}%")
        print(f"Tiempo promedio por ejercicio: {tiempo_promedio:.2f} segundos")

# Ejemplo de uso
usuario = Usuario("Juan")
usuario.registrar_respuesta(True, 5)
usuario.registrar_respuesta(False, 7)
usuario.mostrar_estadisticas()
