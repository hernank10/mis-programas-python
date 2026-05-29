import json
import os

# Configuración inicial
EJERCICIOS_GUARDADOS = "ejercicios_guardados.json"
MAX_EJEMPLOS = 100

# Teoría resumida (basada en el ensayo)
TEORIA = """
=== TEORÍA SOBRE COMPUESTOS SINTAGMÁTICOS Y PREFIJADOS CON 'SIN' ===

1. **Componente átono**: Si el primer elemento no lleva acento prosódico, se escribe junto:
   - ✅ Correcto: mediocampo, sintecho, mediapunta.
   - ❌ Incorrecto: medio campo, sin techo, media punta.

2. **Prefijo 'sin-'**: Se escribe unido si forma una palabra con significado unitario:
   - ✅ Correcto: sinsabor, sinnúmero.
   - ❌ Incorrecto: sin sabor, sin número.

3. **Numerales**: Se escriben separados (excepto excepciones como setecientos):
   - ✅ Correcto: ocho mil, cincuenta y seis.
   - ❌ Incorrecto: ochomil, cincuentaiséis.

4. **Plurales**: 
   - Compuestos unidos: plural en el segundo elemento (centroderechas).
   - Con prefijo 'sin-': plural en el sustantivo (sintechos).
"""

# Base de ejercicios de completación
EJERCICIOS = [
    {
        "enunciado": "El jugador ocupa la posición de ______ (media punta/mediapunta).",
        "respuesta": "mediapunta",
        "explicacion": "'Mediapunta' es un sustantivo compuesto con primer componente átono. ✔️"
    },
    {
        "enunciado": "Muchos ______ (sin techo/sintecho) necesitan ayuda social.",
        "respuesta": "sintechos",
        "explicacion": "La RAE recomienda escribir 'sintecho' junto, pluralizando el segundo elemento. ✔️"
    },
    # ... (Añade más ejercicios aquí)
]

# Función para cargar/guardar ejercicios del usuario
def manejar_archivo(datos=None):
    if datos is None:
        if os.path.exists(EJERCICIOS_GUARDADOS):
            with open(EJERCICIOS_GUARDADOS, 'r') as f:
                return json.load(f)
        return []
    else:
        with open(EJERCICIOS_GUARDADOS, 'w') as f:
            json.dump(datos, f, indent=2)

# Función principal interactiva
def main():
    ejercicios_usuario = manejar_archivo()
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver teoría")
        print("2. Hacer ejercicios de completación")
        print("3. Guardar un ejemplo propio")
        print("4. Ver mis ejercicios guardados")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            print(TEORIA)
        
        elif opcion == "2":
            aciertos = 0
            for ejercicio in EJERCICIOS:
                print(f"\n▶ {ejercicio['enunciado']}")
                respuesta = input("Tu respuesta: ").strip().lower()
                
                if respuesta == ejercicio['respuesta']:
                    print(f"✅ Correcto! {ejercicio['explicacion']}")
                    aciertos +=1
                else:
                    print(f"❌ Incorrecto. La respuesta correcta es: '{ejercicio['respuesta']}'. {ejercicio['explicacion']}")
            
            print(f"\nResultado: {aciertos}/{len(EJERCICIOS)} aciertos.")
        
        elif opcion == "3":
            if len(ejercicios_usuario) >= MAX_EJEMPLOS:
                print("⚠️ Límite alcanzado (100 ejemplos guardados).")
                continue
            
            ejemplo = input("\nEscribe tu ejemplo (formato: '¿Se escribe X o Y?'): ")
            respuesta = input("Respuesta correcta: ").strip()
            explicacion = input("Explicación (norma RAE aplicada): ")
            
            ejercicios_usuario.append({
                "tipo": "user",
                "ejemplo": ejemplo,
                "respuesta": respuesta,
                "explicacion": explicacion
            })
            manejar_archivo(ejercicios_usuario)
            print("✔️ Ejemplo guardado exitosamente.")
        
        elif opcion == "4":
            print("\n=== TUS EJERCICIOS GUARDADOS ===")
            for idx, item in enumerate(ejercicios_usuario, 1):
                print(f"{idx}. {item['ejemplo']}")
                print(f"   Respuesta: {item['respuesta']}")
                print(f"   Explicación: {item['explicacion']}\n")
        
        elif opcion == "5":
            print("¡Hasta luego! ✨")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
