#!/usr/bin/env python3
"""
LOGO Console Interactivo — Python

Características:
- Prompt interactivo: logo>
- Comandos: FD, BK, RT, LT, PU, PD, HOME, CLEAR, REPEAT, TO...END, MAKE, HISTORY, VARS
- Referencia a variables con :name
- Export PNG/SVG
- Historial con re-ejecución: !<n> (ej. !3)
"""

import math
import sys
from PIL import Image, ImageDraw
import svgwrite
import shlex
import ast
import operator

# ----------------- Evaluador seguro de expresiones -----------------
# Permite operaciones con + - * / (floats), números y variables (sustituidas)
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

def safe_eval(expr: str):
    """
    Evalúa la expresión numérica segura usando ast.
    Solo operadores básicos y números.
    """
    node = ast.parse(expr, mode='eval').body

    def _eval(n):
        if isinstance(n, ast.Num):
            return n.n
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -_eval(n.operand)
        if isinstance(n, ast.BinOp) and type(n.op) in SAFE_OPERATORS:
            left = _eval(n.left)
            right = _eval(n.right)
            return SAFE_OPERATORS[type(n.op)](left, right)
        raise ValueError(f"Expresión no permitida: {expr}")

    return _eval(node)

# ----------------- Motor LOGO (vector interno) -----------------
class LogoEngine:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0  # grados, 0 = derecha, aumenta a la izquierda
        self.pen_down = True
        self.lines = []  # lista de ((x1,y1),(x2,y2))
        self.procedures = {}  # name -> (arg_names, body_tokens)
        self.vars = {}  # nombre -> valor (numérico o string)
        self.history = []  # lista de líneas ingresadas

    # Movimiento básico
    def _move_to(self, nx, ny):
        if self.pen_down:
            self.lines.append(((self.x, self.y), (nx, ny)))
        self.x, self.y = nx, ny

    def fd(self, n):
        rad = math.radians(self.angle)
        nx = self.x + n * math.cos(rad)
        ny = self.y + n * math.sin(rad)
        self._move_to(nx, ny)

    def bk(self, n):
        self.fd(-n)

    def rt(self, deg):
        self.angle -= deg

    def lt(self, deg):
        self.angle += deg

    def pu(self):
        self.pen_down = False

    def pd(self):
        self.pen_down = True

    def home(self):
        self._move_to(0.0, 0.0)
        self.angle = 0.0

    def clear(self):
        self.lines.clear()
        self.home()

    # Export PNG
    def export_png(self, filename):
        if not self.lines:
            print("No hay líneas para exportar.")
            return
        xs = [p[0] for l in self.lines for p in l]
        ys = [p[1] for l in self.lines for p in l]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        w = max(100, int(maxx - minx + 20))
        h = max(100, int(maxy - miny + 20))
        img = Image.new("RGB", (w, h), "white")
        draw = ImageDraw.Draw(img)
        for (x1, y1), (x2, y2) in self.lines:
            draw.line((x1 - minx + 10, h - (y1 - miny + 10),
                       x2 - minx + 10, h - (y2 - miny + 10)), fill="black", width=2)
        img.save(filename)
        print(f"PNG exportado a {filename}")

    # Export SVG
    def export_svg(self, filename):
        if not self.lines:
            print("No hay líneas para exportar.")
            return
        dwg = svgwrite.Drawing(filename)
        for (x1, y1), (x2, y2) in self.lines:
            dwg.add(dwg.line(start=(x1, -y1), end=(x2, -y2), stroke="black"))
        dwg.save()
        print(f"SVG exportado a {filename}")

# ----------------- Intérprete -----------------
class LogoInterpreter:
    def __init__(self):
        self.engine = LogoEngine()

    def substitute_vars(self, token):
        # token puede contener :var o ser una cadena literal entre comillas
        if token.startswith('"') and token.endswith('"'):
            return token[1:-1]
        if token.startswith(':'):
            name = token[1:]
            if name in self.engine.vars:
                return str(self.engine.vars[name])
            else:
                raise ValueError(f"Variable no definida: {name}")
        return token

    def expr_value(self, expr_tokens):
        # expr_tokens: lista de tokens que forman expresión, unir y sustituir :vars
        expr = ' '.join(expr_tokens)
        # Reemplazar :var por su valor numérico si existe
        parts = expr.split()
        replaced_parts = []
        for p in parts:
            if p.startswith(':'):
                name = p[1:]
                if name in self.engine.vars:
                    replaced_parts.append(str(self.engine.vars[name]))
                else:
                    raise ValueError(f"Variable no definida: {name}")
            else:
                replaced_parts.append(p)
        s = ' '.join(replaced_parts)
        # evaluar seguro
        try:
            return float(safe_eval(s))
        except Exception as e:
            raise ValueError(f"Error al evaluar expresión '{s}': {e}")

    def tokenize_line(self, line):
        # Usa shlex para respetar comillas
        return shlex.split(line)

    def run_line(self, line):
        line = line.strip()
        if not line:
            return
        # añadir a historial
        self.engine.history.append(line)
        tokens = self.tokenize_line(line)
        self._execute_tokens(tokens)

    def _execute_tokens(self, tokens):
        i = 0
        while i < len(tokens):
            tok = tokens[i].upper()

            if tok == 'FD':
                val = self.expr_value(tokens[i+1:i+2])
                self.engine.fd(val); i += 2; continue

            if tok == 'BK':
                val = self.expr_value(tokens[i+1:i+2])
                self.engine.bk(val); i += 2; continue

            if tok == 'RT':
                val = self.expr_value(tokens[i+1:i+2])
                self.engine.rt(val); i += 2; continue

            if tok == 'LT':
                val = self.expr_value(tokens[i+1:i+2])
                self.engine.lt(val); i += 2; continue

            if tok == 'PU':
                self.engine.pu(); i += 1; continue

            if tok == 'PD':
                self.engine.pd(); i += 1; continue

            if tok == 'HOME':
                self.engine.home(); i += 1; continue

            if tok == 'CLEAR':
                self.engine.clear(); i += 1; continue

            if tok == 'MAKE':
                # MAKE "x 100  or MAKE x 100
                name_token = tokens[i+1]
                if name_token.startswith('"'):
                    name = name_token[1:]
                else:
                    name = name_token
                # the value expression may be multiple tokens
                val = self.expr_value(tokens[i+2:])
                self.engine.vars[name] = val
                print(f'Variable {name} = {val}')
                return

            if tok == 'VARS':
                print("Variables:")
                for k, v in self.engine.vars.items():
                    print(f"  {k} = {v}")
                return

            if tok == 'REPEAT':
                count = int(self.expr_value(tokens[i+1:i+2]))
                # block starts at next token expecting [ 
                if tokens[i+2] != '[':
                    raise ValueError("Sintaxis REPEAT n [ ... ]")
                # extraer bloque respetando anidamiento
                j = i+3
                depth = 1
                block = []
                while j < len(tokens):
                    if tokens[j] == '[':
                        depth += 1
                    elif tokens[j] == ']':
                        depth -= 1
                        if depth == 0:
                            break
                    block.append(tokens[j])
                    j += 1
                for _ in range(count):
                    # ejecutar copia del bloque (puede contener :vars)
                    self._execute_tokens(block.copy())
                return

            if tok == 'TO':
                # definir procedimiento: TO name :a :b ...  (cuerpo hasta END en la misma línea
                # o en múltiples líneas — aquí soportamos definición en varias líneas hasta END token ingresado)
                name = tokens[i+1]
                arg_names = []
                j = i+2
                while j < len(tokens) and tokens[j].startswith(':'):
                    arg_names.append(tokens[j][1:])
                    j += 1
                # Si no hay END en la misma línea, leer más líneas hasta END
                body_tokens = tokens[j:]
                if 'END' not in [t.upper() for t in body_tokens]:
                    # leer líneas adicionales de entrada hasta END
                    print(f"Definiendo procedimiento {name}. Escribe líneas; termina con 'END'.")
                    extra = []
                    while True:
                        try:
                            nxt = input('... ')
                        except EOFError:
                            raise KeyboardInterrupt()
                        if nxt.strip().upper() == 'END':
                            break
                        extra.extend(self.tokenize_line(nxt))
                    body_tokens = body_tokens + extra
                # truncar después de END si existe
                if 'END' in [t.upper() for t in body_tokens]:
                    end_idx = [t.upper() for t in body_tokens].index('END')
                    body_tokens = body_tokens[:end_idx]
                self.engine.procedures[name.lower()] = (arg_names, body_tokens)
                print(f"Procedimiento {name} definido con args {arg_names}")
                return

            # llamada a procedimiento si existe
            if tok.lower() in self.engine.procedures:
                procname = tok.lower()
                arg_names, body = self.engine.procedures[procname]
                call_args = []
                for k in range(len(arg_names)):
                    call_args.append(self.substitute_vars(tokens[i+1+k]))
                # crear mapa temporal de variables (slotting)
                backup = dict(self.engine.vars)
                for name, val in zip(arg_names, call_args):
                    # val puede ser literal string o numérico
                    try:
                        vnum = float(val)
                        self.engine.vars[name] = vnum
                    except:
                        try:
                            # if it's expression-like, evaluate
                            self.engine.vars[name] = float(safe_eval(str(val)))
                        except:
                            self.engine.vars[name] = val
                # ejecutar cuerpo (tokens) - hacemos copia
                try:
                    self._execute_tokens(body.copy())
                finally:
                    # Restaurar variables previas (no persistir args)
                    self.engine.vars = backup
                i += 1 + len(arg_names)
                continue

            if tok == 'HISTORY':
                for idx, line in enumerate(self.engine.history, start=1):
                    print(f"{idx}: {line}")
                return

            if tok.startswith('!'):
                # re-ejecutar historial: !n
                try:
                    idx = int(tok[1:]) - 1
                    hline = self.engine.history[idx]
                    print(f"Re-ejecutando [{idx+1}]: {hline}")
                    self.run_line(hline)
                    return
                except Exception as e:
                    print("Historial inválido:", e)
                    return

            if tok == 'EXPORTPNG':
                fname = tokens[i+1].strip('"')
                self.engine.export_png(fname)
                return

            if tok == 'EXPORTSVG':
                fname = tokens[i+1].strip('"')
                self.engine.export_svg(fname)
                return

            if tok in ('QUIT', 'EXIT'):
                print("Saliendo.")
                sys.exit(0)

            # comando desconocido
            print(f"Comando desconocido o no soportado: {tokens[i]}")
            return

# ----------------- Bucle interactivo -----------------
def repl():
    interp = LogoInterpreter()
    print("LOGO Interactivo — escribe HELP para ver comandos. Ctrl-D para salir.")
    while True:
        try:
            line = input("logo> ")
        except EOFError:
            print("\nSaliendo.")
            break
        if not line.strip():
            continue
        if line.strip().upper() == 'HELP':
            print("Comandos: FD n, BK n, RT deg, LT deg, PU, PD, HOME, CLEAR")
            print("REPEAT n [ ... ], TO name :arg1 ... END (definir), MAKE \"x 10")
            print("HISTORY, !n (re-ejecutar), VARS, EXPORTPNG \"file.png\", EXPORTSVG \"file.svg\"")
            print("QUIT / EXIT")
            continue
        try:
            interp.run_line(line)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
