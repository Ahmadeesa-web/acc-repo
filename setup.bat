@echo off
echo ==========================================
echo   Chemical ERP - Setup ^& Installation
echo ==========================================

echo [1/2] Installing Backend Dependencies...
py -m pip install -r backend/requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [NOTICE] 'py' failed, trying 'python'...
    python -m pip install -r backend/requirements.txt
)

echo.
echo [2/2] Installing Frontend Dependencies...
cd frontend
cmd /c npm install
cd ..

echo.
echo ==========================================
echo   Setup Complete!
echo   Run 'run_erp.bat' to start the system.
echo ==========================================
pause
