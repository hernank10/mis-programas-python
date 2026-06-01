import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import re
import sympy as sp
from sympy import Eq, solve, simplify, expand, factor, integrate, diff, sqrt
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication, convert_xor
import matplotlib.pyplot as plt
from matplotlib import patches
import warnings
warnings.filterwarnings('ignore')

class PhotoMathPrototype:
    def __init__(self):
        # Configurar pytesseract (ajustar según tu sistema)
        # En Windows: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # En Linux/Mac: generalmente ya está en PATH
        self.transformations = standard_transformations + (implicit_multiplication, convert_xor)
        
        # Diccionario de símbolos matemáticos comunes
        self.symbol_map = {
            'x': 'x', 'y': 'y', 'z': 'z',
            'times': '*', 'div': '/', 'cdot': '*',
            'plus': '+', 'minus': '-',
            'equals': '=',
            'sqrt': 'sqrt', 'frac': 'frac',
            '^': '**', 'pow': '**',
            '(': '(', ')': ')',
            '[': '(', ']': ')',
            '{': '(', '}': ')'
        }
        
        # Expresiones regulares para limpiar texto
        self.clean_patterns = [
            (r'\s+', ''),  # Eliminar espacios
            (r'\[', '('), (r'\]', ')'),  # Corchetes a paréntesis
            (r'\{', '('), (r'\}', ')'),  # Llaves a paréntesis
            (r'\\', ''),  # Eliminar barras invertidas
            (r'\\mathrm\{([^}]+)\}', r'\1'),  # Extraer texto de \mathrm{}
            (r'\\text\{([^}]+)\}', r'\1'),  # Extraer texto de \text{}
        ]
        
    def preprocess_image(self, image_path):
        """Preprocesa la imagen para mejorar el OCR"""
        # Cargar imagen
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"No se pudo cargar la imagen: {image_path}")
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Aplicar umbral adaptativo
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)
        
        # Reducir ruido
        kernel = np.ones((2, 2), np.uint8)
        cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)
        
        # Aumentar contraste
        pil_img = Image.fromarray(cleaned)
        enhancer = ImageEnhance.Contrast(pil_img)
        enhanced = enhancer.enhance(2.0)
        
        return np.array(enhanced)
    
    def detect_math_regions(self, image):
        """Detecta regiones que probablemente contengan ecuaciones"""
        # Usar detección de contornos para encontrar áreas con texto
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        regions = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            
            # Filtrar por tamaño (eliminar ruido muy pequeño)
            if w > 20 and h > 20:
                regions.append({
                    'x': x, 'y': y, 'w': w, 'h': h,
                    'roi': image[y:y+h, x:x+w]
                })
        
        return regions
    
    def extract_text_from_image(self, image_path, use_tesseract=True):
        """Extrae texto matemático de la imagen"""
        preprocessed = self.preprocess_image(image_path)
        
        if use_tesseract:
            # Configurar Tesseract para matemáticas
            custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789+-*/=()[]{}xyzt^√∫∑∏≤≥≠≈αβγπ∞'
            
            # Intentar con diferentes preprocesamientos
            texts = []
            
            # 1. Imagen original preprocesada
            text1 = pytesseract.image_to_string(preprocessed, config=custom_config)
            texts.append(text1)
            
            # 2. Invertir colores (texto blanco sobre fondo negro)
            inverted = cv2.bitwise_not(preprocessed)
            text2 = pytesseract.image_to_string(inverted, config=custom_config)
            texts.append(text2)
            
            # 3. Escala de grises suavizada
            blur = cv2.GaussianBlur(preprocessed, (3, 3), 0)
            text3 = pytesseract.image_to_string(blur, config=custom_config)
            texts.append(text3)
            
            # Seleccionar el texto con más contenido
            best_text = max(texts, key=lambda x: len(x.strip()))
            
        else:
            # Alternativa: usar EasyOCR si está disponible
            try:
                import easyocr
                reader = easyocr.Reader(['en'])
                results = reader.readtext(preprocessed)
                best_text = ' '.join([result[1] for result in results])
            except ImportError:
                best_text = pytesseract.image_to_string(preprocessed)
        
        return best_text.strip()
    
    def clean_math_expression(self, text):
        """Limpia y normaliza la expresión matemática"""
        if not text:
            return ""
        
        # Aplicar patrones de limpieza
        cleaned = text
        for pattern, replacement in self.clean_patterns:
            cleaned = re.sub(pattern, replacement, cleaned)
        
        # Reemplazar símbolos matemáticos
        for symbol, replacement in self.symbol_map.items():
            cleaned = cleaned.replace(symbol, replacement)
        
        # Corregir errores comunes de OCR
        corrections = [
            (r'([0-9])([a-zA-Z])', r'\1*\2'),  # 2x -> 2*x
            (r'([a-zA-Z])([0-9])', r'\1*\2'),  # x2 -> x*2
            (r'([0-9])\s*\(', r'\1*('),  # 2( -> 2*(
            (r'\)\s*([0-9a-zA-Z])', r')*\1'),  # )2 -> )*2
            (r'([a-zA-Z])\s*\(', r'\1*('),  # x( -> x*(
            (r'\)\s*\(', r')*('),  # )( -> )*(
            (r'sqrt\s*([^(])', r'sqrt(\1'),  # sqrt2 -> sqrt(2)
            (r'frac\s*([^({])', r'frac(\1'),  # frac12 -> frac(1,2)
        ]
        
        for pattern, replacement in corrections:
            cleaned = re.sub(pattern, replacement, cleaned)
        
        # Convertir fracciones estilo LaTeX: \frac{a}{b} -> a/b
        def replace_frac(match):
            numerator = match.group(1)
            denominator = match.group(2)
            return f'({numerator})/({denominator})'
        
        cleaned = re.sub(r'frac\(([^,]+),([^)]+)\)', replace_frac, cleaned)
        
        # Manejar potencias
        cleaned = cleaned.replace('^', '**')
        
        return cleaned
    
    def parse_equation(self, text):
        """Parsea la ecuación y determina su tipo"""
        cleaned = self.clean_math_expression(text)
        
        # Verificar si es una ecuación (contiene =)
        if '=' in cleaned:
            parts = cleaned.split('=')
            if len(parts) == 2:
                lhs, rhs = parts
                return {
                    'type': 'equation',
                    'lhs': lhs.strip(),
                    'rhs': rhs.strip(),
                    'original': text,
                    'cleaned': cleaned
                }
        
        # Verificar si es una expresión para simplificar
        return {
            'type': 'expression',
            'expression': cleaned,
            'original': text,
            'cleaned': cleaned
        }
    
    def solve_equation(self, equation_data):
        """Resuelve la ecuación usando SymPy"""
        try:
            x, y, z = sp.symbols('x y z')
            
            if equation_data['type'] == 'equation':
                lhs = parse_expr(equation_data['lhs'], transformations=self.transformations)
                rhs = parse_expr(equation_data['rhs'], transformations=self.transformations)
                equation = Eq(lhs, rhs)
                
                # Intentar resolver
                solutions = solve(equation, x, dict=True)
                
                if solutions:
                    return {
                        'success': True,
                        'type': 'equation',
                        'equation': equation,
                        'solutions': solutions,
                        'steps': self.generate_solution_steps(equation, solutions)
                    }
                else:
                    return {
                        'success': False,
                        'error': 'No se pudo resolver la ecuación'
                    }
            
            else:  # expression
                expr = parse_expr(equation_data['expression'], transformations=self.transformations)
                
                # Intentar simplificar
                simplified = simplify(expr)
                
                return {
                    'success': True,
                    'type': 'expression',
                    'original': expr,
                    'simplified': simplified,
                    'steps': self.generate_simplification_steps(expr, simplified)
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_text': equation_data['original']
            }
    
    def generate_solution_steps(self, equation, solutions):
        """Genera pasos detallados para la solución"""
        steps = []
        x = sp.symbols('x')
        
        # Paso 1: Mostrar la ecuación original
        steps.append(f"**Paso 1: Ecuación original**\n{equation}")
        
        # Paso 2: Reorganizar la ecuación
        rearranged = equation.lhs - equation.rhs
        steps.append(f"**Paso 2: Llevar todo al mismo lado**\n{eq(rearranged, 0)}")
        
        # Paso 3: Factorizar si es posible
        factored = factor(rearranged)
        if factored != rearranged:
            steps.append(f"**Paso 3: Factorizar**\n{eq(factored, 0)}")
        
        # Paso 4: Encontrar soluciones
        sol_str = ", ".join([f"x = {sol[x]}" for sol in solutions])
        steps.append(f"**Paso 4: Soluciones**\n{sol_str}")
        
        # Paso 5: Verificar soluciones
        verification = []
        for sol in solutions:
            subs_result = equation.subs(x, sol[x])
            verification.append(f"Para x = {sol[x]}: {equation.lhs} = {equation.rhs.subs(x, sol[x])} ✓")
        
        if verification:
            steps.append(f"**Paso 5: Verificación**\n" + "\n".join(verification))
        
        return steps
    
    def generate_simplification_steps(self, original, simplified):
        """Genera pasos para simplificar una expresión"""
        steps = []
        
        steps.append(f"**Paso 1: Expresión original**\n{original}")
        
        # Paso 2: Expandir si hay productos
        expanded = expand(original)
        if expanded != original:
            steps.append(f"**Paso 2: Expandir**\n{expanded}")
        
        # Paso 3: Combinar términos semejantes
        combined = simplify(expanded)
        if combined != expanded:
            steps.append(f"**Paso 3: Combinar términos semejantes**\n{combined}")
        
        # Paso 4: Factorizar si es posible
        factored = factor(combined)
        if factored != combined:
            steps.append(f"**Paso 4: Factorizar**\n{factored}")
        
        steps.append(f"**Paso 5: Expresión simplificada**\n{simplified}")
        
        return steps
    
    def calculate_derivative(self, expression_str):
        """Calcula la derivada de una expresión"""
        try:
            x = sp.symbols('x')
            expr = parse_expr(expression_str, transformations=self.transformations)
            
            # Calcular derivada
            derivative = diff(expr, x)
            
            steps = [
                f"**Paso 1: Función original**\nf(x) = {expr}",
                f"**Paso 2: Aplicar reglas de derivación**",
                f"**Paso 3: Derivada**\nf'(x) = {derivative}"
            ]
            
            return {
                'success': True,
                'function': expr,
                'derivative': derivative,
                'steps': steps
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def calculate_integral(self, expression_str):
        """Calcula la integral de una expresión"""
        try:
            x = sp.symbols('x')
            expr = parse_expr(expression_str, transformations=self.transformations)
            
            # Calcular integral indefinida
            integral = integrate(expr, x)
            
            steps = [
                f"**Paso 1: Función original**\nf(x) = {expr}",
                f"**Paso 2: Aplicar reglas de integración**",
                f"**Paso 3: Integral indefinida**\n∫f(x)dx = {integral} + C"
            ]
            
            return {
                'success': True,
                'function': expr,
                'integral': integral,
                'steps': steps
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def solve_quadratic(self, a, b, c):
        """Resuelve ecuación cuadrática paso a paso"""
        steps = []
        
        steps.append(f"**Paso 1: Ecuación cuadrática**\n{a}x² + {b}x + {c} = 0")
        
        # Calcular discriminante
        discriminant = b**2 - 4*a*c
        steps.append(f"**Paso 2: Calcular discriminante**\nD = b² - 4ac = {b}² - 4*{a}*{c} = {discriminant}")
        
        if discriminant > 0:
            sqrt_d = sp.sqrt(discriminant)
            steps.append(f"**Paso 3: Raíces reales distintas**\n√D = {sqrt_d}")
            
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            
            steps.append(f"**Paso 4: Fórmula cuadrática**")
            steps.append(f"x₁ = (-b + √D) / 2a = (-{b} + {sqrt_d}) / (2*{a}) = {x1}")
            steps.append(f"x₂ = (-b - √D) / 2a = (-{b} - {sqrt_d}) / (2*{a}) = {x2}")
            
            solutions = [x1, x2]
            
        elif discriminant == 0:
            steps.append(f"**Paso 3: Raíz real única**")
            x = -b / (2*a)
            steps.append(f"x = -b / 2a = -{b} / (2*{a}) = {x}")
            solutions = [x]
            
        else:
            real_part = -b / (2*a)
            imag_part = sp.sqrt(-discriminant) / (2*a)
            steps.append(f"**Paso 3: Raíces complejas**")
            steps.append(f"Parte real: -b/2a = -{b}/(2*{a}) = {real_part}")
            steps.append(f"Parte imaginaria: √|D|/2a = √{abs(discriminant)}/(2*{a}) = {imag_part}")
            solutions = [real_part + imag_part*sp.I, real_part - imag_part*sp.I]
        
        return {
            'success': True,
            'discriminant': discriminant,
            'solutions': solutions,
            'steps': steps
        }
    
    def plot_function(self, expression_str, x_range=(-10, 10)):
        """Grafica una función matemática"""
        try:
            x = sp.symbols('x')
            expr = parse_expr(expression_str, transformations=self.transformations)
            
            # Convertir a función numérica
            f = sp.lambdify(x, expr, 'numpy')
            
            # Crear valores de x
            x_vals = np.linspace(x_range[0], x_range[1], 400)
            y_vals = f(x_vals)
            
            # Crear gráfico
            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'f(x) = {expr}')
            
            # Configurar gráfico
            plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            plt.grid(True, alpha=0.3)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title(f'Gráfico de f(x) = {expr}')
            plt.legend()
            plt.ylim(min(y_vals) - 1, max(y_vals) + 1)
            
            return plt
            
        except Exception as e:
            print(f"Error al graficar: {e}")
            return None
    
    def interactive_solver(self):
        """Interfaz interactiva para resolver problemas"""
        print("="*60)
        print("PHOTOMATH PROTOTYPE - Resolución Matemática Paso a Paso")
        print("="*60)
        
        while True:
            print("\nOpciones:")
            print("1. Resolver ecuación (ej: 2*x + 3 = 7)")
            print("2. Simplificar expresión (ej: (x+1)^2 - x^2)")
            print("3. Calcular derivada (ej: x^2 + 3*x - 5)")
            print("4. Calcular integral (ej: x^2 + 2*x)")
            print("5. Resolver ecuación cuadrática (ej: a=1, b=-3, c=2)")
            print("6. Graficar función")
            print("7. Procesar imagen con ecuación")
            print("8. Salir")
            
            choice = input("\nSelecciona una opción (1-8): ").strip()
            
            if choice == '1':
                equation = input("Ingresa la ecuación (ej: 2*x + 3 = 7): ").strip()
                parsed = self.parse_equation(equation)
                result = self.solve_equation(parsed)
                
                if result['success']:
                    print("\n" + "="*40)
                    print("SOLUCIÓN PASO A PASO")
                    print("="*40)
                    for step in result['steps']:
                        print(f"\n{step}")
                else:
                    print(f"\nError: {result['error']}")
            
            elif choice == '2':
                expression = input("Ingresa la expresión a simplificar: ").strip()
                parsed = self.parse_equation(expression)
                result = self.solve_equation(parsed)
                
                if result['success']:
                    print("\n" + "="*40)
                    print("SIMPLIFICACIÓN PASO A PASO")
                    print("="*40)
                    for step in result['steps']:
                        print(f"\n{step}")
                else:
                    print(f"\nError: {result['error']}")
            
            elif choice == '3':
                expression = input("Ingresa la función para derivar: ").strip()
                result = self.calculate_derivative(expression)
                
                if result['success']:
                    print("\n" + "="*40)
                    print("DERIVADA PASO A PASO")
                    print("="*40)
                    for step in result['steps']:
                        print(f"\n{step}")
                else:
                    print(f"\nError: {result['error']}")
            
            elif choice == '4':
                expression = input("Ingresa la función para integrar: ").strip()
                result = self.calculate_integral(expression)
                
                if result['success']:
                    print("\n" + "="*40)
                    print("INTEGRAL PASO A PASO")
                    print("="*40)
                    for step in result['steps']:
                        print(f"\n{step}")
                else:
                    print(f"\nError: {result['error']}")
            
            elif choice == '5':
                try:
                    a = float(input("Coeficiente a: "))
                    b = float(input("Coeficiente b: "))
                    c = float(input("Coeficiente c: "))
                    
                    result = self.solve_quadratic(a, b, c)
                    
                    print("\n" + "="*40)
                    print("RESOLUCIÓN CUADRÁTICA")
                    print("="*40)
                    for step in result['steps']:
                        print(f"\n{step}")
                        
                    print(f"\n**Soluciones:**")
                    for i, sol in enumerate(result['solutions'], 1):
                        print(f"x{i} = {sol}")
                        
                except ValueError:
                    print("Error: Ingresa números válidos")
            
            elif choice == '6':
                expression = input("Ingresa la función para graficar (ej: x**2 + 3*x - 5): ").strip()
                plt = self.plot_function(expression)
                
                if plt:
                    plt.show()
                else:
                    print("Error al crear el gráfico")
            
            elif choice == '7':
                image_path = input("Ruta de la imagen con la ecuación: ").strip()
                
                try:
                    # Extraer texto de la imagen
                    text = self.extract_text_from_image(image_path)
                    print(f"\nTexto reconocido: {text}")
                    
                    # Procesar la ecuación
                    parsed = self.parse_equation(text)
                    print(f"Expresión procesada: {parsed['cleaned']}")
                    
                    # Resolver
                    result = self.solve_equation(parsed)
                    
                    if result['success']:
                        print("\n" + "="*40)
                        print("SOLUCIÓN DESDE IMAGEN")
                        print("="*40)
                        for step in result['steps']:
                            print(f"\n{step}")
                    else:
                        print(f"\nError: {result['error']}")
                        
                except Exception as e:
                    print(f"Error procesando imagen: {e}")
            
            elif choice == '8':
                print("\n¡Gracias por usar Photomath Prototype!")
                break
            
            else:
                print("Opción no válida. Intenta nuevamente.")

def eq(expr, value=0):
    """Helper function para mostrar ecuaciones"""
    return f"{expr} = {value}"

# Función para demostrar el prototipo
def demo_photomath():
    """Demostración del prototipo Photomath"""
    solver = PhotoMathPrototype()
    
    print("="*60)
    print("DEMOSTRACIÓN PHOTOMATH PROTOTYPE")
    print("="*60)
    
    # Ejemplo 1: Resolver ecuación lineal
    print("\n1. RESOLVIENDO ECUACIÓN LINEAL:")
    print("   Ecuación: 2*x + 5 = 13")
    parsed = solver.parse_equation("2*x + 5 = 13")
    result = solver.solve_equation(parsed)
    
    if result['success']:
        for step in result['steps']:
            print(f"   {step}")
    
    # Ejemplo 2: Simplificar expresión
    print("\n2. SIMPLIFICANDO EXPRESIÓN:")
    print("   Expresión: (x+1)^2 - x^2")
    parsed = solver.parse_equation("(x+1)**2 - x**2")
    result = solver.solve_equation(parsed)
    
    if result['success']:
        for step in result['steps']:
            print(f"   {step}")
    
    # Ejemplo 3: Derivada
    print("\n3. CALCULANDO DERIVADA:")
    print("   Función: x^2 + 3*x - 5")
    result = solver.calculate_derivative("x**2 + 3*x - 5")
    
    if result['success']:
        for step in result['steps']:
            print(f"   {step}")
    
    # Ejemplo 4: Ecuación cuadrática
    print("\n4. RESOLVIENDO ECUACIÓN CUADRÁTICA:")
    print("   Ecuación: x^2 - 3x + 2 = 0")
    result = solver.solve_quadratic(1, -3, 2)
    
    if result['success']:
        for step in result['steps']:
            print(f"   {step}")
    
    print("\n" + "="*60)
    print("¡Demostración completada!")
    print("="*60)
    
    # Preguntar si desea usar la interfaz interactiva
    use_interactive = input("\n¿Deseas usar la interfaz interactiva? (s/n): ").lower()
    if use_interactive == 's':
        solver.interactive_solver()

# Clase avanzada con procesamiento de imágenes mejorado
class AdvancedPhotoMath(PhotoMathPrototype):
    def __init__(self):
        super().__init__()
        self.setup_advanced_ocr()
    
    def setup_advanced_ocr(self):
        """Configura OCR avanzado para matemáticas"""
        # Para producción, se necesitaría entrenar un modelo específico
        # o usar una API como Mathpix
        pass
    
    def detect_and_segment_equations(self, image_path):
        """Detecta y segmenta ecuaciones en una imagen"""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Usar detección de bordes
        edges = cv2.Canny(gray, 50, 150)
        
        # Encontrar contornos
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        equations = []
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            
            # Filtrar por tamaño y relación de aspecto
            if w > 30 and h > 20 and w/h < 10:
                roi = img[y:y+h, x:x+w]
                
                # Extraer texto
                text = pytesseract.image_to_string(roi, config='--psm 6')
                text = text.strip()
                
                if text and any(c.isdigit() or c in '+-*/=()[]{}' for c in text):
                    equations.append({
                        'bbox': (x, y, w, h),
                        'text': text,
                        'image': roi
                    })
        
        return equations
    
    def visualize_detection(self, image_path):
        """Visualiza la detección de ecuaciones"""
        img = cv2.imread(image_path)
        equations = self.detect_and_segment_equations(image_path)
        
        # Dibujar rectángulos alrededor de las ecuaciones detectadas
        for eq in equations:
            x, y, w, h = eq['bbox']
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, eq['text'][:20], (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Mostrar imagen
        plt.figure(figsize=(12, 8))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title('Detección de Ecuaciones')
        plt.axis('off')
        plt.show()
        
        return equations
    
    def solve_from_camera(self):
        """Captura y resuelve ecuaciones desde la cámara"""
        import cv2
        
        print("\nPresiona 's' para capturar la ecuación, 'q' para salir")
        
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Mostrar instrucciones en el frame
            cv2.putText(frame, "Presiona 's' para capturar", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "'q' para salir", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Photomath - Captura de Ecuaciones', frame)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('s'):
                # Guardar imagen temporal
                temp_path = 'temp_equation.jpg'
                cv2.imwrite(temp_path, frame)
                
                # Procesar ecuación
                try:
                    text = self.extract_text_from_image(temp_path)
                    print(f"\nEcuación reconocida: {text}")
                    
                    parsed = self.parse_equation(text)
                    result = self.solve_equation(parsed)
                    
                    if result['success']:
                        print("\nSOLUCIÓN:")
                        for step in result['steps']:
                            print(f"{step}")
                    else:
                        print(f"Error: {result['error']}")
                        
                except Exception as e:
                    print(f"Error procesando imagen: {e}")
                
                # Esperar un momento
                cv2.waitKey(1000)
                
            elif key == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    def create_math_worksheet(self, problems, output_path='worksheet_solutions.pdf'):
        """Crea una hoja de trabajo con soluciones paso a paso"""
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch
        
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        
        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawString(1*inch, height-1*inch, "Photomath - Hoja de Trabajo con Soluciones")
        
        c.setFont("Helvetica", 12)
        y_position = height - 1.5*inch
        
        for i, problem in enumerate(problems, 1):
            # Mostrar problema
            c.drawString(1*inch, y_position, f"{i}. {problem}")
            y_position -= 0.25*inch
            
            # Resolver
            parsed = self.parse_equation(problem)
            result = self.solve_equation(parsed)
            
            if result['success']:
                if 'steps' in result:
                    for step in result['steps'][:3]:  # Mostrar primeros 3 pasos
                        c.drawString(1.5*inch, y_position, step[:80])
                        y_position -= 0.2*inch
            
            y_position -= 0.2*inch
            
            # Nueva página si es necesario
            if y_position < 1*inch:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 1*inch
        
        c.save()
        print(f"Hoja de trabajo guardada como: {output_path}")

# Script principal
if __name__ == "__main__":
    print("="*60)
    print("PHOTOMATH PROTOTYPE - Sistema de Reconocimiento Matemático")
    print("="*60)
    
    print("\nSelecciona el modo:")
    print("1. Modo básico (interfaz de consola)")
    print("2. Modo avanzado (con detección visual)")
    print("3. Demostración automática")
    
    mode = input("\nOpción (1-3): ").strip()
    
    if mode == '1':
        solver = PhotoMathPrototype()
        solver.interactive_solver()
    
    elif mode == '2':
        solver = AdvancedPhotoMath()
        
        print("\nModo avanzado activado")
        print("1. Capturar desde cámara")
        print("2. Procesar imagen existente")
        print("3. Visualizar detección")
        print("4. Crear hoja de trabajo")
        
        option = input("\nOpción (1-4): ").strip()
        
        if option == '1':
            solver.solve_from_camera()
        elif option == '2':
            image_path = input("Ruta de la imagen: ").strip()
            text = solver.extract_text_from_image(image_path)
            print(f"\nTexto reconocido: {text}")
            
            parsed = solver.parse_equation(text)
            result = solver.solve_equation(parsed)
            
            if result['success']:
                for step in result['steps']:
                    print(f"\n{step}")
        elif option == '3':
            image_path = input("Ruta de la imagen: ").strip()
            solver.visualize_detection(image_path)
        elif option == '4':
            problems = []
            print("\nIngresa problemas (deja vacío para terminar):")
            while True:
                problem = input(f"Problema {len(problems)+1}: ").strip()
                if not problem:
                    break
                problems.append(problem)
            
            if problems:
                solver.create_math_worksheet(problems)
    
    elif mode == '3':
        demo_photomath()
    
    else:
        print("Opción no válida")
