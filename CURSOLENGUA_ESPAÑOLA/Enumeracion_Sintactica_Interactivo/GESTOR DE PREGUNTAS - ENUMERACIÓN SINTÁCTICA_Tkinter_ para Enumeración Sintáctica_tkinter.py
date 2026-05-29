import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import json
import os
import subprocess
from datetime import datetime

class GestorPreguntasGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Preguntas Profesional")
        self.geometry("1000x800")
        self.archivo_preguntas = "preguntas.json"
        self.categorias = ["Enumeración simple", "Sujeto-Verbo", "Nombres propios", "Casos complejos"]
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        # Marco principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Panel de control
        control_frame = ttk.LabelFrame(main_frame, text="Acciones")
        control_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        
        botones = [
            ("Generar Plantilla", self.generar_plantilla),
            ("Validar Estructura", self.validar_estructura),
            ("Crear Backup", self.crear_backup),
            ("Integrar en App", self.integrar_aplicacion),
            ("Iniciar Git", self.inicializar_git)
        ]
        
        for texto, comando in botones:
            btn = ttk.Button(control_frame, text=texto, command=comando)
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            
        # Consola de salida
        self.consola = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, state='disabled')
        self.consola.pack(fill=tk.BOTH, expand=True)
        
        # Barra de estado
        self.status = ttk.Label(main_frame, text="Listo", relief=tk.SUNKEN)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        
    def log(self, mensaje):
        self.consola.configure(state='normal')
        self.consola.insert(tk.END, f"> {mensaje}\n")
        self.consola.configure(state='disabled')
        self.consola.see(tk.END)
        self.actualizar_status(mensaje)
        
    def actualizar_status(self, texto):
        self.status.config(text=texto)
        self.update_idletasks()
    
    def generar_plantilla(self):
        try:
            if os.path.exists(self.archivo_preguntas):
                self.crear_backup()
                
            preguntas = []
            for i in range(1, 101):
                preguntas.append({
                    "id": i,
                    "pregunta": f"Pregunta {i} (Editar texto)",
                    "categoria": self.categorias[i % len(self.categorias)],
                    "opciones": ["A) Opción A", "B) Opción B"],
                    "correcta": "A",
                    "dificultad": min((i // 25) + 1, 4)
                })
            
            with open(self.archivo_preguntas, 'w') as f:
                json.dump(preguntas, f, indent=4, ensure_ascii=False)
                
            self.log("Plantilla de 100 preguntas generada con éxito")
            messagebox.showinfo("Éxito", "Plantilla generada correctamente")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def validar_estructura(self):
        try:
            with open(self.archivo_preguntas, 'r') as f:
                data = json.load(f)
                
                if len(data) != 100:
                    raise ValueError(f"Se encontraron {len(data)} preguntas (deben ser 100)")
                
                errores = []
                for idx, p in enumerate(data):
                    if not all(key in p for key in ['id', 'pregunta', 'opciones', 'correcta']):
                        errores.append(f"Pregunta {idx+1}: Estructura incompleta")
                    if p['correcta'] not in ['A', 'B']:
                        errores.append(f"Pregunta {idx+1}: Respuesta debe ser A/B")
                
                if errores:
                    error_msg = "\n".join(errores[:5]) + ("\n..." if len(errores)>5 else "")
                    self.log(f"Errores encontrados:\n{error_msg}")
                    messagebox.showerror("Validación Fallida", f"{len(errores)} errores detectados")
                else:
                    self.log("✓ Validación exitosa")
                    messagebox.showinfo("Validación Exitosa", "Estructura correcta")
                    
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def crear_backup(self):
        try:
            os.makedirs("backups", exist_ok=True)
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"backups/preguntas_{fecha}.json"
            
            with open(self.archivo_preguntas, 'r') as orig, open(backup_file, 'w') as bkp:
                json.dump(json.load(orig), bkp, indent=4)
            
            self.log(f"Backup creado: {backup_file}")
            messagebox.showinfo("Backup Exitoso", f"Archivo guardado en:\n{backup_file}")
            
        except Exception as e:
            messagebox.showerror("Error en Backup", str(e))
    
    def integrar_aplicacion(self):
        try:
            ruta = filedialog.askdirectory(title="Seleccionar directorio de la aplicación")
            if ruta:
                destino = os.path.join(ruta, self.archivo_preguntas)
                os.replace(self.archivo_preguntas, destino)
                self.log(f"Archivo integrado en: {destino}")
                messagebox.showinfo("Integración Exitosa", "Archivo de preguntas movido")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def inicializar_git(self):
        try:
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", self.archivo_preguntas], check=True)
            subprocess.run(["git", "commit", "-m", "Banco inicial de 100 preguntas"], check=True)
            self.log("✓ Repositorio Git inicializado")
            messagebox.showinfo("Git Configurado", "Control de versiones activado")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error Git", str(e))
    
if __name__ == "__main__":
    app = GestorPreguntasGUI()
    app.mainloop()
