@echo off
echo ========================================
echo    SISTEMA CRM COMPRESSORES
echo ========================================
echo.
echo Iniciando sistema...
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

REM Verificar se Docker está rodando
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ERRO: Docker nao esta rodando!
    echo.
    echo 1. Abra o Docker Desktop
    echo 2. Aguarde o Docker inicializar
    echo 3. Execute este script novamente
    echo.
    pause
    exit /b 1
)

echo Docker OK! Construindo imagem...
docker-compose build

if %errorlevel% neq 0 (
    echo ERRO: Falha ao construir a imagem!
    pause
    exit /b 1
)

echo.
echo Imagem construida! Iniciando sistema...
echo.
echo IMPORTANTE:
echo - O sistema sera executado em uma janela separada
echo - Todos os dados serao salvos na pasta 'data'
echo - Para parar o sistema, feche a janela do CRM
echo.

REM Criar pastas necessárias
if not exist "data" mkdir data
if not exist "output" mkdir output
if not exist "logs" mkdir logs

REM Executar o sistema
docker-compose up

echo.
echo Sistema encerrado.
pause