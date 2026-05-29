import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

def caida_libre():
    t = simpledialog.askfloat("Caída libre", "Introduce el tiempo en segundos:")
    if t is not None:
        g = 9.8
        h = 0.5 * g * t ** 2
        messagebox.showinfo("Resultado", f"Distancia recorrida: {h:.2f} metros")

def conversion_unidades():
    ventana = tk.Toplevel()
    ventana.title("Conversión de Unidades")

    def convertir():
        valor = float(entrada.get())
        if variable.get() == "Km a m":
            resultado = valor * 1000
        elif variable.get() == "g a kg":
            resultado = valor / 1000
        elif variable.get() == "L a mL":
            resultado = valor * 1000
        else:
            resultado = 0
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")

    variable = tk.StringVar(value="Km a m")
    opciones = ["Km a m", "g a kg", "L a mL"]
    menu_opciones = tk.OptionMenu(ventana, variable, *opciones)
    menu_opciones.pack()

    entrada = tk.Entry(ventana)
    entrada.pack()

    boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
    boton_convertir.pack()

def registro_temperaturas():
    temperaturas = []
    for i in range(5):
        temp = simpledialog.askfloat("Temperatura", f"Introduce la temperatura {i+1}:")
        if temp is not None:
            temperaturas.append(temp)
    if temperaturas:
        promedio = sum(temperaturas) / len(temperaturas)
        messagebox.showinfo("Promedio", f"Temperatura promedio: {promedio:.2f} °C")

def graficar_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    temperaturas = [21.5, 23.0, 22.2, 24.1, 23.3]
    plt.plot(dias, temperaturas, marker='o')
    plt.title("Temperaturas semanales")
    plt.xlabel("Día")
    plt.ylabel("Temperatura °C")
    plt.grid()
    plt.show()

def tabla_periodica():
    elementos = {
        1: "Hidrógeno", 2: "Helio", 3: "Litio", 4: "Berilio",
        5: "Boro", 6: "Carbono", 7: "Nitrógeno", 8: "Oxígeno"
    }
    numero = simpledialog.askinteger("Tabla periódica", "Introduce número atómico (1-8):")
    if numero in elementos:
        messagebox.showinfo("Elemento", f"Elemento: {elementos[numero]}")
    else:
        messagebox.showwarning("Aviso", "Número no disponible.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ciencias con Python")
ventana.geometry("300x300")

# Botones del menú
tk.Button(ventana, text="Caída libre", command=caida_libre).pack(pady=5)
tk.Button(ventana, text="Conversión de unidades", command=conversion_unidades).pack(pady=5)
tk.Button(ventana, text="Registro de temperaturas", command=registro_temperaturas).pack(pady=5)
tk.Button(ventana, text="Gráfico de temperaturas", command=graficar_temperaturas).pack(pady=5)
tk.Button(ventana, text="Tabla periódica simple", command=tabla_periodica).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()
