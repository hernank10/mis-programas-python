#!/usr/bin/env python3
"""


Features:
- Preprocess image to improve OCR
- Extract math expression string via pytesseract
- Parse with SymPy and try to solve / simplify
- Provide human-readable step hints for linear/quadratic/simplify
- CLI and minimal Tkinter GUI for loading images

Limitations:
- OCR is error-prone on handwritten math or poor photos.
- Step-by-step solver handles common simple cases; more advanced reasoning needs specialized CAS step modules.
"""
import os
import sys
import argparse
import tempfile
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import math
from sympy import symbols, Eq, solve, simplify, factor, Poly
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.core.sympify import SympifyError

# If on Windows and tesseract isn't on PATH, set this:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -------------------------
# Image preprocessing
# -------------------------
def preprocess_image_for_ocr(img_path, debug=False):
    """Return a processed grayscale image suitable for OCR as a PIL Image."""
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {img_path}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize (if very small)
    h, w = gray.shape
    scale = max(1, int(800 / max(h, w)))
    if scale > 1:
        gray = cv2.resize(gray, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

    # Apply bilateral filter to preserve edges
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # Adaptive threshold
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 31, 10)

    # Invert if background is dark
    # We want black text on white background for tesseract
    white_ratio = np.mean(th == 255)
    if white_ratio < 0.5:
        th = cv2.bitwise_not(th)

    # Morphological opening to remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

    # Deskew: compute angle via moments of edges
    coords = np.column_stack(np.where(opened < 255))
    if coords.shape[0] > 0:
        rect = cv2.minAreaRect(coords)
        angle = rect[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        if abs(angle) > 0.1:
            (h, w) = opened.shape
            M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1.0)
            opened = cv2.warpAffine(opened, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
            if debug:
                print(f"Deskew angle: {angle:.2f}")
    # Optionally blur/sharpen
    # Final cleanup: median blur
    opened = cv2.medianBlur(opened, 3)

    # Convert to PIL Image for pytesseract
    from PIL import Image
    pil = Image.fromarray(opened)
    return pil

# -------------------------
# OCR extraction
# -------------------------
def ocr_image_to_text(pil_image, whitelist=None, psm=6):
    """
    Run pytesseract on a PIL image and return cleaned text.
    whitelist: string of allowed characters (helps reduce noise)
    psm: Page segmentation mode for tesseract
    """
    config = f'--psm {psm}'
    if whitelist:
        config += f' -c tessedit_char_whitelist={whitelist}'
    raw = pytesseract.image_to_string(pil_image, config=config)
    # Clean common OCR mistakes for math: unicode minus, etc.
    txt = raw.strip()
    txt = txt.replace('−', '-').replace('—', '-').replace('–', '-')
    txt = txt.replace('\n', ' ').replace('\r', ' ')
    # Remove multiple spaces
    txt = ' '.join(txt.split())
    # sometimes tesseract returns 'x' as 'x' or 'χ' — keep latin letters
    return txt

# -------------------------
# Parsing to sympy
# -------------------------
transformations = (standard_transformations + (implicit_multiplication_application,))

def parse_math_expression(s):
    """
    Try to parse string s as:
    - an equation with '=' -> returns ('eq', sympy.Eq(lhs, rhs))
    - an expression -> returns ('expr', sympy expression)
    Raises SympifyError if cannot parse.
    """
    s = s.strip()
    # fix common OCR confusions: replace 'x' if used as multiplication? We'll keep x variable.
    # If there is an '=' treat as equation
    if '=' in s:
        parts = s.split('=')
        if len(parts) >= 2:
            lhs = parts[0]
            rhs = '='.join(parts[1:])
            try:
                L = parse_expr(lhs, transformations=transformations)
                R = parse_expr(rhs, transformations=transformations)
                return 'eq', Eq(L, R)
            except SympifyError as e:
                raise
    else:
        try:
            E = parse_expr(s, transformations=transformations)
            return 'expr', E
        except SympifyError:
            # attempt some mild cleanup: replace unicode chars
            s2 = s.replace('^', '**')
            E = parse_expr(s2, transformations=transformations)
            return 'expr', E

# -------------------------
# Solver & step generator
# -------------------------
def explain_linear_equation(eq):
    """
    eq is sympy Eq: ax + b = c or similar. Return steps list and solution(s).
    """
    # attempt to rearrange to form ax + b = 0 style
    try:
        # get lhs - rhs = 0
        expr = eq.lhs - eq.rhs
        sym = list(expr.free_symbols)
        if len(sym) != 1:
            # multiple variables -> general solve
            sols = solve(eq)
            return ["Multiple variables or complex equation; solved using general solver."], sols
        var = sym[0]
        # convert to coefficients for polynomial degree <=2
        p = Poly(expr, var)
        deg = p.degree()
        if deg == 1:
            a = p.coeffs()[0]
            b = p.coeffs()[1] if len(p.coeffs())>1 else 0
            # steps: move constant, divide by coefficient
            steps = []
            # Show original
            steps.append(f"Start: {eq}")
            # Move constant to RHS: ax = -b
            # But compute symbolic: isolate var
            isolated = solve(eq, var)
            # We will craft typical steps:
            # step 1: subtract constant term
            # get terms:
            # Do symbolic manipulation to show: ax + b = c -> ax = c - b
            # We can do eq.lhs - constant etc; simpler form: isolate(var)
            # create steps via sympy.simplify
            steps.append(f"Isolate {var}: {var} = ({eq.rhs} - ({expr.subs(var,0)} - 0)) / ({a})  (conceptual)")
            # fallback: provide automatic solution string
            return steps, isolated
        elif deg == 2:
            # quadratic: use quadratic formula and provide steps with discriminant
            var = p.gens[0]
            a = p.coeffs()[0]
            b = p.coeffs()[1] if len(p.coeffs())>1 else 0
            c = p.coeffs()[2] if len(p.coeffs())>2 else 0
            steps = []
            steps.append(f"Equation is quadratic: {a}*{var}^2 + {b}*{var} + {c} = 0")
            steps.append(f"Compute discriminant: D = b^2 - 4ac = ({b})^2 - 4*({a})*({c})")
            Dval = b**2 - 4*a*c
            steps.append(f"D = {Dval}")
            if Dval < 0:
                steps.append("Discriminant < 0: complex roots")
            else:
                steps.append(f"Solutions: ({-b} ± sqrt({Dval})) / (2*{a})")
            sols = solve(eq)
            return steps, sols
        else:
            # higher degree: fallback to general solve
            sols = solve(eq)
            return [f"Higher-degree polynomial (deg={deg}), solved numerically/symbolically."], sols
    except Exception as e:
        # fallback
        sols = solve(eq)
        return [f"Could not generate step-by-step: {e}"], sols

def explain_expression(expr):
    """Return explanation steps for an expression (simplify, factor)"""
    steps = []
    try:
        steps.append(f"Original expression: {expr}")
        s = simplify(expr)
        if s != expr:
            steps.append(f"Simplified: {s}")
        f = factor(expr)
        if f != expr and f != s:
            steps.append(f"Factored: {f}")
        # try expand as alternative
        ex = expr.expand()
        if ex != expr and ex != s and ex != f:
            steps.append(f"Expanded: {ex}")
        if len(steps) == 1:
            steps.append("No simplification found; expression appears already simple or needs different methods.")
        return steps, s
    except Exception as e:
        return [f"Error simplifying: {e}"], expr

def analyze_parsed(parsed):
    """
    parsed: tuple ('eq', Eq) or ('expr', sympy expr)
    Returns dict {type, steps, solution}
    """
    typ, content = parsed
    if typ == 'eq':
        steps, sols = explain_linear_equation(content)
        return {'type': 'equation', 'steps': steps, 'solution': sols}
    else:
        steps, simplified = explain_expression(content)
        return {'type': 'expression', 'steps': steps, 'simplified': simplified}

# -------------------------
# High-level pipeline
# -------------------------
def process_image_file(path, debug=False):
    pil = preprocess_image_for_ocr(path, debug=debug)
    # whitelist: digits, operators, letters, parentheses, ^, /, .
    whitelist = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/^=(). '
    txt = ocr_image_to_text(pil, whitelist=whitelist, psm=6)
    if debug:
        print("OCR text:", txt)
    if not txt:
        raise ValueError("No text recognized by OCR.")
    # try parse
    try:
        parsed = parse_math_expression(txt)
    except Exception as e:
        # try small fixes: replace caret with ** and try again
        fixed = txt.replace('^','**')
        parsed = parse_math_expression(fixed)
    analysis = analyze_parsed(parsed)
    return {
        'raw_text': txt,
        'parsed': parsed,
        'analysis': analysis
    }

# -------------------------
# CLI
# -------------------------
def cli_solve_image(args):
    res = process_image_file(args.image, debug=args.debug)
    print("OCR text:")
    print(res['raw_text'])
    print("\nAnalysis:")
    a = res['analysis']
    for s in a['steps']:
        print("-", s)
    if a['type'] == 'equation':
        print("\nSolution(s):", a['solution'])
    else:
        print("\nSimplified:", a.get('simplified', 'n/a'))

def build_argparser():
    p = argparse.ArgumentParser(description="Photomath-like OCR + SymPy prototype")
    sub = p.add_subparsers(dest='cmd')
    s1 = sub.add_parser('solve_image', help='Process an image and attempt to solve')
    s1.add_argument('--image', '-i', required=True)
    s1.add_argument('--debug', action='store_true')
    sub.add_parser('gui', help='Launch minimal GUI')
    return p

# -------------------------
# Minimal GUI (Tkinter)
# -------------------------
class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Photomath-like OCR demo")
        self.geometry("900x700")
        self.img_path = None
        top = tk.Frame(self); top.pack(fill=tk.X, pady=6)
        tk.Button(top, text="Open Image", command=self.open_image).pack(side=tk.LEFT, padx=6)
        tk.Button(top, text="Process", command=self.process_current).pack(side=tk.LEFT, padx=6)
        tk.Button(top, text="Quit", command=self.quit).pack(side=tk.RIGHT, padx=6)
        mid = tk.Frame(self); mid.pack(fill=tk.BOTH, expand=False)
        self.canvas = tk.Canvas(mid, width=640, height=360, bg='grey')
        self.canvas.pack(pady=6)
        right = tk.Frame(self); right.pack(fill=tk.BOTH, expand=True)
        tk.Label(right, text="OCR / Parsed / Steps:").pack(anchor=tk.W)
        self.out = scrolledtext.ScrolledText(right, wrap=tk.WORD, width=60, height=30)
        self.out.pack(fill=tk.BOTH, expand=True)
        self.pil_image = None
    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.tif;*.bmp")])
        if not path:
            return
        self.img_path = path
        # load small preview
        from PIL import Image, ImageTk
        im = Image.open(path)
        im.thumbnail((640,360))
        self.pil_image = ImageTk.PhotoImage(im)
        self.canvas.delete("all")
        self.canvas.create_image(320,180, image=self.pil_image)
    def process_current(self):
        if not self.img_path:
            messagebox.showwarning("No image", "Select an image first")
            return
        try:
            res = process_image_file(self.img_path, debug=False)
            self.out.delete('1.0', tk.END)
            self.out.insert(tk.END, "OCR text:\n")
            self.out.insert(tk.END, res['raw_text'] + "\n\n")
            parsed = res['parsed']
            self.out.insert(tk.END, f"Parsed type: {parsed[0]}\n{parsed[1]}\n\n")
            self.out.insert(tk.END, "Steps:\n")
            for s in res['analysis']['steps']:
                self.out.insert(tk.END, "- " + s + "\n")
            if res['analysis']['type'] == 'equation':
                self.out.insert(tk.END, "\nSolutions: " + str(res['analysis']['solution']) + "\n")
            else:
                self.out.insert(tk.END, f"\nSimplified: {res['analysis'].get('simplified')}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# -------------------------
# Main
# -------------------------
def main():
    parser = build_argparser()
    args = parser.parse_args()
    if args.cmd == 'solve_image':
        cli_solve_image(args)
    elif args.cmd == 'gui':
        app = SimpleGUI()
        app.mainloop()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
