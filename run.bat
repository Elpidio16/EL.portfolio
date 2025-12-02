@echo off
REM Script pour lancer le portfolio localement sur Windows

echo.
echo ========================================
echo  Portfolio - Lancement en Developpement
echo ========================================
echo.

REM Vérifier si venv existe
if not exist "venv" (
    echo Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer venv
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo Installation des dépendances...
pip install -r requirements.txt

REM Lancer l'application
echo.
echo ========================================
echo  Application en cours de demarrage...
echo  Ouvrez votre navigateur:
echo  http://localhost:5000
echo ========================================
echo.

python app/app.py

pause
