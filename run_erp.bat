@echo off
echo ==========================================
echo   Chemical ERP - Launcher
echo ==========================================

echo Starting Backend...
start "ChemERP Backend" cmd /k "cd backend && (py server.py || python server.py)"

echo.
echo Starting Frontend...
start "ChemERP Frontend" cmd /k "cd frontend && cmd /c npm run dev"

echo.
echo ==========================================
echo   System is starting!
echo   Frontend: http://localhost:5173
echo   Backend Docs: http://localhost:8000/api/docs
echo ==========================================
timeout /t 5
