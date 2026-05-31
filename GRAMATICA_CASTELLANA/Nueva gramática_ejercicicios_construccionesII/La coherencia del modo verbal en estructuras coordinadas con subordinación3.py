# === Diccionario simple de verbos principales y modo requerido ===
modo_por_verbo = {
    "creo": "indicativo",
    "sé": "indicativo",
    "afirmo": "indicativo",
    "pienso": "indicativo",
    "deseo": "subjuntivo",
    "quiero": "subjuntivo",
    "espero": "subjuntivo",
    "pido": "subjuntivo",
    "prefiero": "subjuntivo",
    "ojalá": "subjuntivo"
}

# === Verbos comunes en subjuntivo para comparación (forma simplificada) ===
formas_subjuntivo = ["venga", "llegue", "respetes", "tenga", "pueda", "sepa", "haya", "esté", "haya sido", "hubiera", "viniera"]
formas_indicativo = ["viene", "llega", "respetas", "tiene", "puede", "sabe", "ha", "está", "fue", "hubo", "vendrá", "llegará", "respetará"]

def analizar_modo_verbal(oracion):
    print("\n🔍 Análisis gramatical:")
    encontrada = False
    for verbo_principal in modo_por_verbo:
        if verbo_principal in oracion.lower():
            modo_esperado = modo_por_verbo[verbo_principal]
            print(f"→ Verbo principal: '{verbo_principal}' → requiere {modo_esperado}")
            encontrada = True

            if modo_esperado == "subjuntivo":
                if any(forma in oracion for forma in formas_indicativo):
                    print("⚠️ Se ha usado un verbo en indicativo cuando se esperaba subjuntivo.")
                elif any(forma in oracion for forma in formas_subjuntivo):
                    print("✅ Correcto: el modo verbal es subjuntivo.")
                else:
                    print("❓ No se pudo identificar claramente el modo del verbo subordinado.")
            elif modo_esperado == "indicativo":
                if any(forma in oracion for forma in formas_subjuntivo):
                    print("⚠️ Se ha usado un verbo en subjuntivo cuando se esperaba indicativo.")
                elif any(forma in oracion for forma in formas_indicativo):
                    print("✅ Correcto: el modo verbal es indicativo.")
                else:
                    print("❓ No se pudo identificar claramente el modo del verbo subordinado.")
            break

    if not encontrada:
        print("🤔 No se identificó un verbo principal conocido. Intenta con 'creo', 'deseo', 'pido', etc.")

# === Integrar en menú principal ===
def modo_analisis_manual():
    print("\n=== ANÁLISIS DEL MODO VERBAL ===")
    oracion = input("Escribe una oración compuesta para analizar su corrección gramatical:\n>> ")
    analizar_modo_verbal(oracion)
