@echo off
setlocal enableextensions enabledelayedexpansion

set PROJECT_ROOT=%~dp0
cd /d %PROJECT_ROOT%

set APP_NAME=CRM-Compressores

echo ==^> Instalando dependencias de build (pyinstaller)
py -3 -m pip install -U pip wheel setuptools
py -3 -m pip install -r requirements.txt
py -3 -m pip install pyinstaller

echo ==^> Limpando builds anteriores
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist %APP_NAME%.spec del /q %APP_NAME%.spec

echo ==^> Gerando executavel onefile
pyinstaller --noconfirm ^
  --name "%APP_NAME%" ^
  --onefile ^
  --windowed ^
  --collect-submodules interface.modules ^
  --collect-submodules pdf_generators ^
  --add-data "assets;assets" ^
  --add-data "caploc.jpg;." ^
  --add-data "logo.jpg;." ^
  --add-data "cabeçalho.jpeg;." ^
  --add-data "cabecalho.jpeg;." ^
  main.py

echo ==^> Pronto! Arquivo gerado em: dist\%APP_NAME%.exe
echo Coloque o executavel em uma pasta com permissao de escrita para criar 'data\' e o banco SQLite ao lado.

endlocal
