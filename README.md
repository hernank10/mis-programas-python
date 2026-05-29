# mis-programas-python
mis-programas-python
cd /workspaces/mis-programas-python
cat > README.md << 'EOF'
# 📚 Mis Programas de Python - Aprendizaje de Latín y Gramática Castellana

## 📁 Estructura del Proyecto
mis-programas-python/
├── LATIN/ # Todo el contenido de latín
│ ├── ejercicios/ # Ejercicios de declinaciones y gramática latina
│ ├── tutores/ # Programas interactivos para practicar latín
│ └── datos/ # Archivos JSON con ejercicios y vocabulario
├── GRAMATICA_CASTELLANA/ # Contenido de gramática española
│ ├── ejercicios_python/ # Scripts de práctica gramatical
│ └── documentos/ # Documentación y archivos .docx
└── README.md # Este archivo



## 🏛️ LATÍN

### Ejercicios disponibles:
- **Primera declinación** (genitivo y ablativo)
- Casos y funciones del sintagma nominal
- Sintaxis del ablativo

### Tutores interactivos:
- Vocabulario básico
- Adjetivos de 2ª clase y comparativos
- Formas nominales del verbo (participio, gerundio, supino)
- Verbos irregulares (fero, eo)
- Pronombres personales, reflexivos y posesivos
- Voz pasiva y complemento agente

### Archivo principal:
- `latin_tutor.py` - Tutor principal de latín
- `ejercicios_latin.json` - Base de datos de ejercicios

## 📖 GRAMÁTICA CASTELLANA

### Temas cubiertos:
- Sintaxis de la lengua castellana (60 problemas de gramática)
- Uso correcto de la segunda persona
- Reglas de la primera persona del singular
- Conectores y consejos gramaticales
- Tiempos verbales (pluscuamperfecto)

### Tipos de programas:
- Scripts de consola interactivos
- Aplicaciones con interfaz gráfica (Tkinter)
- Ejercicios prácticos con retroalimentación

## 🚀 Cómo ejecutar los programas

### Ejecutar un tutor de latín:
```bash
cd LATIN/tutores
python3 "Tutor interactivo de latín en la consola. Este programa se enfoca en el vocabulario básico.py"
