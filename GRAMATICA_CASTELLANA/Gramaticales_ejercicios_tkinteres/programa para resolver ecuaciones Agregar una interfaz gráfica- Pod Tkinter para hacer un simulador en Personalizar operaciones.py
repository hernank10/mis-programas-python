import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, solve
import math


class AbacoAvanzado:
    def __init__(self):
        self.resultado = None

    def realizar_operacion(self, num1, operador, num2=None):
        """Realiza operaciones avanzadas."""
        if operador == "^":
            self.resultado = num1 ** (num2 if num2 else 2)
        elif operador == "√":
            self.resultado = math.sqrt(num1)
        elif operador == "%":
            if num2 is not None:
                self.resultado = num1 % num2
            else:
                raise ValueError("El operador '%' necesita dos operandos.")
        else:
            raise ValueError("Operador no soportado.")
        return self.resultado

    def resolver_ecuacion(self, coeficientes, tipo="lineal"):
        """Resuelve ecuaciones lineales y cuadráticas."""
        x = symbols('x')
        if tipo == "lineal":
            ecuacion = Eq(coeficientes[0] * x + coeficientes[1], coeficientes[2])
        elif tipo == "cuadratica":
            ecuacion = Eq(coeficientes[0] * x**2 + coeficientes[1] * x + coeficientes[2], 0)
        else:
            raise ValueError("Tipo de ecuación no soportado.")
        solucion = solve(ecuacion, x)
        return solucion


# Interfaz gráfica con Tkinter
class AbacoGUI:
    def __init__(self, root):
        self.abaco = AbacoAvanzado()
        self.root = root
        self.root.title("Simulador de Ábaco")
        self.create_widgets()

    def create_widgets(self):
        """Crea los elementos gráficos."""
        tk.Label(self.root, text="Número 1:").grid(row=0, column=0)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Operador:").grid(row=1, column=0)
        self.operador_entry = tk.Entry(self.root)
        self.operador_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Número 2:").grid(row=2, column=0)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=2, column=1)

        self.result_label = tk.Label(self.root, text="Resultado: ")
        self.result_label.grid(row=3, column=0, columnspan=2)

        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=4, column=0)
        tk.Button(self.root, text="Salir", command=self.root.quit).grid(row=4, column=1)

        tk.Label(self.root, text="Resolver ecuación cuadrática (ax² + bx + c):").grid(row=5, column=0, columnspan=2)
        tk.Label(self.root, text="a:").grid(row=6, column=0)
        self.a_entry = tk.Entry(self.root)
        self.a_entry.grid(row=6, column=1)

        tk.Label(self.root, text="b:").grid(row=7, column=0)
        self.b_entry = tk.Entry(self.root)
        self.b_entry.grid(row=7, column=1)

        tk.Label(self.root, text="c:").grid(row=8, column=0)
        self.c_entry = tk.Entry(self.root)
        self.c_entry.grid(row=8, column=1)

        tk.Button(self.root, text="Resolver Ecuación", command=self.resolver_ecuacion).grid(row=9, column=0, columnspan=2)

    def calcular(self):
        """Realiza operaciones avanzadas."""
        try:
            num1 = float(self.num1_entry.get())
            operador = self.operador_entry.get()
            num2 = float(self.num2_entry.get()) if self.num2_entry.get() else None
            resultado = self.abaco.realizar_operacion(num1, operador, num2)
            self.result_label.config(text=f"Resultado: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def resolver_ecuacion(self):
        """Resuelve ecuaciones cuadráticas."""
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            soluciones = self.abaco.resolver_ecuacion([a, b, c], tipo="cuadratica")
            messagebox.showinfo("Soluciones", f"Soluciones: {soluciones}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Ejecutar programa
if __name__ == "__main__":
    root = tk.Tk()
    app = AbacoGUI(root)
    root.mainloop()
