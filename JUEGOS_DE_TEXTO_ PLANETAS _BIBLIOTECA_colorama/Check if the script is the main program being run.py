import sys
import time
import random
from collections import defaultdict

# Install colorama if not already installed
try:
    import colorama
except ImportError:
    !pip install colorama
    import colorama

# Inicializar colorama para colores en la terminal (opcional)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

# ... (Rest of the code remains the same) ...

# Ejecutar el juego
# Check if the script is the main program being run
if __name__ == "__main__":
    # If so, create a new Juego instance and start the game
    juego = Juego() # This line is only executed when the script is run directly, not imported
    juego.iniciar_juego()
