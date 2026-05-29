import json
from collections import defaultdict

class DerivacionVerbal:
    def __init__(self):
        self.patrones = {
            'sufijos_comunes': ['-ar', '-ear', '-ecer', '-izar', '-ificar'],
            'parasintesis': ['a-...-ar', 'en-...-ar', 'des-...-ar'],
            'interfijos': ['-ec-', '-ific-', '-iz-']
        }
        
        self.ejemplos = {
            '-ear': ['canturrear', 'matear', 'patear'],
            '-izar': ['argentinizar', 'computerizar'],
            'a-N-ar': ['abotonar', 'aterrizar'],
            'en-A-ecer': ['entristecer', 'enriquecer']
        }
        
        self.variantes = {
            'diacronicas': {
                'enriquir': 'enriquecer',
                'atristar': 'entristecer'
            },
            'diatopicas': {
                'concientizar': ['América'],
                'liderizar': ['Región Andina']
            }
        }
        
        self.verbos_guardados = defaultdict(dict)
        
    def identificar_bases(self, verbo):
        """Analiza un verbo para sugerir posibles bases y afijos"""
        resultados = []
        for sufijo in self.patrones['sufijos_comunes']:
            if verbo.endswith(sufijo.replace('-', '')):
                base = verbo[:-len(sufijo.replace('-', ''))]
                resultados.append((base, sufijo))
        return resultados

    def analizar_patron(self, verbo):
        """Identifica patrones productivos"""
        analisis = []
        # Verificar parasíntesis
        for prefijo in ['a', 'en', 'des']:
            for sufijo in ['ar', 'ecer']:
                if verbo.startswith(prefijo) and verbo.endswith(sufijo):
                    radical = verbo[len(prefijo):-len(sufijo)]
                    analisis.append(f"{prefijo}-{radical}-{sufijo}")
        
        # Comparar con ejemplos conocidos
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                analisis.append(f"Patrón conocido: {patron}")
        
        return analisis if analisis else ["No se identificó patrón claro"]

    def verificar_variacion(self, verbo):
        """Busca variantes diatópicas o diacrónicas"""
        resultados = []
        if verbo in self.variantes['diacronicas']:
            resultados.append(f"Variante histórica: {self.variantes['diacronicas'][verbo]}")
        if verbo in self.variantes['diatopicas']:
            regiones = ', '.join(self.variantes['diatopicas'][verbo])
            resultados.append(f"Uso regional: {regiones}")
        return resultados

    def agregar_ejemplo(self, verbo, patron, region=None):
        """Permite añadir nuevos ejemplos y variantes"""
        if patron not in self.ejemplos:
            self.ejemplos[patron] = []
        self.ejemplos[patron].append(verbo)
        
        if region:
            self.variantes['diatopicas'][verbo] = [region]
        
        print(f"¡Ejemplo {verbo} añadido al patrón {patron}!")

    def generar_informe(self, verbo):
        """Genera un reporte completo"""
        print(f"\n🔍 Análisis de: {verbo}")
        
        print("\n1. Bases y afijos:")
        bases = self.identificar_bases(verbo)
        for base, sufijo in bases:
            print(f" - Posible base: {base} | Sufijo: {sufijo}")
        
        print("\n2. Patrones detectados:")
        for patron in self.analizar_patron(verbo):
            print(f" - {patron}")
        
        print("\n3. Variación:")
        variantes = self.verificar_variacion(verbo)
        if variantes:
            for v in variantes:
                print(f" - {v}")
        else:
            print(" - No se registran variantes")
        
        print("\n4. Ejemplos relacionados:")
        for patron, ejemplos in self.ejemplos.items():
            if verbo in ejemplos:
                print(f" - Ejemplo prototípico de {patron}:")
                print(f"   {', '.join(ejemplos[:3])}...")

    def guardar_datos(self, archivo='datos_verbos.json'):
        """Guarda los datos en un archivo JSON"""
        datos = {
            'ejemplos': self.ejemplos,
            'variantes': self.variantes
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def cargar_datos(self, archivo='datos_verbos.json'):
        """Carga datos desde un archivo JSON"""
        try:
            with open(archivo) as f:
                datos = json.load(f)
            self.ejemplos = datos['ejemplos']
            self.variantes = datos['variantes']
        except FileNotFoundError:
            print("¡Archivo no encontrado, empezando con datos base!")

def menu_principal():
    herramienta = DerivacionVerbal()
    herramienta.cargar_datos()
    
    while True:
        print("\n" + "="*50)
        print(" HERRAMIENTA DE ANÁLISIS DE DERIVACIÓN VERBAL")
        print("="*50)
        print("1. Analizar un verbo")
        print("2. Agregar nuevo ejemplo")
        print("3. Guardar datos")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            verbo = input("Ingrese un verbo: ").lower().strip()
            herramienta.generar_informe(verbo)
        
        elif opcion == '2':
            verbo = input("Verbo a agregar: ").lower().strip()
            patron = input("Patrón (ej: -ear, a-N-ar): ").strip()
            region = input("Región (opcional): ").strip() or None
            herramienta.agregar_ejemplo(verbo, patron, region)
        
        elif opcion == '3':
            herramienta.guardar_datos()
            print("Datos guardados exitosamente!")
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_principal()
