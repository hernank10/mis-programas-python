"""
Mini LOGO en Python
- Interfaz gráfica mínima con turtle (canvas embebido en Tkinter)
- Interprete de comandos estilo LOGO: FD, BK, RT, LT, PU, PD, REPEAT, COLOR, GOTO, CIRCLE, HOME, CLEAR, SPEED, PENWIDTH, LABEL, RUN, SAVE, LOAD, HELP, EXIT
- Soporta sintaxis de REPEAT n [ comandos ... ] y cadenas entre comillas para LABEL.

Cómo usar:
1. Ejecuta: python3 mini_logo.py
2. Escribe comandos en la caja de texto y pulsa Enter o "Ejecutar".
3. Ejemplos:
   FD 100
   RT 90
   REPEAT 4 [ FD 100 RT 90 ]
   COLOR red
   PENWIDTH 3
   LABEL "Hola LOGO"
   SAVE ejemplo.logo
   RUN ejemplo.logo

Autor: Generado por ChatGPT
"""

import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
import re
import shlex
import sys

class MiniLogo:
    def __init__(self, root):
        self.root = root
        root.title("Mini LOGO — Python")

        # Canvas de turtle
        self.canvas = ScrolledCanvas(root, width=800, height=600)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.screen = TurtleScreen(self.canvas)
        self.screen.setworldcoordinates(-400, -300, 400, 300)

        # Tortuga
        self.t = RawTurtle(self.screen)
        self.t.speed(0)

        # Panel de control
        ctrl = tk.Frame(root)
        ctrl.pack(side=tk.BOTTOM, fill=tk.X)

        self.entry = tk.Entry(ctrl)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind('<Return>', lambda e: self.run_line(self.entry.get()))

        btn = tk.Button(ctrl, text="Ejecutar", command=lambda: self.run_line(self.entry.get()))
        btn.pack(side=tk.LEFT)

        btn_clear = tk.Button(ctrl, text="Limpiar pantalla", command=self.clear)
        btn_clear.pack(side=tk.LEFT)

        btn_help = tk.Button(ctrl, text="Ayuda", command=self.show_help)
        btn_help.pack(side=tk.LEFT)

        self.log = tk.Text(root, height=6)
        self.log.pack(side=tk.BOTTOM, fill=tk.X)

        self._write("Mini LOGO listo. Escribe HELP para ver comandos.\n")

    # ---------------------- Utilidades de parsing ----------------------
    def tokenize(self, line):
        # Separa corchetes como tokens y respeta cadenas entre comillas
        tokens = re.findall(r"\[|\]|\"[^\"]*\"|'[^']*'|\S+", line)
        return tokens

    def extract_bracket_content(self, tokens, start_idx):
        # Espera que tokens[start_idx] == '['
        depth = 0
        content_tokens = []
        i = start_idx
        while i < len(tokens):
            tok = tokens[i]
            if tok == '[':
                depth += 1
                if depth > 1:
                    content_tokens.append(tok)
            elif tok == ']':
                depth -= 1
                if depth == 0:
                    return content_tokens, i
                else:
                    content_tokens.append(tok)
            else:
                content_tokens.append(tok)
            i += 1
        raise ValueError('Corchetes no balanceados')

    # ---------------------- Ejecutor ----------------------
    def run_line(self, line):
        self.entry.delete(0, tk.END)
        line = line.strip()
        if not line:
            return
        self._write('> ' + line + '\n')
        try:
            tokens = self.tokenize(line)
            self.execute_tokens(tokens)
        except Exception as e:
            self._write('Error: ' + str(e) + '\n')

    def execute_tokens(self, tokens):
        i = 0
        while i < len(tokens):
            tok = tokens[i].upper()
            # Mapeo de comandos simples
            if tok in ('FD', 'FORWARD'):
                val = float(tokens[i+1])
                self.t.forward(val)
                i += 2
            elif tok in ('BK', 'BACK'):
                val = float(tokens[i+1])
                self.t.backward(val)
                i += 2
            elif tok in ('RT', 'RIGHT'):
                val = float(tokens[i+1])
                self.t.right(val)
                i += 2
            elif tok in ('LT', 'LEFT'):
                val = float(tokens[i+1])
                self.t.left(val)
                i += 2
            elif tok in ('PU', 'PENUP'):
                self.t.penup(); i += 1
            elif tok in ('PD', 'PENDOWN'):
                self.t.pendown(); i += 1
            elif tok == 'COLOR' or tok == 'SETCOLOR':
                # Puede ser nombre de color o 3 valores RGB 0-255
                if i+1 >= len(tokens): raise ValueError('COLOR requiere argumento')
                arg = tokens[i+1]
                if re.match(r"^\d+$", arg) and i+3 < len(tokens):
                    r = int(tokens[i+1]); g = int(tokens[i+2]); b = int(tokens[i+3])
                    # turtle acepta colores en tuplas 0..1
                    self.t.pencolor((r/255, g/255, b/255))
                    i += 4
                else:
                    self.t.pencolor(arg)
                    i += 2
            elif tok == 'GOTO':
                x = float(tokens[i+1]); y = float(tokens[i+2])
                self.t.goto(x, y); i += 3
            elif tok == 'CIRCLE':
                r = float(tokens[i+1])
                self.t.circle(r); i += 2
            elif tok == 'HOME':
                self.t.home(); i += 1
            elif tok == 'CLEAR' or tok == 'CLS':
                self.clear(); i += 1
            elif tok == 'RESET':
                self.t.reset(); i += 1
            elif tok == 'SPEED':
                s = int(tokens[i+1]); self.t.speed(s); i += 2
            elif tok == 'PENWIDTH':
                w = float(tokens[i+1]); self.t.width(w); i += 2
            elif tok == 'LABEL' or tok == 'WRITE':
                # etiqueta: puede venir entre comillas
                arg = tokens[i+1]
                if arg.startswith('"') or arg.startswith("'"):
                    text = arg[1:-1]
                else:
                    text = arg
                self.t.write(text, font=("Arial", 12, "normal"))
                i += 2
            elif tok == 'REPEAT':
                # REPEAT n [ ... ]
                count = int(tokens[i+1])
                if tokens[i+2] != '[':
                    raise ValueError('REPEAT debe tener corchetes: REPEAT n [ ... ]')
                inner_tokens, j = self.extract_bracket_content(tokens, i+2)
                for _ in range(count):
                    self.execute_tokens(inner_tokens)
                i = j + 1
            elif tok == 'RUN' or tok == 'LOAD':
                # RUN filename
                fname = tokens[i+1].strip('"')
                self.run_file(fname)
                i += 2
            elif tok == 'SAVE':
                fname = tokens[i+1].strip('"')
                # Guardar la última línea en el archivo (simple)
                # Para conveniencia, pedimos al usuario todo un script en el diálogo
                rest = ' '.join(tokens[i+2:])
                with open(fname, 'a', encoding='utf-8') as f:
                    if rest:
                        f.write(rest + '\n')
                    else:
                        f.write('\n')
                self._write(f"Guardado a {fname}\n")
                i = len(tokens)
            elif tok == 'HELP':
                self.show_help(); i += 1
            elif tok == 'EXIT' or tok == 'QUIT':
                self._write('Saliendo...\n')
                self.root.quit(); return
            else:
                # Intenta interpretar como línea compuesta separada por ;
                # o comando desconocido
                # Si el token es '[' o ']', ignorar
                if tok in ('[', ']'):
                    i += 1
                    continue
                # intentar interpretar como comentario o comando de texto
                # Si hay punto y coma, separar subcomandos
                subline = ' '.join(tokens[i:])
                if ';' in subline:
                    parts = subline.split(';')
                    for p in parts:
                        p = p.strip()
                        if p:
                            self.execute_tokens(self.tokenize(p))
                    return
                raise ValueError(f'Comando desconocido: {tokens[i]}')

    # ---------------------- Operaciones de archivo ----------------------
    def run_file(self, fname):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    self._write('RUN> ' + line + '\n')
                    tokens = self.tokenize(line)
                    self.execute_tokens(tokens)
        except FileNotFoundError:
            self._write('Archivo no encontrado: ' + fname + '\n')

    # ---------------------- UI helpers ----------------------
    def clear(self):
        self.t.clear(); self.t.home(); self._write('Pantalla limpiada.\n')

    def show_help(self):
        h = (
            "Comandos disponibles:\n"
            "FD <n>, BK <n>, RT <grados>, LT <grados>\n"
            "PU, PD, COLOR <nombre|r g b>, PENWIDTH <n>, SPEED <0..10>\n"
            "GOTO x y, CIRCLE r, HOME, CLEAR, RESET\n"
            "LABEL \"texto\"\n"
            "REPEAT n [ ... ]  (ej: REPEAT 4 [ FD 100 RT 90 ])\n"
            "RUN <archivo>, SAVE <archivo>\n"
            "HELP, EXIT\n"
        )
        self._write(h)

    def _write(self, text):
        self.log.insert(tk.END, text)
        self.log.see(tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = MiniLogo(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
