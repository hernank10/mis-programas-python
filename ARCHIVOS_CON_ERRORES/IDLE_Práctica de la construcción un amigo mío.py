Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/jhernanacvdo/Desktop/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO.py

🧠 PRÁCTICA DE LA CONSTRUCCIÓN 'UN AMIGO MÍO'
1. Ver teoría
2. Ver ejemplos
3. Hacer ejercicio de redacción
4. Salir
Selecciona una opción: 
= RESTART: /Users/jhernanacvdo/Desktop/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO2.py

🧠 MENÚ DE PRÁCTICA: CONSTRUCCIÓN 'UN AMIGO MÍO'
1. Ver teoría
2. Ver ejemplos
3. Hacer ejercicio de redacción
4. Revisar errores
5. Guardar progreso
6. Salir
Selecciona una opción: 
= RESTART: /Users/jhernanacvdo/Desktop/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter.py

= RESTART: /Users/jhernanacvdo/Documents/Programa- Práctica de la construcción "un amigo mío".py

=== TEORÍA ===
En español, usamos la estructura:
[Artículo indefinido (un/una)] + [sustantivo] + [posesivo pospuesto (mío/tuyo/suyo...)]

Ejemplo: 
- "Un compañero tuyo" (no "un de tus compañeros" como en inglés/francés).
- "Una idea suya" (no "una de sus ideas").

Reglas:
1. El posesivo concuerda en género/número con el sustantivo: "un libro mío" (masculino) / "una amiga mía" (femenino).
2. ¡Nunca uses artículo definido (el/la) con posesivo antepuesto! Incorrecto: "un mi amigo".


=== EJEMPLOS ===

▶ Grupo 1 ◀
- Un profesor mío
- Una vecina suya
- Unos compañeros nuestros
- Una prima tuya
- Un médico suyo
- Unas conocidas vuestras
- Un político tuyo
- Una influencer mía
- Unos clientes suyos
- Una amiga nuestra
- Un poeta suyo
- Unas socias vuestras
- Un cantante mío
- Una actriz suya
- Unos vecinos tuyos

▶ Grupo 2 ◀
- Un libro tuyo
- Una carta suya
- Unos zapatos míos
- Una idea nuestra
- Un proyecto suyo
- Unas llaves vuestras
- Un coche mío
- Una foto tuya
- Unos documentos nuestros
- Una canción suya
- Un problema mío
- Unas opiniones vuestras
- Un teléfono suyo
- Una historia nuestra
- Unos errores tuyos

▶ Grupo 3 ◀
- Un restaurante mío
- Una ciudad suya
- Unos pueblos nuestros
- Una universidad tuya
- Un parque suyo
- Unas calles vuestras
- Un sueño mío
- Una teoría suya
- Unos recuerdos nuestros
- Una tradición tuya
- Un conflicto suyo
- Unas costumbres vuestras
- Un secreto mío
- Una oportunidad nuestra
- Unos planes tuyos

=== EJERCICIOS ===

Crea una frase con: un teorema + vuestro
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Documents/Programa- Práctica de la construcción "un amigo mío"2.py

=== CONSTRUCCIONES DISPONIBLES ===
1. Artículo indefinido + sustantivo + posesivo
2. Determinante (algún/ningún) + sustantivo + posesivo
3. Artículo definido + sustantivo + posesivo (enfático)
4. Ver progreso
5. Salir

Selecciona una opción: 
= RESTART: /Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 207, in <module>
    app = SpanishConstructorGUI(root)
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 24, in __init__
    self.create_widgets()
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 107, in create_widgets
    self.update_content()
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 148, in update_content
    construccion = self.constructions[construccion_id]
AttributeError: 'SpanishConstructorGUI' object has no attribute 'constructions'. Did you mean: 'construccion_var'?
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 2068, in __call__
    return self.func(*args)
           ~~~~~~~~~^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 862, in callit
    func(*args)
    ~~~~^^^^^^^
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 161, in generate_new_exercise
    construccion = self.constructions[construccion_id]
                   ^^^^^^^^^^^^^^^^^^
AttributeError: 'SpanishConstructorGUI' object has no attribute 'constructions'. Did you mean: 'construccion_var'?

= RESTART: /Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 207, in <module>
    app = SpanishConstructorGUI(root)
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 24, in __init__
    self.create_widgets()
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 107, in create_widgets
    self.update_content()
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 148, in update_content
    construccion = self.constructions[construccion_id]
AttributeError: 'SpanishConstructorGUI' object has no attribute 'constructions'. Did you mean: 'construccion_var'?
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 2068, in __call__
    return self.func(*args)
           ~~~~~~~~~^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 862, in callit
    func(*args)
    ~~~~^^^^^^^
  File "/Users/jhernanacvdo/Desktop/Programa- Práctica de la construcción "un amigo mío"3tkinter.py", line 161, in generate_new_exercise
    construccion = self.constructions[construccion_id]
                   ^^^^^^^^^^^^^^^^^^
AttributeError: 'SpanishConstructorGUI' object has no attribute 'constructions'. Did you mean: 'construccion_var'?

= RESTART: /Users/jhernanacvdo/Desktop/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter.py", line 106, in <module>
    self.generar_btn = tk.Button(root, text="Generar y guardar 100 ejemplos", command=self.generar_ejemplos)
NameError: name 'self' is not defined

= RESTART: /Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py", line 133, in <module>
    app = SpanishConstructorGUI(root)
  File "/Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py", line 15, in __init__
    self.left_panel,
AttributeError: 'SpanishConstructorGUI' object has no attribute 'left_panel'

= RESTART: /Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py", line 133, in <module>
    app = SpanishConstructorGUI(root)
  File "/Users/jhernanacvdo/Documents/PRÁCTICA- CONSTRUCCIÓN 'UN AMIGO MÍO3_tkinter2.py", line 15, in __init__
    self.left_panel,
AttributeError: 'SpanishConstructorGUI' object has no attribute 'left_panel'

========================= RESTART: Shell =========================
