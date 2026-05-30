Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /Users/jhernanacvdo/Desktop/oraciones_anticipacionS.py
Error: [Errno 2] No such file or directory: 'oraciones_anticipacion.json'

= RESTART: /Users/jhernanacvdo/Desktop/oraciones_anticipacionS.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/oraciones_anticipacionS.py", line 3, in <module>
    with open('oraciones_anticipacion.json', 'r', encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'oraciones_anticipacion.json'

= RESTART: /Users/jhernanacvdo/Desktop/oraciones_anticipacionS.py
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/oraciones_anticipacionS.py", line 3, in <module>
    with open('oraciones_anticipacion.json', 'r', encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'oraciones_anticipacion.json'

= RESTART: /Users/jhernanacvdo/Documents/oraciones_anticipacionS.py
Error: El archivo no existe en la ruta especificada.
>>> 
= RESTART: /Users/jhernanacvdo/Documents/oraciones_anticipacion.json
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Documents/oraciones_anticipacion.json", line 4, in <module>
    datos = json.load(f)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
