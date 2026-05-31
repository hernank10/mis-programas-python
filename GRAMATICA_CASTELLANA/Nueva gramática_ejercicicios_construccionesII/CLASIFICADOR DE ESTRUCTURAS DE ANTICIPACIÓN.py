import re

class ClasificadorAnticipacion:
    def __init__(self):
        self.categorias = {
            1: {
                'nombre': 'Anticipación con adjetivo absoluto',
                'ejemplos': [
                    'Libros, tiene muchos',
                    'Café, tomó tres tazas',
                    'Problemas, resolvió algunos'
                ],
                'patron': r"^(\w+),\s*(\w+)\s+(muchos|pocos|varios|tres|una\s\w+|algunos|bastantes|demasiados)\b"
            },
            2: {
                'nombre': 'Anticipación con pronombre resuntivo',
                'ejemplos': [
                    'Amigos, los tiene en todos lados',
                    'Libros, los compra por internet',
                    'Problemas, los solucionó rápido'
                ],
                'patron': r"^(\w+),\s*(los|las|lo|la)\s+\w+"
            }
        }
    
    def mostrar_ejemplos(self, categoria):
        print(f"\n=== Ejemplos de {self.categorias[categoria]['nombre']} ===")
        for i, ejemplo in enumerate(self.categorias[categoria]['ejemplos'], 1):
            print(f"{i}. {ejemplo}")
    
    def analizar_oracion(self, oracion):
        oracion = oracion.strip().lower()
        resultados = {
            'categoria': 0,
            'detalles': {},
            'explicacion': ''
        }
        
        # Verificar categoría 1
        match = re.match(self.categorias[1]['patron'], oracion, re.IGNORECASE)
        if match:
            resultados['categoria'] = 1
            resultados['detalles'] = {
                'sustantivo': match.group(1).capitalize(),
                'verbo': match.group(2),
                'modificador': match.group(3)
            }
            resultados['explicacion'] = (f"ESTRUCTURA VÁLIDA\n"
                                      f"Sustantivo anticipado: {match.group(1).capitalize()}\n"
                                      f"Verbo: {match.group(2)}\n"
                                      f"Modificador: {match.group(3)}")
            return resultados
        
        # Verificar categoría 2
        match = re.match(self.categorias[2]['patron'], oracion, re.IGNORECASE)
        if match:
            resultados['categoria'] = 2
            resultados['detalles'] = {
                'sustantivo': match.group(1).capitalize(),
                'pronombre': match.group(2)
            }
            resultados['explicacion'] = (f"ESTRUCTURA VÁLIDA\n"
                                      f"Sustantivo anticipado: {match.group(1).capitalize()}\n"
                                      f"Pronombre de retomo: {match.group(2)}")
            return resultados
        
        resultados['explicacion'] = "ESTRUCTURA NO RECONOCIDA\nFormato requerido:\nCategoría 1: 'Sustantivo, verbo + modificador'\nCategoría 2: 'Sustantivo, pronombre + verbo'"
        return resultados

    def menu_principal(self):
        while True:
            print("\n=== CLASIFICADOR DE ESTRUCTURAS DE ANTICIPACIÓN ===")
            print("1. Ver ejemplos de Categoría 1")
            print("2. Ver ejemplos de Categoría 2")
            print("3. Analizar tu propia oración")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.mostrar_ejemplos(1)
                print("\nCaracterísticas principales:")
                print("- Sustantivo al inicio seguido de verbo y modificador")
                print("- No usa pronombres de retomo (lo, la, los, las)")
                print("- Ejemplo: 'Libros, tiene muchos'")
            
            elif opcion == '2':
                self.mostrar_ejemplos(2)
                print("\nCaracterísticas principales:")
                print("- Sustantivo al inicio seguido de pronombre")
                print("- El pronombre (lo/la/los/las) retoma al sustantivo")
                print("- Ejemplo: 'Problemas, los solucionó'")
            
            elif opcion == '3':
                entrada_usuario = input("\nEscribe una oración (ej: 'Libros, tiene muchos'): ")
                analisis = self.analizar_oracion(entrada_usuario)
                
                print("\n" + "="*50)
                if analisis['categoria'] != 0:
                    print(f"✅ PERTENECE A LA CATEGORÍA {analisis['categoria']}")
                    print(f"Tipo: {self.categorias[analisis['categoria']]['nombre']}")
                    print(analisis['explicacion'])
                else:
                    print("❌ NO CORRESPONDE A NINGUNA CATEGORÍA")
                    print(analisis['explicacion'])
                print("="*50)
            
            elif opcion == '4':
                print("¡Hasta luego! 👋")
                break
            
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    clasificador = ClasificadorAnticipacion()
    clasificador.menu_principal()
