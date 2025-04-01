@echo off
echo Starting the game...

REM
tasklist /FI "IMAGENAME eq vcxsrv.exe" 2>NUL | find /I /N "vcxsrv.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo VcXsrv is already running
) else (
    echo Starting VcXsrv...
    start "" "%PROGRAMFILES%\VcXsrv\vcxsrv.exe" :0 -multiwindow -ac
    timeout /t 2
)

REM
echo Starting the game container...
docker-compose up --build -d

echo Game should start in a few seconds...
timeout /t 5

REM
docker-compose logs -f 