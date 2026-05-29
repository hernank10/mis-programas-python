import random
import re

class GeneradorOraciones:
    def __init__(self):
        # Verbos regulares e irregulares comunes en español
        self.verbos = {
            'comer': {'presente': ['como', 'comes', 'come', 'comemos', 'coméis', 'comen']},
            'trabajar': {'presente': ['trabajo', 'trabajas', 'trabaja', 'trabajamos', 'trabajáis', 'trabajan']},
            'vivir': {'presente': ['vivo', 'vives', 'vive', 'vivimos', 'vivís', 'viven']},
            'amar': {'presente': ['amo', 'amas', 'ama', 'amamos', 'amáis', 'aman']},
            'correr': {'presente': ['corro', 'corres', 'corre', 'corremos', 'corréis', 'corren']}
        }
        
        self.conectores = [
            'pero', 'aunque', 'sin embargo', 'no obstante', 'mas'
        ]
        
        self.complementos = [
            'nos divertimos mucho', 'aprendí algo nuevo', 'lo pasamos bien',
            'obtuve buenos resultados', 'logramos nuestro objetivo', 'sigo intentándolo'
        ]

    def generar_oracion(self):
        verbo = random.choice(list(self.verbos.keys()))
        persona = random.choice([3, 4])  # 3: tercera persona singular, 4: primera plural
        conjugacion = self.verbos[verbo]['presente'][persona]
        conector = random.choice(self.conectores)
        complemento = random.choice(self.complementos)
        
        return f"{verbo.capitalize()} no {conjugacion}, {conector} {complemento}."

    def analizar_estructura(self, oracion):
        patron = r"^(\w+)(ar|er|ir)\b\s+no\s+\b\1\w*\b.*?(pero|aunque|sin embargo|no obstante|mas)\b"
        match = re.search(patron, oracion, re.IGNORECASE)
        
        if match:
            return {
                'verbo': match.group(1) + match.group(2),
                'negacion': match.group(0).split()[2],
                'conector': match.group(3),
                'valido': True
            }
        return {'valido': False}

    def menu(self):
        while True:
            print("\n=== Generador de Oraciones con Anticipación del Infinitivo ===")
            print("1. Generar oración aleatoria")
            print("2. Validar una oración")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                oracion = self.generar_oracion()
                print("\n🔠 Oración generada:")
                print(oracion)
                print("\n🔍 Estructura:")
                print(f"- Infinitivo: {oracion.split()[0].rstrip(',')}")
                print(f"- Verbo conjugado: {oracion.split()[2]}")
                print(f"- Conector: {oracion.split()[4].rstrip(',')}")
                
            elif opcion == '2':
                user_input = input("\nIngrese una oración para validar: ")
                analisis = self.analizar_estructura(user_input.lower())
                
                if analisis['valido']:
                    print("\n✅ Estructura válida detectada!")
                    print(f"Verbo: {analisis['verbo'].capitalize()}")
                    print(f"Negación: {analisis['negacion']}")
                    print(f"Conector: {analisis['conector'].capitalize()}")
                else:
                    print("\n❌ Estructura no válida o no reconocida")
                    
            elif opcion == '3':
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción no válida")

if __name__ == "__main__":
    generador = GeneradorOraciones()
    generador.menu()
