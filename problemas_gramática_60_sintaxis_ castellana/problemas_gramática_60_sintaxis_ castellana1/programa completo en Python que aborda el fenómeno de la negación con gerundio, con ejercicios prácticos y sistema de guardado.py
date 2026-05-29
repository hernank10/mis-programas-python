import json
import os
import re

ARCHIVO_DATOS = "datos_gerundio.json"

TEORIA = {
    "Introducción": {
        "descripción": "Alternancia entre <no + gerundio> y <sin + infinitivo>",
        "contenido": [
            "no + gerundio: negación de acción simultánea (Juan comía no masticando)",
            "sin + infinitivo: ausencia de acción previa (Aprobó sin estudiar)",
            "Restricciones: verbos de logro rechazan no + gerundio (*Terminó el proyecto no trabajando)"
        ]
    },
    "Diferencias semánticas": [
        "no + gerundio → acción simultánea negada",
        "sin + infinitivo → ausencia de acción necesaria",
        "RAE: no + gerundio implica 'negación activa'"
    ]
}

EJERCICIOS = [
    {
        "tipo": "completacion",
        "enunciado": "Aprobó el examen ___ (estudiar) → [sin estudiar/no estudiando]",
        "opciones": ["sin estudiar", "no estudiando"],
        "solucion": "sin estudiar",
        "explicacion": "Verbo de logro (aprobar) requiere 'sin + infinitivo'"
    },
    {
        "tipo": "completacion",
        "enunciado": "Caminaba ___ (mirar) el suelo → [sin mirar/no mirando]",
        "opciones": ["sin mirar", "no mirando"],
        "solucion": "no mirando",
        "explicacion": "Acción simultánea negada (caminar + no mirar)"
    },
    {
        "tipo": "correccion",
        "enunciado": "Corrige la frase: *Ganó el partido no entrenando",
        "solucion": "Ganó el partido sin entrenar",
        "explicacion": "Verbo de logro (ganar) no admite 'no + gerundio'"
    }
]

class EstudioGerundio:
    def __init__(self):
        self.ejemplos_usuario = []
        self.cargar_datos()
    
    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                self.ejemplos_usuario = json.load(f).get('ejemplos', [])[:100]
    
    def guardar_datos(self):
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump({'ejemplos': self.ejemplos_usuario}, f, ensure_ascii=False, indent=2)
    
    def mostrar_teoria(self):
        print("\n=== TEORÍA ===")
        for seccion, contenido in TEORIA.items():
            print(f"\n◆ {seccion}")
            if isinstance(contenido, dict):
                for k, v in contenido.items():
                    print(f"  ► {k}:")
                    for item in v if isinstance(v, list) else [v]:
                        print(f"    - {item}")
            else:
                for item in contenido:
                    print(f"  - {item}")
        print("\n")
    
    def validar_construccion(self, texto):
        patrones = [
            r"\bno\s+\w+ando\b",    # Gerundios -ar
            r"\bno\s+\w+iendo\b",   # Gerundios -er/-ir
            r"\bsin\s+\w+ar\b",     # Infinitivos -ar
            r"\bsin\s+\w+er\b",     # Infinitivos -er
            r"\bsin\s+\w+ir\b"      # Infinitivos -ir
        ]
        return any(re.search(p, texto.lower()) for p in patrones)
    
    def ejercicio_completacion(self):
        print("\n=== EJERCICIOS DE COMPLETACIÓN ===")
        aciertos = 0
        for ejercicio in filter(lambda x: x['tipo'] == 'completacion', EJERCICIOS):
            print(f"\nEjercicio: {ejercicio['enunciado']}")
            
            for i, opcion in enumerate(ejercicio['opciones'], 1):
                print(f"{i}. {opcion}")
            
            respuesta = input("Elige el número correcto: ").strip()
            try:
                indice = int(respuesta) - 1
                seleccion = ejercicio['opciones'][indice]
            except (ValueError, IndexError):
                seleccion = ""
            
            if seleccion == ejercicio['solucion']:
                aciertos += 1
                print(f"✅ Correcto! {ejercicio['explicacion']}")
            else:
                print(f"❌ Incorrecto. Solución: {ejercicio['solucion']}\n   Explicación: {ejercicio['explicacion']}")
        
        print(f"\nResultado final: {aciertos}/{len(EJERCICIOS)} correctos")
    
    def ejercicio_correccion(self):
        print("\n=== EJERCICIOS DE CORRECCIÓN ===")
        for ejercicio in filter(lambda x: x['tipo'] == 'correccion', EJERCICIOS):
            print(f"\nFrase a corregir: {ejercicio['enunciado']}")
            respuesta = input("Tu corrección: ").strip()
            
            if respuesta.lower() == ejercicio['solucion'].lower():
                print(f"✅ Perfecto! {ejercicio['explicacion']}")
            else:
                print(f"❌ Mejor solución: {ejercicio['solucion']}\n   Explicación: {ejercicio['explicacion']}")
    
    def ejercicio_redaccion(self):
        print("\n=== EJERCICIO DE REDACCIÓN ===")
        print("Escribe oraciones usando las construcciones estudiadas (máx 100). Escribe 'salir' para terminar.\n")
        
        while len(self.ejemplos_usuario) < 100:
            oracion = input("Tu oración: ").strip()
            if oracion.lower() == 'salir':
                break
            
            if self.validar_construccion(oracion):
                self.ejemplos_usuario.append(oracion)
                self.guardar_datos()
                print("✅ Ejemplo válido y guardado!")
            else:
                print("⚠️ Estructura no válida. Debe contener:\n   - 'no + gerundio' (ej: no mirando)\n   - 'sin + infinitivo' (ej: sin mirar)")
        
        print("\nTus mejores ejemplos:")
        for idx, ej in enumerate(self.ejemplos_usuario[-5:], 1):
            print(f"{idx}. {ej}")
    
    def menu_principal(self):
        while True:
            print("\n=== MENÚ PRINCIPAL ===")
            print("1. Estudiar teoría")
            print("2. Ejercicios de completación")
            print("3. Ejercicios de corrección")
            print("4. Ejercicio de redacción")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                self.mostrar_teoria()
            elif opcion == '2':
                self.ejercicio_completacion()
            elif opcion == '3':
                self.ejercicio_correccion()
            elif opcion == '4':
                self.ejercicio_redaccion()
            elif opcion == '5':
                self.guardar_datos()
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida")

if __name__ == "__main__":
    sistema = EstudioGerundio()
    sistema.menu_principal()
