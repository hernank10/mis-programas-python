import tkinter as tk
from sympy import symbols, solve
from sympy.plotting import plot

def resolver_ecuacion():
    x = symbols('x')
    ecuacion = entrada_ecuacion.get()
    solucion = solve(ecuacion, x)
    resultado.set(solucion)

def graficar_ecuacion():
    x = symbols('x')
    ecuacion = entrada_ecuacion.get()
    plot(ecuacion)

root = tk.Tk()
root.title('Simulación con Tkinter y SymPy')

entrada_ecuacion = tk.Entry(root, width=50)
entrada_ecuacion.pack(pady=10)

boton_resolver = tk.Button(root, text='Resolver', command=resolver_ecuacion)
boton_resolver.pack()

boton_graficar = tk.Button(root, text='Graficar', command=graficar_ecuacion)
boton_graficar.pack()

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(root, textvariable=resultado)
etiqueta_resultado.pack()

root.mainloop()
