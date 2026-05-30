import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from gtts import gTTS
import os
from datetime import datetime

class OrtografiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutor de Ortografía Española")
        self.root.geometry("800x600")
        
        # Cargar datos
        self.ejemplos = self.cargar_json('ejemplos.json')
        self.progreso = self.cargar_json('progreso.json')
        
        # Configurar interfaz
        self.crear_menu_principal()
        self.crear_widgets()
        
        # Variables de estado
        self.ejemplo_actual = None
        self.categoria_actual = None

    def cargar_json(self, archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_json(self, datos, archivo):
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=2)

    def crear_menu_principal(self):
        menubar = tk.Menu(self.root)
        
        # Menú de práctica
        menu_practica = tk.Menu(menubar, tearoff=0)
        for categoria in ['B/V', 'G/J', 'C/Z/S', 'LL/Y', 'QU/C/K', 'ACENTOS']:
            menu_practica.add_command(
                label=categoria,
                command=lambda c=categoria: self.iniciar_practica(c)
            )
        menubar.add_cascade(label="Practicar", menu=menu_practica)
        
        # Menú de administración
        menu_admin = tk.Menu(menubar, tearoff=0)
        menu_admin.add_command(label="Agregar ejemplo", command=self.mostrar_editor)
        menu_admin.add_command(label="Ver todos", command=self.mostrar_ejemplos)
        menu_admin.add_command(label="Estadísticas", command=self.mostrar_estadisticas)
        menubar.add_cascade(label="Administrar", menu=menu_admin)
        
        self.root.config(menu=menubar)

    def crear_widgets(self):
        # Panel principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Widgets de práctica
        self.lbl_categoria = ttk.Label(self.main_frame, font=('Arial', 14))
        self.lbl_categoria.pack(pady=10)
        
        self.lbl_afi = ttk.Label(self.main_frame, font=('Arial', 12))
        self.lbl_afi.pack(pady=5)
        
        self.btn_audio = ttk.Button(
            self.main_frame,
            text="Escuchar pronunciación",
            command=self.reproducir_audio
        )
        self.btn_audio.pack(pady=5)
        
        self.entrada = ttk.Entry(self.main_frame, font=('Arial', 14))
        self.entrada.pack(pady=10)
        
        self.btn_verificar = ttk.Button(
            self.main_frame,
            text="Verificar",
            command=self.verificar_respuesta
        )
        self.btn_verificar.pack(pady=5)
        
        self.lbl_explicacion = ttk.Label(
            self.main_frame,
            wraplength=600,
            font=('Arial', 12)
        )
        self.lbl_explicacion.pack(pady=10)
        
        self.lbl_progreso = ttk.Label(self.main_frame, font=('Arial', 12))
        self.lbl_progreso.pack(pady=10)

    def iniciar_practica(self, categoria):
        self.categoria_actual = categoria
        self.ejemplos_categoria = [
            e for e in self.ejemplos if e['categoria'] == categoria
        ]
        random.shuffle(self.ejemplos_categoria)
        self.indice_actual = 0
        self.aciertos = 0
        
        self.mostrar_siguiente_ejemplo()
        self.actualizar_progreso_ui()

    def mostrar_siguiente_ejemplo(self):
        if self.indice_actual < len(self.ejemplos_categoria):
            self.ejemplo_actual = self.ejemplos_categoria[self.indice_actual]
            self.lbl_categoria.config(text=f"Categoría: {self.categoria_actual}")
            self.lbl_afi.config(text=f"AFI: {self.ejemplo_actual['AFI']}")
            self.entrada.delete(0, tk.END)
            self.lbl_explicacion.config(text="")
        else:
            messagebox.showinfo(
                "Práctica completada",
                f"Resultado: {self.aciertos}/{len(self.ejemplos_categoria)} correctos"
            )
            self.guardar_progreso()
            self.main_frame.pack()

    def verificar_respuesta(self):
        respuesta = self.entrada.get().strip().lower()
        correcta = self.ejemplo_actual['palabra'].lower()
        
        if respuesta == correcta:
            self.aciertos += 1
            mensaje = "✅ Correcto!\n"
        else:
            mensaje = f"❌ Incorrecto. La respuesta correcta es: {correcta}\n"
        
        mensaje += f"Regla: {self.ejemplo_actual['regla']}"
        self.lbl_explicacion.config(text=mensaje)
        self.indice_actual += 1
        self.actualizar_progreso_ui()
        self.root.after(2000, self.mostrar_siguiente_ejemplo)

    def actualizar_progreso_ui(self):
        total = len(self.ejemplos_categoria)
        self.lbl_progreso.config(
            text=f"Progreso: {self.indice_actual}/{total} | Aciertos: {self.aciertos}"
        )

    def reproducir_audio(self):
        tts = gTTS(text=self.ejemplo_actual['palabra'], lang='es')
        tts.save('temp.mp3')
        os.system('start temp.mp3' if os.name == 'nt' else 'afplay temp.mp3')

    def mostrar_editor(self, ejemplo=None):
        editor = tk.Toplevel(self.root)
        editor.title("Editor de Ejemplos")
        
        campos = [
            ('Palabra', 'palabra'),
            ('AFI', 'AFI'),
            ('Categoría', 'categoria'),
            ('Regla', 'regla'),
            ('Significado', 'significado')
        ]
        
        entries = {}
        for i, (label, key) in enumerate(campos):
            ttk.Label(editor, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(editor, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5)
            if ejemplo:
                entry.insert(0, ejemplo[key])
            entries[key] = entry
        
        def guardar():
            nuevo_ejemplo = {key: entry.get() for key, entry in entries.items()}
            if ejemplo:
                self.ejemplos[self.ejemplos.index(ejemplo)] = nuevo_ejemplo
            else:
                self.ejemplos.append(nuevo_ejemplo)
            self.guardar_json(self.ejemplos, 'ejemplos.json')
            editor.destroy()
            messagebox.showinfo("Éxito", "Ejemplo guardado correctamente")
        
        ttk.Button(editor, text="Guardar", command=guardar).grid(
            row=len(campos), columnspan=2, pady=10)

    def mostrar_ejemplos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Todos los Ejemplos")
        
        tree = ttk.Treeview(ventana, columns=('Categoría', 'AFI', 'Regla'), show='headings')
        tree.heading('#0', text='Palabra')
        tree.heading('Categoría', text='Categoría')
        tree.heading('AFI', text='AFI')
        tree.heading('Regla', text='Regla')
        
        for ejemplo in self.ejemplos:
            tree.insert('', 'end', 
                text=ejemplo['palabra'],
                values=(ejemplo['categoria'], ejemplo['AFI'], ejemplo['regla'])
            )
        
        tree.pack(fill=tk.BOTH, expand=True)

    def mostrar_estadisticas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Estadísticas de Progreso")
        
        stats_text = tk.Text(ventana, wrap=tk.WORD)
        stats_text.pack(fill=tk.BOTH, expand=True)
        
        # Generar estadísticas
        total_ejemplos = len(self.ejemplos)
        stats_text.insert(tk.END, f"Ejemplos en base: {total_ejemplos}\n\n")
        
        for categoria in ['B/V', 'G/J', 'C/Z/S', 'LL/Y', 'QU/C/K', 'ACENTOS']:
            stats_text.insert(tk.END, f"=== {categoria} ===\n")
            ejemplos_cat = [e for e in self.progreso if e['categoria'] == categoria]
            intentos = sum(e['intentos'] for e in ejemplos_cat)
            aciertos = sum(e['aciertos'] for e in ejemplos_cat)
            
            if intentos > 0:
                porcentaje = (aciertos / intentos) * 100
                stats_text.insert(tk.END, 
                    f"Aciertos: {aciertos}/{intentos} ({porcentaje:.1f}%)\n\n")
            else:
                stats_text.insert(tk.END, "Aún no practicado\n\n")

    def guardar_progreso(self):
        registro = {
            'fecha': str(datetime.now()),
            'categoria': self.categoria_actual,
            'intentos': len(self.ejemplos_categoria),
            'aciertos': self.aciertos
        }
        self.progreso.append(registro)
        self.guardar_json(self.progreso, 'progreso.json')

if __name__ == "__main__":
    root = tk.Tk()
    app = OrtografiaApp(root)
    root.mainloop()
