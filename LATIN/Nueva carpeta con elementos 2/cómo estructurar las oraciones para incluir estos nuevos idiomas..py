def verificar_entrada(correcta, idioma):
    while True:
        entrada = input(f"Escribe ortográficamente la siguiente oración en {idioma}: \n{correcta}\nTu respuesta: ")
        if entrada.strip() == correcta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")

# Lista de oraciones en varios idiomas
oraciones = {
    'ingles': [
        "Python is a versatile programming language.",
        "Lists are mutable in Python.",
        "Dictionaries store key-value pairs.",
        "Tuples are immutable data structures.",
        "Conditional statements control program flow.",
        "Loops repeat code until a condition is met.",
        "Functions encapsulate reusable code blocks.",
        "Classes define object blueprints.",
        "Modules help organize Python code.",
        "Exception handling manages errors gracefully."
    ],
    'espanol': [
        "Python es un lenguaje de programación versátil.",
        "Las listas son mutables en Python.",
        "Los diccionarios almacenan pares clave-valor.",
        "Las tuplas son estructuras de datos inmutables.",
        "Las declaraciones condicionales controlan el flujo del programa.",
        "Los bucles repiten código hasta que se cumple una condición.",
        "Las funciones encapsulan bloques de código reutilizables.",
        "Las clases definen los planos de los objetos.",
        "Los módulos ayudan a organizar el código de Python.",
        "El manejo de excepciones gestiona errores de manera elegante."
    ],
    'hebreo': [
        "פייתון הוא שפת תכנות רב-תכליתית.",
        "רשימות ניתנות לשינוי בפייתון.",
        "מילונים אחסנו מפות מפתח-ערך.",
        "טאפלים הם מבני נתונים לא משנים.",
        "הצהרות תנאי שולטות בזרימת התוכנית.",
        "לולאות חוזרות על קוד עד שתתקיים תנאי.",
        "פונקציות מכללות בלוקי קוד שניתן להשתמש בהם שוב.",
        "מחלקות מגדירות את התוכניות לאובייקטים.",
        "מודולים עוזרים לארגן את קוד הפייתון.",
        "טיפול בחריגות מנהל שגיאות בצורה יעילה."
    ]
}

# Iterar sobre las oraciones y pedir al usuario que las escriba correctamente
for idioma, lista_oraciones in oraciones.items():
    print(f"\n### Idioma: {idioma.capitalize()} ###\n")
    for oracion in lista_oraciones:
        verificar_entrada(oracion, idioma)
