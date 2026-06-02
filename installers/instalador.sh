#!/bin/bash
# Instalador automático para mis-programas-python (Unix/Mac/Linux/Termux)

echo "═══════════════════════════════════════════════════════════════════"
echo "   🐍 MIS PROGRAMAS PYTHON - INSTALADOR AUTOMÁTICO 🐍"
echo "═══════════════════════════════════════════════════════════════════"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Directorio de instalación
INSTALL_DIR="$HOME/mis_programas_python"
mkdir -p "$INSTALL_DIR"
echo -e "${GREEN}✅ Instalando en: $INSTALL_DIR${NC}"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 no encontrado. Instálalo primero.${NC}"
    exit 1
fi

# Instalar dependencias
echo -e "${BLUE}📦 Instalando dependencias...${NC}"
pip3 install colorama nltk --quiet

# Clonar repositorios
echo -e "${BLUE}📥 Clonando repositorios...${NC}"
cd "$INSTALL_DIR"

if [ -d "mis-programas-python" ]; then
    cd mis-programas-python && git pull && cd ..
else
    git clone https://github.com/Hernank10/mis-programas-python.git
fi

if [ -d "mini-htmls-educativos" ]; then
    cd mini-htmls-educativos && git pull && cd ..
else
    git clone https://github.com/Hernank10/mini-htmls-educativos.git
fi

# Crear lanzador
echo -e "${BLUE}🚀 Creando lanzador...${NC}"
cat > "$INSTALL_DIR/ejecutar.sh" << 'LAUNCHER'
#!/bin/bash
cd "$HOME/mis_programas_python/mis-programas-python"
python3 menu_principal.py
LAUNCHER

chmod +x "$INSTALL_DIR/ejecutar.sh"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 ¡INSTALACIÓN COMPLETADA! 🎉${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "📁 Ubicación: ${YELLOW}$INSTALL_DIR${NC}"
echo ""
echo -e "🚀 Para ejecutar:"
echo -e "   ${YELLOW}cd $INSTALL_DIR && ./ejecutar.sh${NC}"
echo ""
echo -e "🎮 Para jugar juegos de texto:"
echo -e "   ${YELLOW}cd \"$INSTALL_DIR/mis-programas-python/JUEGOS_DE_TEXTO_ PLANETAS _BIBLIOTECA_colorama\"${NC}"
echo -e "   ${YELLOW}python3 tomson_ciudad_salvaje.py${NC}"
echo ""
echo -e "📖 Para ver lecciones HTML:"
echo -e "   ${YELLOW}cd $INSTALL_DIR/mini-htmls-educativos && python3 -m http.server 8000${NC}"
echo -e "   Luego abre ${YELLOW}http://localhost:8000${NC} en tu navegador"
echo ""
