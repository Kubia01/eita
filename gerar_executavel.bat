@echo off
echo ========================================
echo    GERANDO EXECUTAVEL DO SISTEMA
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Python nao esta instalado!
    echo.
    echo Para instalar o Python:
    echo 1. Baixe o Python em: https://www.python.org/downloads/
    echo 2. Instale marcando "Add Python to PATH"
    echo 3. Execute este script novamente
    echo.
    pause
    exit /b 1
)

echo Python OK! Instalando dependencias...

REM Atualizar pip
python -m pip install --upgrade pip

REM Instalar dependências
pip install -r requirements.txt

REM Instalar PyInstaller
pip install pyinstaller

echo.
echo Dependencias instaladas! Gerando executavel...
echo.

REM Criar diretório de saída
if not exist "dist" mkdir dist

REM Gerar executável
pyinstaller --noconfirm ^
  --name "CRM-Compressores" ^
  --onefile ^
  --windowed ^
  --add-data "assets;assets" ^
  --add-data "logo.jpg;." ^
  --add-data "caploc.jpg;." ^
  --add-data "cabeçalho.jpeg;." ^
  --add-data "modelo-crm.jpg;." ^
  --icon "logo.jpg" ^
  main.py

if %errorlevel% neq 0 (
    echo ERRO: Falha ao gerar executavel!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    EXECUTAVEL GERADO COM SUCESSO!
echo ========================================
echo.
echo O executavel esta em: dist/CRM-Compressores.exe
echo.
echo Para distribuir:
echo 1. Copie o arquivo CRM-Compressores.exe
echo 2. Envie para a pessoa que vai usar
echo 3. Ela so precisa executar o arquivo
echo.
echo IMPORTANTE:
echo - Na primeira execucao, o sistema criara a pasta 'data'
echo - Todos os dados serao salvos automaticamente
echo - Nao e necessario instalar Python no computador de destino
echo.

pause