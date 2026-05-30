# -*- coding: utf-8 -*-
import json
import random
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
from datetime import datetime

class SpanishConstructorGUI:
    def __init__(self, root):
        # ... (código anterior sin cambios) ...
        
        # Agregar nuevo botón en el panel izquierdo
        ttk.Button(
            self.left_panel, 
            text="Generar 100 ejemplos", 
            command=self.generate_100_examples
        ).pack(pady=10, fill=tk.X)
        
        # ... (resto del código anterior sin cambios) ...

    def generate_100_examples(self):
        examples = []
        constructions = [
            (1, "Artículo indefinido + sustantivo + posesivo"),
            (2, "Determinante + sustantivo + posesivo"),
            (3, "Artículo definido enfático")
        ]
        
        # Generar 34 ejemplos por construcción (102 total)
        for const_id, const_name in constructions:
            for _ in range(34):
                example = self.generate_example(const_id, const_name)
                examples.append({
                    "español": example['frase'],
                    "inglés": example['traduccion'],
                    "construcción": const_name
                })
        
        # Guardar archivo
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=f"ejemplos_español_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(examples, f, ensure_ascii=False, indent=2)
                messagebox.showinfo("Éxito", f"100 ejemplos guardados en:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar: {str(e)}")

    def generate_example(self, const_id, const_name):
        sustantivo = random.choice(self.sustantivos)
        posesivos = ['mío', 'tuyo', 'suyo', 'nuestro', 'vuestro', 'suyo']
        posesivo = random.choice(posesivos)
        numero = random.choice(['singular', 'plural'])
        genero = sustantivo['genero']
        
        # Configurar artículo según construcción
        if const_id == 1:
            articulos = ['un', 'una', 'unos', 'unas']
        elif const_id == 2:
            articulos = ['algún', 'ningún', 'alguna', 'ninguna']
        else:  # const_id == 3
            articulos = ['el', 'la', 'los', 'las']
        
        # Seleccionar artículo
        if numero == 'plural':
            art_options = [a for a in articulos if a.endswith('s') or a.endswith('s')]
        else:
            art_options = [a for a in articulos if not a.endswith('s')]
        
        articulo = random.choice(art_options)
        
        # Formar sustantivo
        sust = sustantivo['plural'] if numero == 'plural' else sustantivo['palabra']
        
        # Ajustar posesivo
        pos = self.ajustar_posesivo(posesivo, genero, numero)
        
        # Crear frase
        frase_es = f"{articulo.capitalize()} {sust} {pos}"
        
        # Generar traducción
        traduccion_en = self.generar_traduccion(articulo, sust, pos, const_id)
        
        return {
            'frase': frase_es,
            'traduccion': traduccion_en
        }

    def ajustar_posesivo(self, posesivo, genero, numero):
        # Lógica de concordancia
        base = posesivo[:-1] if posesivo.endswith('o') else posesivo
        sufijo_genero = 'a' if genero == 'f' else 'o'
        
        if numero == 'singular':
            return f"{base}{sufijo_genero}"
        else:
            return f"{base}{sufijo_genero}s"

    def generar_traduccion(self, articulo, sust, pos, const_id):
        # Mapear posesivos a inglés
        posesivos_en = {
            'mío': 'my',
            'tuyo': 'your',
            'suyo': 'his/her/their',
            'nuestro': 'our',
            'vuestro': 'your (pl)',
            'suyo': 'their'
        }
        
        base_pos = pos.rstrip('oas')
        traduccion_pos = posesivos_en.get(base_pos, 'of mine')
        
        if const_id == 3:
            return f"The {sust} {traduccion_pos}"
        
        if const_id == 2:
            determinante = 'some' if 'alg' in articulo else 'no'
            return f"{determinante.capitalize()} {traduccion_pos} {sust}"
        
        # Para construcción 1
        return f"A {traduccion_pos} {sust}" if articulo in ['un', 'una'] else f"Some {traduccion_pos} {sust}"

# ... (el resto de la clase SpanishConstructorGUI sin cambios) ...

if __name__ == "__main__":
    root = tk.Tk()
    app = SpanishConstructorGUI(root)
    root.mainloop()
