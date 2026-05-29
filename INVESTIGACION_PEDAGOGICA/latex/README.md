# Proyecto de Investigación Pedagógica

## Desarrollo de Competencias Lingüísticas en Español Mediante Herramientas Interactivas en Python

### Contenido de esta carpeta

- `proyecto_investigacion.tex` - Documento principal en LaTeX
- `proyecto_investigacion.pdf` - Versión compilada en PDF (generar con pdflatex)

### Cómo compilar el documento

```bash
# Compilar a PDF
pdflatex proyecto_investigacion.tex
pdflatex proyecto_investigacion.tex  # segunda vez para referencias

# O con latexmk (recomendado)
latexmk -pdf proyecto_investigacion.tex

Estructura del documento
Planteamiento del problema

Marco teórico

Objetivos

Metodología

Cronograma

Análisis de datos

Consideraciones éticas

Resultados esperados

Limitaciones

Bibliografía

Anexos

Requisitos de LaTeX
bash
# Instalar en Ubuntu/Debian
sudo apt-get install texlive-full

# Instalar en macOS
brew install --cask mactex

# O usar Overleaf (online)
Enlace al repositorio principal
https://github.com/Hernank10/mis-programas-python

## Artículo pedagógico

El archivo `articulo_pedagogico.tex` contiene un artículo completo sobre el uso educativo de todos los programas del repositorio, con:

- Descripción de cada módulo (Latín, Gramática, Juegos, Fonética, Inglés)
- Fundamentos pedagógicos (constructivismo, gamificación)
- Ejemplos de uso en el aula
- Guía rápida de inicio
- Referencias bibliográficas

### Compilar el artículo

```bash
pdflatex articulo_pedagogico.tex
pdflatex articulo_pedagogico.tex  # segunda pasada
