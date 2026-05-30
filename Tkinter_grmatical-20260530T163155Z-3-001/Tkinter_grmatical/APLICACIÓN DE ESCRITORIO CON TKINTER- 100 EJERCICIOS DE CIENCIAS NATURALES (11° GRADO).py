# ==============================================================================
# APLICACIÓN DE ESCRITORIO CON TKINTER: 100 EJERCICIOS DE CIENCIAS NATURALES (11° GRADO)
# ==============================================================================
# Este script crea una aplicación de escritorio con una interfaz gráfica (GUI)
# usando la librería Tkinter. Presenta 100 ejercicios de ciencias naturales y
# permite al usuario escribir una paráfrasis para cada uno.
#
# Las paráfrasis se almacenan y se pueden guardar en un archivo de texto al
# finalizar todos los ejercicios.
# ==============================================================================

import tkinter as tk
from tkinter import scrolledtext, messagebox, font

class CienciasApp(tk.Tk):
    """
    Clase principal para la aplicación de 100 ejercicios de ciencias naturales.
    Hereda de tk.Tk para ser la ventana principal.
    """
    def __init__(self):
        super().__init__()
        self.title("Ejercicios de Ciencias Naturales (11° Grado)")
        self.geometry("800x600")
        self.configure(bg="#F0F0F0")

        # Configuración de fuentes
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.content_font = font.Font(family="Helvetica", size=12)
        self.paraphrase_font = font.Font(family="Helvetica", size=11, slant="italic")

        # Variables de estado
        self.ejercicios_completados = 0
        self.parafra-sis_guardadas = []

        # --- Contenido de los ejercicios (los mismos 100 ejercicios del script de consola) ---
        self.ejercicios = [
            # SECCIÓN 1: QUÍMICA - CINÉTICA, EQUILIBRIO Y TERMODINÁMICA
            {"titulo": "1. Cinética Química", "contenido": "La cinética química estudia la velocidad de las reacciones y los factores que la afectan (temperatura, concentración, catalizadores)."},
            {"titulo": "2. Efecto de la Temperatura", "contenido": "A mayor temperatura, las partículas se mueven más rápido, chocan con más energía y la reacción ocurre más rápido."},
            {"titulo": "3. Teoría de las Colisiones", "contenido": "Para que una reacción ocurra, las moléculas deben chocar con la orientación y energía adecuadas."},
            {"titulo": "4. Rol de un Catalizador", "contenido": "Un catalizador es una sustancia que acelera una reacción sin consumirse. Las enzimas son catalizadores biológicos."},
            {"titulo": "5. Energía de Activación", "contenido": "Es la energía mínima necesaria para que una reacción ocurra. Un catalizador la reduce, haciendo la reacción más fácil."},
            {"titulo": "6. Reacción Reversible", "contenido": "En una reacción reversible, los reactivos se convierten en productos y los productos pueden volver a convertirse en reactivos."},
            {"titulo": "7. Equilibrio Químico", "contenido": "En el equilibrio químico, la velocidad de la reacción hacia adelante es igual a la velocidad de la reacción hacia atrás."},
            {"titulo": "8. Principio de Le Châtelier", "contenido": "Si alteras un sistema en equilibrio (agregando reactivos), el sistema se ajustará para contrarrestar el cambio."},
            {"titulo": "9. Entalpía de una Reacción", "contenido": "La entalpía es el calor que se absorbe (endotérmica) o se libera (exotérmica) en una reacción química."},
            {"titulo": "10. Reacción Exotérmica", "contenido": "En una reacción exotérmica, la energía de los productos es menor que la de los reactivos, liberando calor."},
            {"titulo": "11. Reacción Endotérmica", "contenido": "En una reacción endotérmica, la energía de los productos es mayor que la de los reactivos, absorbiendo calor del entorno."},
            {"titulo": "12. Entropía", "contenido": "La entropía es la medida del desorden en un sistema. Los procesos naturales tienden a un mayor desorden."},
            {"titulo": "13. Energía Libre de Gibbs", "contenido": "Determina si una reacción puede ocurrir de forma espontánea, considerando la entalpía y la entropía."},
            {"titulo": "14. Oxidación", "contenido": "La oxidación es la pérdida de electrones. Cuando un clavo de hierro se oxida, el hierro pierde electrones."},
            {"titulo": "15. Reducción", "contenido": "La reducción es la ganancia de electrones. La oxidación y la reducción siempre ocurren juntas."},
            {"titulo": "16. Celda Galvánica", "contenido": "Una celda galvánica convierte la energía química de una reacción espontánea en energía eléctrica. Así funcionan las baterías."},
            {"titulo": "17. Celda Electrolítica", "contenido": "Una celda electrolítica usa energía eléctrica para forzar una reacción química no espontánea."},
            {"titulo": "18. Potencial de Reducción", "contenido": "Es una medida de la tendencia de una sustancia a ganar electrones. Las sustancias con alto potencial se reducen fácilmente."},
            {"titulo": "19. pH de una Solución", "contenido": "El pH mide la acidez o basicidad de una solución. El agua pura tiene un pH de 7 (neutro)."},
            {"titulo": "20. Ácidos y Bases Fuertes", "contenido": "Un ácido o base fuerte se disocia completamente en agua."},
            {"titulo": "21. Indicador de pH", "contenido": "Un indicador de pH cambia de color según la acidez de la solución."},
            {"titulo": "22. Efecto de la Concentración", "contenido": "Si aumentas la concentración de un reactivo en equilibrio, la reacción se moverá hacia los productos."},
            {"titulo": "23. Disolución Espontánea", "contenido": "Cuando agregas sal al agua, las moléculas se mezclan de forma espontánea, aumentando la entropía."},
            {"titulo": "24. Ley de Faraday", "contenido": "La cantidad de sustancia producida en la electrólisis es directamente proporcional a la cantidad de electricidad."},
            {"titulo": "25. Corrosión", "contenido": "La corrosión es un proceso electroquímico donde el metal se oxida. Se puede prevenir con protección catódica."},

            # SECCIÓN 2: FÍSICA - FENÓMENOS ONDULATORIOS Y FLUIDOS
            {"titulo": "26. Onda y Tipos", "contenido": "Una onda es una perturbación que se propaga. Hay ondas mecánicas (sonido) y electromagnéticas (luz)."},
            {"titulo": "27. Partes de una Onda", "contenido": "Una onda tiene cresta (punto alto), valle (punto bajo), amplitud (altura) y longitud de onda."},
            {"titulo": "28. Movimiento Armónico Simple (MAS)", "contenido": "El movimiento de un péndulo es un ejemplo de MAS, un movimiento oscilatorio periódico."},
            {"titulo": "29. Frecuencia y Periodo", "contenido": "Frecuencia: número de oscilaciones por segundo. Periodo: tiempo que tarda una oscilación completa."},
            {"titulo": "30. Efecto Doppler", "contenido": "El efecto Doppler es el cambio de frecuencia aparente de una onda debido al movimiento de la fuente o del observador."},
            {"titulo": "31. Polarización de la Luz", "contenido": "La polarización es cuando las ondas de luz se orientan en una sola dirección. Los lentes polarizados bloquean la luz reflejada."},
            {"titulo": "32. Principio de Superposición", "contenido": "Cuando dos ondas se encuentran, sus amplitudes se suman. Esto puede generar interferencia constructiva o destructiva."},
            {"titulo": "33. Fluidos y Propiedades", "contenido": "Un fluido es una sustancia que puede fluir, como un líquido o un gas. Propiedades: densidad, viscosidad y presión."},
            {"titulo": "34. Ley de Pascal", "contenido": "Una fuerza aplicada a un fluido confinado se transmite por igual en todas las direcciones. Es la base de los frenos hidráulicos."},
            {"titulo": "35. Principio de Arquímedes", "contenido": "Un objeto sumergido experimenta una fuerza de empuje hacia arriba igual al peso del fluido que desplaza."},
            {"titulo": "36. Ecuación de Bernoulli", "contenido": "Relaciona la presión y la velocidad en un fluido. Donde el fluido va más rápido, su presión es menor."},
            {"titulo": "37. Flujo Laminar vs. Turbulento", "contenido": "Flujo laminar: capas de fluido se mueven suavemente. Flujo turbulento: el fluido se mueve de forma caótica."},
            {"titulo": "38. Tensión Superficial", "contenido": "Es la cohesión de las moléculas en la superficie de un líquido. Permite que algunos insectos caminen sobre el agua."},
            {"titulo": "39. Capilaridad", "contenido": "Es la capacidad de un líquido de subir por un tubo delgado. Así las plantas transportan agua desde las raíces."},
            {"titulo": "40. Presión Hidrostática", "contenido": "La presión a una profundidad bajo el agua aumenta con la profundidad."},
            {"titulo": "41. Ecuación de Continuidad", "contenido": "El caudal de un fluido que entra en un tubo debe ser igual al que sale."},
            {"titulo": "42. Ondas Sísmicas", "contenido": "Las ondas sísmicas se propagan a través de la tierra. Hay ondas P (más rápidas) y S (más lentas)."},
            {"titulo": "43. Ley de Poiseuille", "contenido": "Describe el flujo de un fluido viscoso. A mayor viscosidad, más lento fluye el líquido."},
            {"titulo": "44. Resonancia", "contenido": "Es cuando un objeto vibra con su frecuencia natural, amplificando la vibración."},
            {"titulo": "45. Difracción de las Ondas", "contenido": "Es cuando una onda se desvía al pasar por un obstáculo o una abertura."},
            {"titulo": "46. Interferencia Constructiva", "contenido": "Dos ondas que se superponen y están en fase generan una onda más grande."},
            {"titulo": "47. Interferencia Destructiva", "contenido": "Dos ondas que se superponen y están en oposición de fase se anulan entre sí."},
            {"titulo": "48. Radiación Electromagnética", "contenido": "Es una forma de energía que se propaga como ondas. La luz visible y las ondas de radio son ejemplos."},
            {"titulo": "49. Polarización por Refracción", "contenido": "Cuando la luz se refleja en una superficie, se polariza, vibrando en una dirección específica."},
            {"titulo": "50. Viscosidad de un Fluido", "contenido": "Es la resistencia interna de un fluido al flujo. La miel es más viscosa que el agua."},

            # SECCIÓN 3: BIOLOGÍA - EVOLUCIÓN Y GENÉTICA MOLECULAR AVANZADA
            {"titulo": "51. Evolución Biológica", "contenido": "La evolución es el cambio en las características genéticas de las poblaciones a través de las generaciones."},
            {"titulo": "52. Mutación", "contenido": "Una mutación es un cambio aleatorio en la secuencia del ADN. Es la fuente primaria de la variación genética."},
            {"titulo": "53. Selección Natural", "contenido": "Los individuos con rasgos que les permiten sobrevivir y reproducirse mejor tienen más probabilidades de dejar descendencia."},
            {"titulo": "54. Flujo Genético", "contenido": "Es la transferencia de genes de una población a otra, por ejemplo, cuando el polen viaja de un lugar a otro."},
            {"titulo": "55. Deriva Genética", "contenido": "Es el cambio aleatorio en las frecuencias de los alelos en una población, especialmente en poblaciones pequeñas."},
            {"titulo": "56. Especiación", "contenido": "Es el proceso por el cual una población de organismos evoluciona para convertirse en una especie distinta."},
            {"titulo": "57. Biotecnología Moderna", "contenido": "Utiliza técnicas como la ingeniería genética para manipular el ADN y crear productos útiles."},
            {"titulo": "58. Organismos Genéticamente Modificados (OGM)", "contenido": "La biotecnología permite crear cultivos resistentes a insectos o a la sequía."},
            {"titulo": "59. Clonación Reproductiva y Terapéutica", "contenido": "Clonación reproductiva: crear un organismo idéntico. Terapéutica: crear células para tratar enfermedades."},
            {"titulo": "60. Vacunas de ARNm", "contenido": "Una vacuna de ARNm enseña a tus células a producir una proteína que desencadena una respuesta inmune."},
            {"titulo": "61. Gen y Alelo", "contenido": "Gen: un segmento de ADN que codifica un rasgo. Alelo: una forma particular de un gen."},
            {"titulo": "62. Ley de Hardy-Weinberg", "contenido": "Esta ley describe cómo las frecuencias alélicas se mantienen constantes si no hay factores evolutivos actuando."},
            {"titulo": "63. Biogeografía", "contenido": "Es el estudio de la distribución de las especies en el espacio y el tiempo."},
            {"titulo": "64. Teoría de la Endosimbiosis", "contenido": "Postula que las mitocondrias y los cloroplastos evolucionaron a partir de bacterias que fueron 'tragadas' por células más grandes."},
            {"titulo": "65. Fósiles y Evolución", "contenido": "Los fósiles son evidencia que nos muestra cómo las especies han cambiado a lo largo de millones de años."},
            {"titulo": "66. Hibridación en la Agricultura", "contenido": "Es el cruce de dos especies o variedades para obtener una descendencia con características mejoradas."},
            {"titulo": "67. Bioética", "contenido": "Es la rama de la ética que se ocupa de los dilemas morales que surgen de los avances en la biología y medicina."},
            {"titulo": "68. Cuello de Botella Genético", "contenido": "Es un evento que reduce drásticamente el tamaño de una población, disminuyendo la diversidad genética."},
            {"titulo": "69. Reloj Molecular", "contenido": "Es una técnica que usa el ritmo de las mutaciones para estimar cuándo se separaron dos especies de un ancestro común."},
            {"titulo": "70. Origen de las Especies en las Islas Galápagos", "contenido": "Los pinzones de Darwin evolucionaron para tener picos adaptados a los diferentes tipos de semillas en cada isla."},
            {"titulo": "71. Genoma", "contenido": "Es el conjunto completo de la información genética de un organismo."},
            {"titulo": "72. Ingeniería Genética en la Medicina", "contenido": "Se puede usar para corregir genes defectuosos que causan enfermedades en los humanos."},
            {"titulo": "73. Adaptación vs. Aclimatación", "contenido": "Adaptación: un rasgo evolutivo. Aclimatación: un cambio fisiológico temporal."},
            {"titulo": "74. Coevolución", "contenido": "Es cuando dos o más especies influyen en la evolución de la otra."},
            {"titulo": "75. Especie", "contenido": "Es un grupo de organismos que pueden reproducirse entre sí y tener descendencia fértil."},

            # SECCIÓN 4: CIENCIAS AMBIENTALES - ECOLOGÍA GLOBAL
            {"titulo": "76. Cambio Climático", "contenido": "Es la alteración a largo plazo de los patrones climáticos globales, causada principalmente por la actividad humana."},
            {"titulo": "77. Efecto Invernadero", "contenido": "Los gases de efecto invernadero retienen el calor en la atmósfera. El exceso de gases causa calentamiento global."},
            {"titulo": "78. Capa de Ozono", "contenido": "La capa de ozono protege a la Tierra de la radiación ultravioleta del sol, que es perjudicial para los seres vivos."},
            {"titulo": "79. Deforestación y el Ciclo del Carbono", "contenido": "Al talar un bosque, se libera CO₂ a la atmósfera y se reduce la capacidad del planeta para absorberlo."},
            {"titulo": "80. Huella de Carbono", "contenido": "Es la cantidad total de gases de efecto invernadero que se emiten por las acciones de un individuo o empresa."},
            {"titulo": "81. Acidificación de los Océanos", "contenido": "El exceso de CO₂ en la atmósfera es absorbido por los océanos, lo que los hace más ácidos."},
            {"titulo": "82. Pérdida de Biodiversidad", "contenido": "Es la disminución de la variedad de vida en la Tierra, causada por la destrucción de hábitats, contaminación, etc."},
            {"titulo": "83. Contaminación del Agua", "contenido": "Los fertilizantes y pesticidas pueden contaminar los ríos, dañando los ecosistemas acuáticos."},
            {"titulo": "84. Energía Renovable", "contenido": "Es la que se obtiene de fuentes que se renuevan de forma natural, como la energía solar, eólica e hidroeléctrica."},
            {"titulo": "85. Biogás", "contenido": "El biogás se produce por la descomposición de materia orgánica y se puede usar como combustible."},
            {"titulo": "86. Agroecosistema", "contenido": "Es un ecosistema modificado por el ser humano para la producción de alimentos."},
            {"titulo": "87. Manejo de Cuencas Hidrográficas", "contenido": "Es la gestión de un área de tierra donde toda el agua fluye hacia un mismo río."},
            {"titulo": "88. Economía Circular", "contenido": "Busca reducir los residuos y reutilizar los productos, usando lo que se desecha como materia prima."},
            {"titulo": "89. Suelos Sanos", "contenido": "Son vitales para la agricultura, la absorción de agua y la captura de carbono."},
            {"titulo": "90. Desarrollo Sostenible", "contenido": "Satisface las necesidades del presente sin comprometer la capacidad de las futuras generaciones."},
            {"titulo": "91. Minería Ilegal", "contenido": "Puede contaminar los ríos con mercurio y cianuro, destruir ecosistemas y afectar la salud."},
            {"titulo": "92. Resiliencia de un Ecosistema", "contenido": "Es la capacidad de un ecosistema para recuperarse de una perturbación."},
            {"titulo": "93. Especies Invasoras", "contenido": "Se reproducen sin control en un nuevo hábitat y desplazan a las especies nativas."},
            {"titulo": "94. Calentamiento Global vs. Cambio Climático", "contenido": "Calentamiento global: aumento de la temperatura. Cambio climático: los efectos más amplios."},
            {"titulo": "95. Polinización por Insectos", "contenido": "Es vital para la reproducción de muchas plantas y para la producción de gran parte de nuestros alimentos."},
            {"titulo": "96. Servicio Ecosistémico", "contenido": "Son los beneficios que los humanos obtenemos de la naturaleza, como el aire limpio y la purificación del agua."},
            {"titulo": "97. Impacto Ambiental", "contenido": "Cualquier cambio en el ambiente que se debe a las actividades humanas, sea positivo o negativo."},
            {"titulo": "98. Biorremediación", "contenido": "Uso de organismos vivos para limpiar contaminantes del ambiente de forma natural."},
            {"titulo": "99. Conservación de la Materia", "contenido": "En un ciclo biogeoquímico, la materia se transforma pero la cantidad total se conserva."},
            {"titulo": "100. Conservación de la Energía", "contenido": "La energía no se crea ni se destruye, solo se transforma en un ecosistema."}
        ]
        # --- Fin del contenido de los ejercicios ---

        # Configurar la interfaz gráfica
        self.crear_widgets()
        self.cargar_ejercicio()

    def crear_widgets(self):
        """Crea y posiciona todos los elementos de la GUI."""
        main_frame = tk.Frame(self, bg="#F0F0F0", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Título principal y contador
        self.titulo_label = tk.Label(main_frame, text="Ejercicios de Ciencias Naturales", font=self.title_font, bg="#F0F0F0")
        self.titulo_label.pack(pady=(0, 10))

        self.contador_label = tk.Label(main_frame, text="Ejercicio 1 de 100", font=self.content_font, bg="#F0F0F0")
        self.contador_label.pack(pady=(0, 10))

        # Marco para mostrar el ejercicio
        ejercicio_frame = tk.LabelFrame(main_frame, text="Concepto a estudiar", font=self.content_font, bg="white", padx=10, pady=10)
        ejercicio_frame.pack(fill="x", pady=(10, 20))

        self.ejercicio_label = tk.Label(ejercicio_frame, text="", wraplength=700, justify="left", font=self.content_font, bg="white", pady=5)
        self.ejercicio_label.pack(fill="x", expand=True)

        # Marco para que el usuario parafrasee
        parafra-sis_frame = tk.LabelFrame(main_frame, text="Escribe tu paráfrasis aquí", font=self.content_font, bg="white", padx=10, pady=10)
        parafra-sis_frame.pack(fill="both", expand=True, pady=(0, 20))

        self.parafra-sis_text = scrolledtext.ScrolledText(parafra-sis_frame, wrap=tk.WORD, width=60, height=8, font=self.paraphrase_font)
        self.parafra-sis_text.pack(fill="both", expand=True)

        # Botones
        self.boton_siguiente = tk.Button(main_frame, text="Siguiente Ejercicio", command=self.siguiente_ejercicio, font=self.content_font, bg="#4CAF50", fg="white", relief="raised", bd=3)
        self.boton_siguiente.pack(pady=10)

        self.boton_guardar = tk.Button(main_frame, text="Guardar todas las paráfrasis", command=self.guardar_parafra-sis, font=self.content_font, bg="#2196F3", fg="white", relief="raised", bd=3)
        self.boton_guardar.pack(pady=5)
        self.boton_guardar.pack_forget() # Ocultar el botón al inicio

    def cargar_ejercicio(self):
        """Carga el ejercicio actual en la interfaz."""
        if self.ejercicios_completados < len(self.ejercicios):
            ejercicio = self.ejercicios[self.ejercicios_completados]
            self.contador_label.config(text=f"Ejercicio {self.ejercicios_completados + 1} de {len(self.ejercicios)}")
            self.ejercicio_label.config(text=f"{ejercicio['titulo']}\n\n{ejercicio['contenido']}")
            self.parafra-sis_text.delete("1.0", tk.END)
        else:
            self.ejercicio_label.config(text="¡Has completado todos los ejercicios! 🎉")
            self.parafra-sis_text.delete("1.0", tk.END)
            self.parafra-sis_text.config(state=tk.DISABLED)
            self.boton_siguiente.pack_forget()
            self.boton_guardar.pack(pady=10)

    def siguiente_ejercicio(self):
        """Guarda la paráfrasis actual y carga el siguiente ejercicio."""
        parafra-sis = self.parafra-sis_text.get("1.0", tk.END).strip()
        if parafra-sis:
            ejercicio_actual = self.ejercicios[self.ejercicios_completados]
            self.parafra-sis_guardadas.append({
                "numero": self.ejercicios_completados + 1,
                "titulo": ejercicio_actual["titulo"],
                "parafra-sis": parafra-sis
            })
            self.ejercicios_completados += 1
            self.cargar_ejercicio()
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una paráfrasis antes de continuar.")

    def guardar_parafra-sis(self):
        """Guarda todas las paráfrasis en un archivo de texto."""
        nombre_archivo = "parafra-sis_ciencias_11_tkinter.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                for item in self.parafra-sis_guardadas:
                    archivo.write(f"--- Ejercicio {item['numero']} - {item['titulo']} ---\n")
                    archivo.write(f"{item['parafra-sis']}\n\n")
            messagebox.showinfo("Guardado Exitoso", f"Se ha creado el archivo '{nombre_archivo}' con tus paráfrasis.")
        except IOError as e:
            messagebox.showerror("Error de Archivo", f"No se pudo guardar el archivo: {e}")

if __name__ == '__main__':
    app = CienciasApp()
    app.mainloop()
