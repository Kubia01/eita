@echo off
echo ========================================
echo    DISTRIBUICAO DO SISTEMA CRM
echo ========================================
echo.

REM Verificar se estamos no Windows
if not "%OS%"=="Windows_NT" (
    echo ERRO: Este script e para Windows!
    echo Use executar_sistema.sh no Linux/macOS
    pause
    exit /b 1
)

echo Sistema: Windows
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

echo Python OK! Verificando dependencias...

REM Instalar dependências
echo.
echo Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    OPCOES DE DISTRIBUICAO
echo ========================================
echo.
echo 1. Gerar Executavel (.exe) - Arquivo unico
echo 2. Docker - Solucao profissional
echo 3. Pacote Completo - Para instalacao manual
echo.
set /p opcao="Escolha uma opcao (1-3): "

if "%opcao%"=="1" goto executavel
if "%opcao%"=="2" goto docker
if "%opcao%"=="3" goto pacote
goto erro

:executavel
echo.
echo ========================================
echo    GERANDO EXECUTAVEL
echo ========================================
echo.

REM Instalar PyInstaller
pip install pyinstaller

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
echo Arquivo: dist/CRM-Compressores.exe
echo.
echo Para distribuir:
echo 1. Copie o arquivo CRM-Compressores.exe
echo 2. Envie para a pessoa que vai usar
echo 3. Ela so precisa executar o arquivo
echo.
goto fim

:docker
echo.
echo ========================================
echo    PREPARANDO DOCKER
echo ========================================
echo.

REM Verificar se Docker está instalado
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Docker nao esta instalado!
    echo.
    echo Para instalar o Docker:
    echo 1. Baixe o Docker Desktop em: https://www.docker.com/products/docker-desktop
    echo 2. Instale e reinicie o computador
    echo 3. Execute este script novamente
    echo.
    pause
    exit /b 1
)

echo Docker OK! Construindo imagem...
docker-compose build

if %errorlevel% neq 0 (
    echo ERRO: Falha ao construir imagem Docker!
    pause
    exit /b 1
)

echo.
echo ========================================
echo    DOCKER PREPARADO COM SUCESSO!
echo ========================================
echo.
echo Para distribuir:
echo 1. Copie toda a pasta do projeto
echo 2. Inclua os arquivos: Dockerfile, docker-compose.yml, executar_sistema.bat
echo 3. A pessoa precisa instalar Docker Desktop
echo 4. Execute: executar_sistema.bat
echo.
goto fim

:pacote
echo.
echo ========================================
echo    CRIANDO PACOTE COMPLETO
echo ========================================
echo.

REM Criar pasta de distribuição
if exist "CRM-Compressores-Distribuicao" rmdir /s /q "CRM-Compressores-Distribuicao"
mkdir "CRM-Compressores-Distribuicao"

REM Copiar arquivos principais
copy "main.py" "CRM-Compressores-Distribuicao\"
copy "database.py" "CRM-Compressores-Distribuicao\"
copy "requirements.txt" "CRM-Compressores-Distribuicao\"
copy "logo.jpg" "CRM-Compressores-Distribuicao\"
copy "caploc.jpg" "CRM-Compressores-Distribuicao\"
copy "cabeçalho.jpeg" "CRM-Compressores-Distribuicao\"
copy "modelo-crm.jpg" "CRM-Compressores-Distribuicao\"
copy "README.md" "CRM-Compressores-Distribuicao\"
copy "instalar_dependencias.py" "CRM-Compressores-Distribuicao\"

REM Copiar pastas
xcopy "interface" "CRM-Compressores-Distribuicao\interface\" /e /i /q
xcopy "pdf_generators" "CRM-Compressores-Distribuicao\pdf_generators\" /e /i /q
xcopy "utils" "CRM-Compressores-Distribuicao\utils\" /e /i /q
if exist "assets" xcopy "assets" "CRM-Compressores-Distribuicao\assets\" /e /i /q

REM Criar arquivo de instruções
echo SISTEMA CRM COMPRESSORES > "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo ======================== >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo. >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo INSTRUCOES DE INSTALACAO: >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo 1. Instalar Python 3.7 ou superior >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo 2. Executar: python instalar_dependencias.py >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo 3. Executar: python main.py >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo. >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo LOGIN PADRAO: >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo - Usuario: admin >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"
echo - Senha: admin123 >> "CRM-Compressores-Distribuicao\COMO_USAR.txt"

echo.
echo ========================================
echo    PACOTE CRIADO COM SUCESSO!
echo ========================================
echo.
echo Pasta: CRM-Compressores-Distribuicao
echo.
echo Para distribuir:
echo 1. Compacte a pasta CRM-Compressores-Distribuicao
echo 2. Envie para a pessoa que vai usar
echo 3. Ela precisa instalar Python e executar as instrucoes
echo.
goto fim

:erro
echo.
echo Opcao invalida! Escolha 1, 2 ou 3.
pause
exit /b 1

:fim
echo.
echo ========================================
echo    DISTRIBUICAO CONCLUIDA!
echo ========================================
echo.
echo IMPORTANTE:
echo - Teste o sistema antes de enviar
echo - Verifique se todas as funcionalidades estao funcionando
echo - Inclua instrucoes claras para o usuario final
echo.
echo Para testar o sistema:
echo python main.py
echo.
pause