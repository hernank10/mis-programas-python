import random
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class AprendizajeConceptosGriegos:
    """Sistema interactivo para aprendizaje trilingüe de conceptos griegos"""
    
    def __init__(self):
        self.conceptos = self.cargar_conceptos()
        self.estadisticas = {
            'intentos': 0,
            'aciertos': 0,
            'conceptos_practicados': set(),
            'historial': []
        }
        self.cargar_estadisticas()
    
    def cargar_conceptos(self) -> List[Dict]:
        """Carga la base de datos de conceptos griegos"""
        conceptos_base = [
            # FILOSOFÍA & VIRTUD (primeros 20)
            {
                'id': 1,
                'griego': 'Γνῶθι σαυτόν',
                'transliteracion': 'Gnōthi seautón',
                'español': 'Conócete a ti mismo',
                'ingles': 'Know thyself',
                'categoria': 'Filosofía',
                'explicacion': 'Máxima délfica que invita al autoconocimiento como base de la sabiduría'
            },
            {
                'id': 2,
                'griego': 'Ἀρετή',
                'transliteracion': 'Aretḗ',
                'español': 'Virtud, excelencia',
                'ingles': 'Virtue, excellence',
                'categoria': 'Filosofía',
                'explicacion': 'Excelencia en el cumplimiento de la función propia'
            },
            {
                'id': 3,
                'griego': 'Εὐδαιμονία',
                'transliteracion': 'Eudaimonía',
                'español': 'Felicidad, florecimiento',
                'ingles': 'Happiness, human flourishing',
                'categoria': 'Filosofía',
                'explicacion': 'Estado de plenitud y realización humana'
            },
            {
                'id': 4,
                'griego': 'Λόγος',
                'transliteracion': 'Lógos',
                'español': 'Razón, palabra, principio',
                'ingles': 'Reason, word, principle',
                'categoria': 'Filosofía',
                'explicacion': 'Principio racional que ordena el cosmos'
            },
            {
                'id': 5,
                'griego': 'Πόθος',
                'transliteracion': 'Póthos',
                'español': 'Anhelo, nostalgia',
                'ingles': 'Longing, yearning',
                'categoria': 'Filosofía',
                'explicacion': 'Nostalgia profunda, deseo metafísico'
            },
            # MÁXIMAS DELFICAS
            {
                'id': 6,
                'griego': 'Μηδὲν ἄγαν',
                'transliteracion': 'Mēdén ágan',
                'español': 'Nada en exceso',
                'ingles': 'Nothing in excess',
                'categoria': 'Máximas',
                'explicacion': 'Principio de moderación délfico'
            },
            {
                'id': 7,
                'griego': 'Πάντα ῥεῖ',
                'transliteracion': 'Pánta rheî',
                'español': 'Todo fluye',
                'ingles': 'Everything flows',
                'categoria': 'Máximas',
                'explicacion': 'Principio heraclíteo del cambio constante'
            },
            {
                'id': 8,
                'griego': 'Σπεῦδε βραδέως',
                'transliteracion': 'Speûde bradéōs',
                'español': 'Apresúrate lentamente',
                'ingles': 'Make haste slowly',
                'categoria': 'Máximas',
                'explicacion': 'Prudencia en la acción'
            },
            # TRAGEDIA
            {
                'id': 9,
                'griego': 'Πάθει μάθος',
                'transliteracion': 'Páthei máthos',
                'español': 'Aprendizaje a través del sufrimiento',
                'ingles': 'Learning through suffering',
                'categoria': 'Tragedia',
                'explicacion': 'Máxima de Esquilo sobre el crecimiento personal'
            },
            # CONCEPTOS MODERNOS
            {
                'id': 10,
                'griego': 'Φιλότιμο',
                'transliteracion': 'Philótimo',
                'español': 'Amor al honor, dignidad',
                'ingles': 'Love of honour, dignity',
                'categoria': 'Moderno',
                'explicacion': 'Valor fundamental de la ética griega moderna'
            },
            {
                'id': 11,
                'griego': 'Μεράκι',
                'transliteracion': 'Meráki',
                'español': 'Alma, pasión en el hacer',
                'ingles': 'Soulful passion',
                'categoria': 'Moderno',
                'explicacion': 'Poner el alma en lo que se hace'
            },
            {
                'id': 12,
                'griego': 'Καιρός',
                'transliteracion': 'Kairós',
                'español': 'Momento oportuno',
                'ingles': 'Opportune moment',
                'categoria': 'Filosofía',
                'explicacion': 'Tiempo cualitativo, momento propicio'
            }
        ]
        return conceptos_base
    
    def cargar_estadisticas(self):
        """Carga estadísticas previas si existen"""
        try:
            if os.path.exists('estadisticas_griego.json'):
                with open('estadisticas_griego.json', 'r', encoding='utf-8') as f:
                    self.estadisticas = json.load(f)
        except:
            pass
    
    def guardar_estadisticas(self):
        """Guarda las estadísticas de aprendizaje"""
        with open('estadisticas_griego.json', 'w', encoding='utf-8') as f:
            json.dump(self.estadisticas, f, ensure_ascii=False, indent=2)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        while True:
            print("\n" + "="*60)
            print("SISTEMA DE APRENDIZAJE TRILINGÜE - CONCEPTOS GRIEGOS")
            print("="*60)
            print("\nMENÚ PRINCIPAL:")
            print("1. Ejercicio de Escritura Completa")
            print("2. Práctica de Comparación Bilingüe")
            print("3. Modo Desafío Aleatorio")
            print("4. Crear Frases Personalizadas")
            print("5. Ver Todos los Conceptos")
            print("6. Estadísticas de Aprendizaje")
            print("7. Examen Final")
            print("0. Salir")
            
            opcion = input("\nSeleccione una opción (0-7): ").strip()
            
            if opcion == '1':
                self.ejercicio_escritura_completa()
            elif opcion == '2':
                self.practica_comparacion_bilingue()
            elif opcion == '3':
                self.modo_desafio_aleatorio()
            elif opcion == '4':
                self.crear_frases_personalizadas()
            elif opcion == '5':
                self.ver_todos_conceptos()
            elif opcion == '6':
                self.mostrar_estadisticas()
            elif opcion == '7':
                self.examen_final()
            elif opcion == '0':
                print("\n¡Gracias por practicar! Guardando estadísticas...")
                self.guardar_estadisticas()
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def ejercicio_escritura_completa(self):
        """Ejercicio 1: Escribir las tres versiones y crear frases"""
        concepto = random.choice(self.conceptos)
        
        print("\n" + "-"*60)
        print("EJERCICIO DE ESCRITURA COMPLETA")
        print("-"*60)
        print(f"\nConcepto a practicar: {concepto['griego']}")
        print(f"Categoría: {concepto['categoria']}")
        print(f"Explicación: {concepto['explicacion']}")
        
        # Registrar que se está practicando este concepto
        self.estadisticas['conceptos_practicados'].add(concepto['id'])
        self.estadisticas['intentos'] += 1
        
        print("\n" + "="*40)
        print("PARTE 1: ESCRITURA DE TRADUCCIONES")
        print("="*40)
        
        # 1. Transliteración
        translit_input = input("\n1. Escriba la transliteración: ").strip()
        if translit_input.lower() == concepto['transliteracion'].lower():
            print("   ✓ Correcto!")
        else:
            print(f"   ✗ La transliteración correcta es: {concepto['transliteracion']}")
        
        # 2. Español
        espanol_input = input("\n2. Escriba la traducción al español: ").strip()
        if concepto['español'].lower() in espanol_input.lower() or espanol_input.lower() in concepto['español'].lower():
            print("   ✓ Correcto!")
            self.estadisticas['aciertos'] += 1
        else:
            print(f"   ✗ La traducción española es: {concepto['español']}")
        
        # 3. Inglés
        ingles_input = input("\n3. Escriba la traducción al inglés: ").strip()
        if concepto['ingles'].lower() in ingles_input.lower() or ingles_input.lower() in concepto['ingles'].lower():
            print("   ✓ Correcto!")
            self.estadisticas['aciertos'] += 1
        else:
            print(f"   ✗ La traducción inglesa es: {concepto['ingles']}")
        
        print("\n" + "="*40)
        print("PARTE 2: CREACIÓN DE FRASES")
        print("="*40)
        print("\nAhora cree frases usando este concepto en contexto:")
        
        # Frase en español
        frase_es = input("\nEscriba una frase en ESPAÑOL usando este concepto:\n")
        print(f"\nSu frase en español: \"{frase_es}\"")
        
        # Frase en inglés
        frase_en = input("\nEscriba una frase en INGLÉS usando este concepto:\n")
        print(f"\nSu frase en inglés: \"{frase_en}\"")
        
        # Guardar las frases creadas
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'concepto': concepto['transliteracion'],
            'frase_espanol': frase_es,
            'frase_ingles': frase_en
        }
        self.estadisticas['historial'].append(registro)
        
        print("\n" + "="*40)
        print("RESUMEN DEL CONCEPTO:")
        print("="*40)
        print(f"Griego: {concepto['griego']}")
        print(f"Transliteración: {concepto['transliteracion']}")
        print(f"Español: {concepto['español']}")
        print(f"English: {concepto['ingles']}")
        
        input("\nPresione Enter para continuar...")
    
    def practica_comparacion_bilingue(self):
        """Ejercicio 2: Práctica de comparación entre español e inglés"""
        print("\n" + "-"*60)
        print("PRÁCTICA DE COMPARACIÓN BILINGÜE")
        print("-"*60)
        print("\nSe mostrará un concepto en una lengua, debe escribir la otra.")
        
        # Seleccionar modo
        print("\nModos disponibles:")
        print("1. Español → Inglés")
        print("2. Inglés → Español")
        print("3. Griego → Ambos")
        
        modo = input("\nSeleccione modo (1-3): ").strip()
        concepto = random.choice(self.conceptos)
        
        self.estadisticas['intentos'] += 1
        
        if modo == '1':
            # Español → Inglés
            print(f"\nConcepto en ESPAÑOL: {concepto['español']}")
            respuesta = input("Escriba la traducción al INGLÉS: ").strip()
            
            if concepto['ingles'].lower() in respuesta.lower() or respuesta.lower() in concepto['ingles'].lower():
                print("✓ ¡Correcto!")
                self.estadisticas['aciertos'] += 1
            else:
                print(f"✗ La respuesta correcta es: {concepto['ingles']}")
        
        elif modo == '2':
            # Inglés → Español
            print(f"\nConcepto en INGLÉS: {concepto['ingles']}")
            respuesta = input("Escriba la traducción al ESPAÑOL: ").strip()
            
            if concepto['español'].lower() in respuesta.lower() or respuesta.lower() in concepto['español'].lower():
                print("✓ ¡Correcto!")
                self.estadisticas['aciertos'] += 1
            else:
                print(f"✗ La respuesta correcta es: {concepto['español']}")
        
        elif modo == '3':
            # Griego → Ambos
            print(f"\nConcepto en GRIEGO: {concepto['griego']}")
            print(f"Transliteración: {concepto['transliteracion']}")
            
            respuesta_es = input("\nEscriba la traducción al ESPAÑOL: ").strip()
            respuesta_en = input("Escriba la traducción al INGLÉS: ").strip()
            
            aciertos = 0
            if concepto['español'].lower() in respuesta_es.lower() or respuesta_es.lower() in concepto['español'].lower():
                print("✓ Español correcto")
                aciertos += 1
            else:
                print(f"✗ Español correcto: {concepto['español']}")
            
            if concepto['ingles'].lower() in respuesta_en.lower() or respuesta_en.lower() in concepto['ingles'].lower():
                print("✓ Inglés correcto")
                aciertos += 1
            else:
                print(f"✗ Inglés correcto: {concepto['ingles']}")
            
            if aciertos == 2:
                self.estadisticas['aciertos'] += 2
        
        # Mostrar información completa
        print("\n" + "="*40)
        print("INFORMACIÓN COMPLETA:")
        print("="*40)
        print(f"Griego: {concepto['griego']}")
        print(f"Transliteración: {concepto['transliteracion']}")
        print(f"Español: {concepto['español']}")
        print(f"English: {concepto['ingles']}")
        print(f"\nExplicación: {concepto['explicacion']}")
        
        input("\nPresione Enter para continuar...")
    
    def modo_desafio_aleatorio(self):
        """Modo 3: Desafío aleatorio con tiempo y puntuación"""
        print("\n" + "-"*60)
        print("MODO DESAFÍO ALEATORIO")
        print("-"*60)
        print("\nResponda correctamente a 5 conceptos aleatorios.")
        print("Tiene 30 segundos por cada uno.")
        
        import time
        puntuacion = 0
        total_preguntas = min(5, len(self.conceptos))
        
        conceptos_desafio = random.sample(self.conceptos, total_preguntas)
        
        for i, concepto in enumerate(conceptos_desafio, 1):
            print(f"\n--- Pregunta {i} de {total_preguntas} ---")
            
            # Seleccionar tipo de pregunta aleatoria
            tipo_pregunta = random.choice(['español', 'ingles', 'griego'])
            
            inicio = time.time()
            
            if tipo_pregunta == 'español':
                print(f"\n¿Cuál es la traducción al INGLÉS de: '{concepto['español']}'?")
                print(f"(Transliteración: {concepto['transliteracion']})")
                respuesta = input("Respuesta: ").strip()
                correcta = concepto['ingles']
            
            elif tipo_pregunta == 'ingles':
                print(f"\n¿Cuál es la traducción al ESPAÑOL de: '{concepto['ingles']}'?")
                print(f"(Griego: {concepto['griego']})")
                respuesta = input("Respuesta: ").strip()
                correcta = concepto['español']
            
            else:  # griego
                print(f"\nGriego: {concepto['griego']}")
                respuesta_es = input("Traducción al español: ").strip()
                respuesta_en = input("Traducción al inglés: ").strip()
                
                tiempo_transcurrido = time.time() - inicio
                
                if tiempo_transcurrido > 30:
                    print("¡Tiempo agotado!")
                    continue
                
                # Verificar ambas respuestas
                es_correcta = (concepto['español'].lower() in respuesta_es.lower() or 
                              respuesta_es.lower() in concepto['español'].lower())
                en_correcta = (concepto['ingles'].lower() in respuesta_en.lower() or 
                              respuesta_en.lower() in concepto['ingles'].lower())
                
                if es_correcta and en_correcta:
                    print("✓ ¡Doble acierto!")
                    puntuacion += 2
                elif es_correcta or en_correcta:
                    print("✓ ¡Acierto parcial!")
                    puntuacion += 1
                    if not es_correcta:
                        print(f"  Español correcto: {concepto['español']}")
                    if not en_correcta:
                        print(f"  Inglés correcto: {concepto['ingles']}")
                else:
                    print(f"✗ Español: {concepto['español']}")
                    print(f"✗ English: {concepto['ingles']}")
                
                continue
            
            tiempo_transcurrido = time.time() - inicio
            
            if tiempo_transcurrido > 30:
                print("¡Tiempo agotado!")
                print(f"Respuesta correcta: {correcta}")
                continue
            
            # Verificar respuesta para español/inglés
            if correcta.lower() in respuesta.lower() or respuesta.lower() in correcta.lower():
                print("✓ ¡Correcto!")
                puntuacion += 1
            else:
                print(f"✗ Respuesta correcta: {correcta}")
            
            # Mostrar información completa
            print(f"\nInformación completa:")
            print(f"Griego: {concepto['griego']}")
            print(f"Transliteración: {concepto['transliteracion']}")
            print(f"Español: {concepto['español']}")
            print(f"English: {concepto['ingles']}")
        
        # Resultado final
        print("\n" + "="*40)
        print("RESULTADO FINAL DEL DESAFÍO")
        print("="*40)
        print(f"Puntuación: {puntuacion}/{total_preguntas * 2} puntos posibles")
        print(f"Porcentaje: {(puntuacion/(total_preguntas * 2)) * 100:.1f}%")
        
        # Actualizar estadísticas
        self.estadisticas['intentos'] += total_preguntas
        # Nota: Los aciertos ya se contaron individualmente
        
        input("\nPresione Enter para continuar...")
    
    def crear_frases_personalizadas(self):
        """Modo 4: Crear y guardar frases personalizadas"""
        print("\n" + "-"*60)
        print("CREACIÓN DE FRASES PERSONALIZADAS")
        print("-"*60)
        
        # Mostrar algunos conceptos sugeridos
        print("\nConceptos disponibles:")
        for i, concepto in enumerate(self.conceptos[:10], 1):
            print(f"{i}. {concepto['transliteracion']} - {concepto['español']}")
        
        print("\n0. Seleccionar concepto por nombre")
        
        opcion = input("\nSeleccione un concepto (1-10) o 0 para buscar: ").strip()
        
        if opcion == '0':
            # Búsqueda por nombre
            busqueda = input("Ingrese parte del nombre (griego, español o inglés): ").lower()
            encontrados = []
            
            for concepto in self.conceptos:
                if (busqueda in concepto['transliteracion'].lower() or 
                    busqueda in concepto['español'].lower() or 
                    busqueda in concepto['ingles'].lower()):
                    encontrados.append(concepto)
            
            if not encontrados:
                print("No se encontraron conceptos con esa búsqueda.")
                return
            
            print("\nConceptos encontrados:")
            for i, concepto in enumerate(encontrados, 1):
                print(f"{i}. {concepto['transliteracion']} - {concepto['español']}")
            
            seleccion = int(input("\nSeleccione un concepto: ")) - 1
            if 0 <= seleccion < len(encontrados):
                concepto_seleccionado = encontrados[seleccion]
            else:
                print("Selección no válida.")
                return
        elif opcion.isdigit() and 1 <= int(opcion) <= 10:
            concepto_seleccionado = self.conceptos[int(opcion) - 1]
        else:
            print("Opción no válida.")
            return
        
        print("\n" + "="*40)
        print(f"CONCEPTO SELECCIONADO:")
        print("="*40)
        print(f"Griego: {concepto_seleccionado['griego']}")
        print(f"Transliteración: {concepto_seleccionado['transliteracion']}")
        print(f"Español: {concepto_seleccionado['español']}")
        print(f"English: {concepto_seleccionado['ingles']}")
        print(f"\nExplicación: {concepto_seleccionado['explicacion']}")
        
        print("\n" + "="*40)
        print("CREACIÓN DE FRASES:")
        print("="*40)
        
        # Crear frases en español
        print("\nFRASE EN ESPAÑOL:")
        print("Contextos sugeridos: filosófico, literario, personal, académico")
        frase_es = input("Escriba su frase:\n").strip()
        
        # Crear frases en inglés
        print("\nFRASE EN INGLÉS:")
        print("Suggested contexts: philosophical, literary, personal, academic")
        frase_en = input("Write your sentence:\n").strip()
        
        # Guardar en historial
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'concepto': concepto_seleccionado['transliteracion'],
            'frase_espanol': frase_es,
            'frase_ingles': frase_en,
            'tipo': 'personalizada'
        }
        self.estadisticas['historial'].append(registro)
        
        print("\n" + "="*40)
        print("FRASES GUARDADAS:")
        print("="*40)
        print(f"\nEspañol: \"{frase_es}\"")
        print(f"\nEnglish: \"{frase_en}\"")
        
        # Opción para guardar en archivo
        guardar = input("\n¿Desea guardar estas frases en un archivo? (s/n): ").lower()
        if guardar == 's':
            with open('frases_griego.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}]")
                f.write(f"\nConcepto: {concepto_seleccionado['transliteracion']}")
                f.write(f"\nEspañol: {frase_es}")
                f.write(f"\nEnglish: {frase_en}")
                f.write(f"\n{'-'*40}\n")
            print("Frases guardadas en 'frases_griego.txt'")
        
        input("\nPresione Enter para continuar...")
    
    def ver_todos_conceptos(self):
        """Modo 5: Ver todos los conceptos disponibles"""
        print("\n" + "-"*60)
        print("TODOS LOS CONCEPTOS DISPONIBLES")
        print("-"*60)
        
        # Filtrar por categoría si se desea
        categorias = set(c['categoria'] for c in self.conceptos)
        print("\nCategorías disponibles:", ", ".join(categorias))
        
        filtro = input("\nFiltrar por categoría (Enter para todas): ").strip()
        
        print("\n" + "="*80)
        print(f"{'ID':<4} {'TRANSLITERACIÓN':<20} {'ESPAÑOL':<25} {'ENGLISH':<25} {'CATEGORÍA':<10}")
        print("="*80)
        
        for concepto in self.conceptos:
            if not filtro or concepto['categoria'].lower() == filtro.lower():
                print(f"{concepto['id']:<4} {concepto['transliteracion']:<20} {concepto['español']:<25} {concepto['ingles']:<25} {concepto['categoria']:<10}")
        
        print("\nTotal de conceptos:", len(self.conceptos))
        
        input("\nPresione Enter para continuar...")
    
    def mostrar_estadisticas(self):
        """Modo 6: Mostrar estadísticas de aprendizaje"""
        print("\n" + "-"*60)
        print("ESTADÍSTICAS DE APRENDIZAJE")
        print("-"*60)
        
        total_conceptos = len(self.conceptos)
        practicados = len(self.estadisticas['conceptos_practicados'])
        
        print(f"\nConceptos totales: {total_conceptos}")
        print(f"Conceptos practicados: {practicados}")
        print(f"Porcentaje cubierto: {(practicados/total_conceptos)*100:.1f}%")
        
        if self.estadisticas['intentos'] > 0:
            porcentaje_aciertos = (self.estadisticas['aciertos'] / (self.estadisticas['intentos'] * 2)) * 100
            print(f"\nIntentos totales: {self.estadisticas['intentos']}")
            print(f"Aciertos: {self.estadisticas['aciertos']}")
            print(f"Tasa de aciertos: {porcentaje_aciertos:.1f}%")
        else:
            print("\nAún no hay datos de práctica.")
        
        # Mostrar últimas frases creadas
        if self.estadisticas['historial']:
            print(f"\nÚltimas frases creadas ({min(5, len(self.estadisticas['historial']))} más recientes):")
            print("-"*60)
            
            for registro in self.estadisticas['historial'][-5:]:
                print(f"\nFecha: {registro['fecha']}")
                print(f"Concepto: {registro['concepto']}")
                print(f"Español: {registro['frase_espanol'][:50]}...")
                print(f"English: {registro['frase_ingles'][:50]}...")
        
        input("\nPresione Enter para continuar...")
    
    def examen_final(self):
        """Modo 7: Examen final comprensivo"""
        print("\n" + "-"*60)
        print("EXAMEN FINAL COMPRENSIVO")
        print("-"*60)
        print("\nResponda correctamente a 10 preguntas de diferentes tipos.")
        print("Cada pregunta vale 10 puntos.")
        print("\n¡Buena suerte!")
        
        import time
        puntuacion = 0
        total_preguntas = 10
        
        # Seleccionar preguntas aleatorias
        preguntas = random.sample(self.conceptos, min(total_preguntas, len(self.conceptos)))
        
        for i, concepto in enumerate(preguntas, 1):
            print(f"\n--- Pregunta {i} de {total_preguntas} ---")
            
            # Tipo de pregunta aleatorio
            tipo = random.choice(['traduccion', 'frase_es', 'frase_en', 'completa'])
            
            if tipo == 'traduccion':
                # Traducción en cualquier dirección
                direccion = random.choice(['es-en', 'en-es', 'griego'])
                
                if direccion == 'es-en':
                    print(f"\nTraduzca al INGLÉS: '{concepto['español']}'")
                    respuesta = input("Respuesta: ").strip()
                    correcta = concepto['ingles']
                    
                elif direccion == 'en-es':
                    print(f"\nTraduzca al ESPAÑOL: '{concepto['ingles']}'")
                    respuesta = input("Respuesta: ").strip()
                    correcta = concepto['español']
                    
                else:  # griego
                    print(f"\nGriego: {concepto['griego']}")
                    print(f"Transliteración: {concepto['transliteracion']}")
                    respuesta_es = input("Español: ").strip()
                    respuesta_en = input("English: ").strip()
                    
                    # Verificar ambas
                    es_correcta = (concepto['español'].lower() in respuesta_es.lower() or 
                                  respuesta_es.lower() in concepto['español'].lower())
                    en_correcta = (concepto['ingles'].lower() in respuesta_en.lower() or 
                                  respuesta_en.lower() in concepto['ingles'].lower())
                    
                    if es_correcta and en_correcta:
                        print("✓ ¡Perfecto! 10 puntos")
                        puntuacion += 10
                    elif es_correcta or en_correcta:
                        print("✓ ¡Parcialmente correcto! 5 puntos")
                        puntuacion += 5
                        if not es_correcta:
                            print(f"  Español: {concepto['español']}")
                        if not en_correcta:
                            print(f"  English: {concepto['ingles']}")
                    else:
                        print(f"✗ Español: {concepto['español']}")
                        print(f"✗ English: {concepto['ingles']}")
                    
                    continue
                
                # Verificar respuesta simple
                if correcta.lower() in respuesta.lower() or respuesta.lower() in correcta.lower():
                    print("✓ ¡Correcto! 10 puntos")
                    puntuacion += 10
                else:
                    print(f"✗ Correcto: {correcta}")
            
            elif tipo == 'frase_es':
                print(f"\nCree una frase en ESPAÑOL usando el concepto: {concepto['transliteracion']}")
                print(f"({concepto['español']})")
                frase = input("Su frase: ").strip()
                
                # Verificar que use el concepto (aproximadamente)
                if concepto['transliteracion'].lower() in frase.lower() or concepto['español'].lower() in frase.lower():
                    print("✓ ¡Buen uso del concepto! 10 puntos")
                    puntuacion += 10
                else:
                    print("✗ La frase no parece usar el concepto claramente")
            
            elif tipo == 'frase_en':
                print(f"\nCreate an ENGLISH sentence using: {concepto['transliteracion']}")
                print(f"({concepto['ingles']})")
                frase = input("Your sentence: ").strip()
                
                if concepto['transliteracion'].lower() in frase.lower() or concepto['ingles'].lower() in frase.lower():
                    print("✓ ¡Good use of the concept! 10 points")
                    puntuacion += 10
                else:
                    print("✗ The sentence doesn't clearly use the concept")
            
            else:  # completa
                print(f"\nComplete la información para: {concepto['griego']}")
                translit = input("Transliteración: ").strip()
                espanol = input("Español: ").strip()
                ingles = input("English: ").strip()
                
                correctos = 0
                if concepto['transliteracion'].lower() == translit.lower():
                    correctos += 1
                if concepto['español'].lower() in espanol.lower() or espanol.lower() in concepto['español'].lower():
                    correctos += 1
                if concepto['ingles'].lower() in ingles.lower() or ingles.lower() in concepto['ingles'].lower():
                    correctos += 1
                
                puntos = (correctos * 10) // 3
                puntuacion += puntos
                print(f"✓ {correctos}/3 correctos - {puntos} puntos")
        
        # Resultado final
        print("\n" + "="*50)
        print("RESULTADO DEL EXAMEN")
        print("="*50)
        print(f"\nPuntuación final: {puntuacion}/100 puntos")
        print(f"Porcentaje: {puntuacion}%")
        
        if puntuacion >= 90:
            print("\n🎉 ¡Excelente! Dominio sobresaliente.")
        elif puntuacion >= 70:
            print("\n👍 ¡Muy bien! Buen conocimiento.")
        elif puntuacion >= 50:
            print("\n✅ Aprobado. Sigue practicando.")
        else:
            print("\n📚 Necesitas más práctica. ¡No te rindas!")
        
        # Guardar resultado del examen
        self.estadisticas['historial'].append({
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'tipo': 'examen_final',
            'puntuacion': puntuacion
        })
        
        input("\nPresione Enter para continuar...")

def main():
    """Función principal del programa"""
    print("\n" + "="*70)
    print("SISTEMA DE APRENDIZAJE TRILINGÜE DE CONCEPTOS GRIEGOS")
    print("="*70)
    print("\nEste programa te ayudará a dominar 100 conceptos griegos en")
    print("sus tres dimensiones: transliteración, español e inglés.")
    print("\nDesarrollado para aprendizaje activo y expresión cultural.")
    
    sistema = AprendizajeConceptosGriegos()
    sistema.mostrar_menu_principal()

if __name__ == "__main__":
    main()
