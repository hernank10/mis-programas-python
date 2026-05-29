import json
import os
import re
from collections import defaultdict

ARCHIVO_DATOS = "datos_gerundio_avanzado.json"

TEORIA = {
    # ... (mismo contenido teórico anterior)
}

EJERCICIOS = [
    {
        "tipo": "completacion",
        "verbo_tipo": "logro",
        "enunciado": "___ (terminar) el proyecto a tiempo, perdió el contrato",
        "opciones": ["Sin terminar", "No terminando"],
        "solucion": "Sin terminar",
        "explicacion": "Verbo de logro (terminar) requiere 'sin + infinitivo'",
        "dialecto": "estandar",
        "fallos": 0,
        "puntos": 10
    },
    {
        "tipo": "completacion",
        "verbo_tipo": "actividad",
        "enunciado": "Leyó el libro ___ (prestar) atención → [sin prestar/no prestando]",
        "opciones": ["sin prestar", "no prestando"],
        "solucion": "no prestando",
        "explicacion": "Acción simultánea negada (leer + no prestar atención)",
        "dialecto": "caribe",
        "fallos": 0,
        "puntos": 15
    },
    # +15 ejercicios adicionales...
]

class EstudioGerundioAvanzado:
    def __init__(self):
        self.datos_usuario = {
            'ejemplos': [],
            'puntuacion': 0,
            'nivel': 1,
            'historial_errores': defaultdict(int)
        }
        self.cargar_datos()
    
    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.datos_usuario = {
                    'ejemplos': datos.get('ejemplos', [])[:100],
                    'puntuacion': datos.get('puntuacion', 0),
                    'nivel': datos.get('nivel', 1),
                    'historial_errores': defaultdict(int, datos.get('historial_errores', {}))
                }
    
    def guardar_datos(self):
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump({
                'ejemplos': self.datos_usuario['ejemplos'],
                'puntuacion': self.datos_usuario['puntuacion'],
                'nivel': self.datos_usuario['nivel'],
                'historial_errores': dict(self.datos_usuario['historial_errores'])
            }, f, ensure_ascii=False, indent=2)
    
    def actualizar_nivel(self):
        niveles = {1: 0, 2: 100, 3: 300, 4: 600, 5: 1000}
        for nivel, puntos in sorted(niveles.items(), reverse=True):
            if self.datos_usuario['puntuacion'] >= puntos:
                self.datos_usuario['nivel'] = nivel
                break
    
    # ... (funciones anteriores mejoradas)
    
    def menu_principal(self):
        while True:
            print(f"\n=== MENÚ PRINCIPAL (Nivel {self.datos_usuario['nivel']} - Puntos: {self.datos_usuario['puntuacion']}) ===")
            print("1. Estudiar teoría")
            print("2. Ejercicios por tipo de verbo")
            print("3. Ejercicios dialectales")
            print("4. Autoevaluación libre")
            print("5. Análisis de errores")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                self.mostrar_teoria()
            elif opcion == '2':
                self.ejercicios_por_tipo()
            elif opcion == '3':
                self.ejercicios_dialectales()
            elif opcion == '4':
                self.modo_autoevaluacion()
            elif opcion == '5':
                self.analizar_errores()
            elif opcion == '6':
                self.guardar_datos()
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida")

    def ejercicios_por_tipo(self):
        tipos = {ej['verbo_tipo'] for ej in EJERCICIOS}
        print("\nTipos disponibles:", ", ".join(tipos))
        tipo_elegido = input("Elige un tipo de verbo: ").lower()
        
        ejercicios_filtrados = [ej for ej in EJERCICIOS if ej['verbo_tipo'] == tipo_elegido]
        self.procesar_ejercicios(ejercicios_filtrados)

    def ejercicios_dialectales(self):
        dialectos = {ej['dialecto'] for ej in EJERCICIOS if ej['dialecto'] != 'estandar'}
        print("\nDialectos disponibles:", ", ".join(dialectos))
        dialecto_elegido = input("Elige un dialecto: ").lower()
        
        ejercicios_filtrados = [ej for ej in EJERCICIOS if ej['dialecto'] == dialecto_elegido]
        self.procesar_ejercicios(ejercicios_filtrados)

    def procesar_ejercicios(self, ejercicios):
        for ejercicio in ejercicios:
            # Lógica de presentación y validación
            if respuesta_correcta:
                self.datos_usuario['puntuacion'] += ejercicio['puntos']
                self.actualizar_nivel()
            else:
                self.datos_usuario['historial_errores'][ejercicio['id']] += 1

    def analizar_errores(self):
        print("\n=== ANÁLISIS DE ERRORES ===")
        errores_ordenados = sorted(self.datos_usuario['historial_errores'].items(), 
                                 key=lambda x: x[1], reverse=True)[:5]
        
        for ejercicio_id, cantidad in errores_ordenados:
            ejercicio = next(ej for ej in EJERCICIOS if ej['id'] == ejercicio_id)
            print(f"\nEjercicio: {ejercicio['enunciado']}")
            print(f"Errores: {cantidad} - Dificultad: {ejercicio['dificultad']}")
            print(f"Explicación: {ejercicio['explicacion']}")

    def modo_autoevaluacion(self):
        print("\n=== MODO AUTOVALORACIÓN ===")
        print("Escribe oraciones libremente. El sistema analizará automáticamente:")
        print("Formato aceptado: [no + gerundio] o [sin + infinitivo]\n")
        
        while True:
            frase = input("\nEscribe tu frase (o 'salir'): ").strip()
            if frase.lower() == 'salir':
                break
            
            analisis = self.analizar_frase(frase)
            print(f"\nAnálisis: {analisis['resultado']}")
            print(f"Explicación: {analisis['explicacion']}")
            
            if analisis['valido'] and input("¿Guardar ejemplo? (s/n): ").lower() == 's':
                self.datos_usuario['ejemplos'].append(frase)
                self.guardar_datos()

    def analizar_frase(self, frase):
        patron_valido = r"\b(no\s+\w+ando|no\s+\w+iendo|sin\s+\w+ar|sin\s+\w+er|sin\s+\w+ir)\b"
        matches = re.findall(patron_valido, frase, flags=re.IGNORECASE)
        
        if not matches:
            return {
                'valido': False,
                'resultado': "❌ Estructura no detectada",
                'explicacion': "No se encontraron construcciones válidas de negación con gerundio"
            }
        
        # Análisis semántico básico
        explicaciones = []
        for construccion in matches:
            if 'no' in construccion:
                explicacion = "Estructura 'no + gerundio' detectada. Uso adecuado para acciones simultáneas negadas."
                if any(v in construccion for v in ['terminar', 'lograr', 'ganar']):
                    explicacion += " Posible error: verbos de logro suelen requerir 'sin + infinitivo'"
            else:
                explicacion = "Estructura 'sin + infinitivo' detectada. Uso adecuado para ausencia de acción."
        
        return {
            'valido': True,
            'resultado': "✅ Estructura válida detectada",
            'explicacion': "\n".join(explicaciones)
        }

if __name__ == "__main__":
    sistema = EstudioGerundioAvanzado()
    sistema.menu_principal()
