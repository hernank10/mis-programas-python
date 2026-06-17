#!/usr/bin/env python3
"""Agregar más ejercicios de inglés a la base de datos"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db_manager import db

ejercicios = [
    # Más plurales
    ('plurales', '¿Cuál es el plural de "fox"?', 'foxes', 'Los plurales terminados en -x añaden -es', 1),
    ('plurales', '¿Cuál es el plural de "baby"?', 'babies', 'Los plurales terminados en -y precedida de consonante cambian a -ies', 1),
    ('plurales', '¿Cuál es el plural de "man"?', 'men', 'Plural irregular', 2),
    ('plurales', '¿Cuál es el plural de "woman"?', 'women', 'Plural irregular', 2),
    
    # Más verbos
    ('verbos', '¿Cuál es el pasado de "write"?', 'wrote', 'Verbo irregular', 2),
    ('verbos', '¿Cuál es el pasado de "read"?', 'read', 'Verbo irregular (se pronuncia diferente)', 2),
    ('verbos', '¿Cuál es el pasado de "sing"?', 'sang', 'Verbo irregular', 2),
    ('verbos', '¿Cuál es el pasado de "swim"?', 'swam', 'Verbo irregular', 2),
    
    # Más vocabulario
    ('vocabulario', '¿Cómo se dice "mesa" en inglés?', 'table', 'Mueble', 1),
    ('vocabulario', '¿Cómo se dice "silla" en inglés?', 'chair', 'Mueble', 1),
    ('vocabulario', '¿Cómo se dice "ventana" en inglés?', 'window', 'Parte de una casa', 1),
    ('vocabulario', '¿Cómo se dice "puerta" en inglés?', 'door', 'Parte de una casa', 1),
    ('vocabulario', '¿Cómo se dice "amigo" en inglés?', 'friend', 'Persona cercana', 1),
    ('vocabulario', '¿Cómo se dice "familia" en inglés?', 'family', 'Grupo de personas', 1),
    
    # Más tiempos verbales
    ('tiempos', 'Completa: "I ____ (be) a teacher"', 'am', 'Presente simple del verbo to be', 1),
    ('tiempos', 'Completa: "She ____ (study) now"', 'is studying', 'Presente continuo', 2),
    ('tiempos', 'Completa: "They ____ (finish) already"', 'have finished', 'Presente perfecto', 2),
    ('tiempos', 'Completa: "He ____ (go) to the market yesterday"', 'went', 'Pasado simple', 2),
    
    # Más preposiciones
    ('preposiciones', 'Completa: "I am afraid ____ spiders"', 'of', 'Miedo a algo', 2),
    ('preposiciones', 'Completa: "She is looking ____ her keys"', 'for', 'Buscar algo', 2),
    ('preposiciones', 'Completa: "He is waiting ____ the bus"', 'for', 'Esperar algo', 2),
]

for e in ejercicios:
    db.ejecutar('''
    INSERT OR IGNORE INTO ejercicios_ingles 
    (categoria, pregunta, respuesta_correcta, explicacion, dificultad)
    VALUES (?, ?, ?, ?, ?)
    ''', e)

print(f"✅ Agregados {len(ejercicios)} ejercicios adicionales")
print(f"📊 Total ejercicios de inglés: {db.consultar_uno('SELECT COUNT(*) FROM ejercicios_ingles')[0]}")
