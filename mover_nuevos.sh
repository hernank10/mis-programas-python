#!/bin/bash
echo "=== MOVIENDO ARCHIVOS NUEVOS A SU LUGAR ==="

# Ver archivos no rastreados
echo ""
echo "Archivos no rastreados:"
git status --porcelain | grep "^??" | sed 's/^?? //'

echo ""
read -p "¿Quieres moverlos automáticamente? (s/n): " respuesta

if [ "$respuesta" = "s" ]; then
    # Aquí puedes definir reglas de movimiento
    git add .
    echo "✅ Archivos añadidos a git"
else
    echo "❌ No se movieron archivos"
fi
