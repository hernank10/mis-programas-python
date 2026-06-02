@echo off
title Instalador - Mis Programas Python
echo ========================================
echo    MIS PROGRAMAS PYTHON - INSTALADOR
echo ========================================
echo.

:: Directorio de instalación
set INSTALL_DIR=%USERPROFILE%\mis_programas_python
mkdir "%INSTALL_DIR%" 2>nul
echo [OK] Instalando en: %INSTALL_DIR%

:: Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no encontrado. Instala Python desde python.org
    pause
    exit /b 1
)

:: Instalar dependencias
echo Instalando dependencias...
pip install colorama nltk

:: Clonar repositorios
cd "%INSTALL_DIR%"
if exist "mis-programas-python" (
    cd mis-programas-python
    git pull
    cd ..
) else (
    git clone https://github.com/Hernank10/mis-programas-python.git
)

if exist "mini-htmls-educativos" (
    cd mini-htmls-educativos
    git pull
    cd ..
) else (
    git clone https://github.com/Hernank10/mini-htmls-educativos.git
)

:: Crear lanzador
echo python menu_principal.py > "%INSTALL_DIR%\ejecutar.bat"

echo.
echo ========================================
echo    INSTALACION COMPLETADA
echo ========================================
echo.
echo Ubicacion: %INSTALL_DIR%
echo.
echo Para ejecutar:
echo   cd %INSTALL_DIR%
echo   ejecutar.bat
echo.
pause
