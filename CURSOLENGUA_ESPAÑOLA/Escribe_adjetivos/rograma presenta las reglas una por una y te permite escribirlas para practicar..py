# Programa para aprender las reglas de la flexión en castellano mediante la repetición

# Lista de reglas de flexión
reglas = [
    "Sustantivos terminados en -o generalmente son masculinos. Ejemplo: niño (masculino), libro (masculino).",
    "Sustantivos terminados en -a generalmente son femeninos. Ejemplo: niña (femenino), casa (femenino).",
    "Algunos sustantivos terminados en -a son masculinos y algunos terminados en -o son femeninos. Ejemplo: día (masculino), mano (femenino).",
    "Algunos sustantivos tienen la misma forma para ambos géneros y se distinguen por el artículo. Ejemplo: el artista (masculino), la artista (femenino).",
    "Sustantivos terminados en vocal añaden -s para formar el plural. Ejemplo: niño - niños, casa - casas.",
    "Sustantivos terminados en consonante añaden -es para formar el plural. Ejemplo: reloj - relojes, papel - papeles.",
    "Sustantivos terminados en -z cambian la -z a -c antes de añadir -es. Ejemplo: luz - luces, pez - peces.",
    "Algunos sustantivos no cambian en plural. Ejemplo: el lunes - los lunes.",
    "Adjetivos terminados en -o cambian a -a para el femenino. Ejemplo: niño alto - niña alta.",
    "Adjetivos terminados en -e o consonante generalmente no cambian en género. Ejemplo: niño inteligente - niña inteligente, niño feliz - niña feliz.",
    "Algunos adjetivos tienen formas específicas para cada género. Ejemplo: actor español - actriz española.",
    "Adjetivos terminados en vocal añaden -s para formar el plural. Ejemplo: niño alto - niños altos, niña alta - niñas altas.",
    "Adjetivos terminados en consonante añaden -es para formar el plural. Ejemplo: niño feliz - niños felices, niña feliz - niñas felices.",
    "Adjetivos terminados en -z cambian la -z a -c antes de añadir -es. Ejemplo: luz brillante - luces brillantes.",
    "Verbos de primera conjugación (-ar) en presente de indicativo: yo hablo, tú hablas, él/ella/usted habla, nosotros/nosotras hablamos, vosotros/vosotras habláis, ellos/ellas/ustedes hablan.",
    "Verbos de primera conjugación (-ar) en pretérito perfecto simple: yo hablé, tú hablaste, él/ella/usted habló, nosotros/nosotras hablamos, vosotros/vosotras hablasteis, ellos/ellas/ustedes hablaron.",
    "Verbos de segunda conjugación (-er) en presente de indicativo: yo como, tú comes, él/ella/usted come, nosotros/nosotras comemos, vosotros/vosotras coméis, ellos/ellas/ustedes comen.",
    "Verbos de segunda conjugación (-er) en pretérito perfecto simple: yo comí, tú comiste, él/ella/usted comió, nosotros/nosotras comimos, vosotros/vosotras comisteis, ellos/ellas/ustedes comieron.",
    "Verbos de tercera conjugación (-ir) en presente de indicativo: yo vivo, tú vives, él/ella/usted vive, nosotros/nosotras vivimos, vosotros/vosotras vivís, ellos/ellas/ustedes viven.",
    "Verbos de tercera conjugación (-ir) en pretérito perfecto simple: yo viví, tú viviste, él/ella/usted vivió, nosotros/nosotras vivimos, vosotros/vosotras vivisteis, ellos/ellas/ustedes vivieron.",
    "Algunos verbos cambian la vocal en la raíz en ciertas formas. Ejemplo: pensar (e > ie) - yo pienso, tú piensas.",
    "Algunos verbos añaden consonantes en ciertas formas. Ejemplo: conducir (c > zc) - yo conduzco.",
    "Algunos verbos tienen formas completamente irregulares. Ejemplo: ser - yo soy, tú eres."
]

def aprender_reglas():
    print("Aprende las reglas de la flexión en castellano mediante la repetición.\n")
    
    for i, regla in enumerate(reglas):
        print(f"Regla {i+1}: {regla}")
        input("Presiona Enter para continuar...\n")
        
        respuesta = input(f"Escribe la regla {i+1} de nuevo: ")
        
        if respuesta.strip() == regla.strip():
            print("¡Correcto! Has recordado bien la regla.\n")
        else:
            print(f"Incorrecto. La regla correcta es:\n{regla}\n")
            
        input("Presiona Enter para continuar con la siguiente regla...\n")

if __name__ == "__main__":
    aprender_reglas()
