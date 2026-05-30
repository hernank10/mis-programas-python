import random

# Lista de ejemplos y reglas del uso de la letra H
reglas = {
    "Palabras que empiezan por los diptongos hie-, hue-, hui-": ["hierba", "huevo", "huir"],
    "Palabras que empiezan por hecto-": ["hectárea", "hectolitro"],
    "Palabras que empiezan por helio-": ["helio", "heliógrafo"],
    "Palabras que empiezan por hetero-": ["heterogéneo", "heterosexual"],
    "Palabras que empiezan por hexa-": ["hexágono", "hexaedro"],
    "Palabras que empiezan por hidro-": ["hidratación", "hidráulico"],
    "Palabras que empiezan por hiper-": ["hiperactivo", "hipérbole"],
    "Palabras que empiezan por hipo-": ["hipopótamo", "hipotermia"],
    "Palabras que empiezan por homo-": ["homólogo", "homófono"],
    "Palabras que empiezan por hospital-": ["hospital", "hospitalidad"],
    "Palabras que empiezan por hotel-": ["hotel", "hotelero"],
    "Formas de los verbos cuyo infinitivo se escribe con h (haber)": ["he", "has", "ha", "hemos", "habéis", "han"],
    "Formas de los verbos cuyo infinitivo se escribe con h (hacer)": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
    "Palabras que empiezan por hidr-": ["hidratante", "hidrógeno"],
    "Palabras que empiezan por higr-": ["higrómetro", "higroscópico"],
    "Palabras que empiezan por hig-": ["higiene", "higiénico"],
    "Palabras que empiezan por hist-": ["historia", "historial"],
    "Palabras que empiezan por holg-": ["holgazán", "holgura"],
    "Palabras que empiezan por horm-": ["hormiga", "hormonal"],
    "Palabras que empiezan por horr-": ["horrible", "horrorizar"],
    "Palabras que empiezan por hosp-": ["hospedar", "hospedaje"],
    "Palabras que empiezan por host-": ["hostal", "hostilidad"],
    "Palabras que empiezan por herm-": ["hermano", "hermético"],
    "Palabras que empiezan por hern-": ["hernia", "hernioplastia"],
    "Palabras que empiezan por hermo-": ["hermosura", "hermoso"],
    "Palabras que empiezan por herni-": ["herniación", "herniología"],
    "Palabras que empiezan por hem-": ["hemorragia", "hemoglobina"],
    "Palabras que empiezan por hemi-": ["hemisferio", "hemiplegia"],
    "Palabras que empiezan por hum-": ["humano", "humedad"],
    "Palabras que empiezan por hues-": ["hueso", "huesudo"],
    "Interjecciones y palabras onomatopéyicas": ["¡Hola!", "¡Huy!"]
}

def repasar_reglas():
    while True:
        # Seleccionar una regla aleatoria
        regla, ejemplos = random.choice(list(reglas.items()))
        
        print(f"\nRegla: {regla}")
        print(f"Ejemplos: {', '.join(ejemplos)}")
        
        respuesta = input("Escribe una palabra o frase relacionada con esta regla (o 'salir' para terminar): ").strip()
        
        if respuesta.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if respuesta in ejemplos:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. Ejemplos correctos son: {', '.join(ejemplos)}")

if __name__ == "__main__":
    repasar_reglas()
