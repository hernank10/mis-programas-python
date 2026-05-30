#!/bin/bash
# Menú principal para todos los programas

while true; do
    clear
    echo "====================================="
    echo "   MIS PROGRAMAS DE APRENDIZAJE"
    echo "====================================="
    echo ""
    echo "📖 SELECCIONA UN IDIOMA:"
    echo "1) 🏛️  LATÍN (6 programas)"
    echo "2) 🇬🇧  INGLÉS (31 programas)"
    echo "3) 📖  ESPAÑOL (150+ programas)"
    echo "4) 🎮  JUEGOS EDUCATIVOS"
    echo "5) 🚪  SALIR"
    echo ""
    read -p "Elige una opción (1-5): " opcion

    case $opcion in
        1)
            echo ""
            echo "=== PROGRAMAS DE LATÍN ==="
            echo "1) Entrenador de Declinaciones"
            echo "2) Primera Declinación"
            echo "3) Segunda Declinación"
            echo "4) Cuarta Declinación"
            echo "5) Tercera Declinación"
            echo "6) Volver"
            read -p "Elige: " subop
            case $subop in
                1) cd LATIN/ejercicios_reales && python "ENTRENADOR DE DECLINACIONES LATINAS.py";;
                2) cd LATIN/ejercicios_reales && python " ENTRENADOR DE PRIMERA DECLINACIÓN LATINA.py";;
                3) cd LATIN/ejercicios_reales && python " ENTRENADOR LATÍN- SEGUNDA DECLINACIÓN.py";;
                4) cd LATIN/ejercicios_reales && python "ENTRENADOR DE LA CUARTA DECLINACIÓN LATINA.py";;
                5) cd LATIN/ejercicios_reales && python "Práctica- Tercera declinación en latín.py";;
                6) continue;;
            esac
            ;;
        2)
            echo ""
            echo "=== PROGRAMAS DE INGLÉS ==="
            ls INGLES/tutores/ | nl
            echo ""
            read -p "Elige un número (0 para volver): " subop
            if [ $subop -gt 0 ]; then
                programa=$(ls INGLES/tutores/ | sed -n "${subop}p")
                cd INGLES/tutores && python "$programa"
            fi
            ;;
        3)
            echo ""
            echo "=== PROGRAMAS DE ESPAÑOL ==="
            echo "1) Programa interactivo RAE"
            echo "2) Lecciones de lengua castellana"
            echo "3) Diccionario de lecciones"
            echo "4) Diptongos y tildes"
            echo "5) Sintaxis (60 problemas)"
            echo "6) Versión Kivy"
            echo "7) Volver"
            read -p "Elige: " subop
            case $subop in
                1) cd GRAMATICA_CASTELLANA && python "Programa interactivo para aprender a escribir frases y transformarlas (RAE + ejemplos).py";;
                2) cd GRAMATICA_CASTELLANA && python "lecciones adicionales de lengua castellana_json.py";;
                3) cd GRAMATICA_CASTELLANA && python "Este es el diccionario3lengacastellana principal que contiene TODAS las 100 lecciones .py";;
                4) cd GRAMATICA_CASTELLANA/Ejercicios_palabras_diptongos_hiatos_tíldes && python "identifique los diptongos de las palabras en español en 5 oraciones.py";;
                5) cd GRAMATICA_CASTELLANA/sintaxis_castellana/60problemas_gramatica && python "Oraciones impersonales con sujeto humano y su identidad.py";;
                6) cd GRAMATICA_CASTELLANA && python "versión en Kivy del programa que construimos antes.py";;
                7) continue;;
            esac
            ;;
        4)
            echo ""
            echo "=== JUEGOS EDUCATIVOS ==="
            echo "1) NUEVOS JUEGOS II"
            echo "2) Volver"
            read -p "Elige: " subop
            if [ $subop -eq 1 ]; then
                cd "NUEVOS JUEGOS II"
                ls *.py | head -10
                echo ""
                read -p "Escribe el nombre exacto del juego: " juego
                python "$juego"
            fi
            ;;
        5)
            echo "¡Hasta luego! 👋"
            exit 0
            ;;
    esac
    echo ""
    read -p "Presiona Enter para continuar..."
done
