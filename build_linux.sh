#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT"

APP_NAME="CRM-Compressores"

echo "==> Criando ambiente virtual (.venv)"
python3 -m venv .venv
source .venv/bin/activate

echo "==> Instalando dependências de build (pyinstaller) no venv"
python -m pip install -U pip wheel setuptools
pip install -r requirements.txt
pip install pyinstaller

echo "==> Limpando builds anteriores"
rm -rf build dist "${APP_NAME}.spec" || true

echo "==> Gerando executável onefile"
.venv/bin/pyinstaller --noconfirm \
  --name "$APP_NAME" \
  --onefile \
  --windowed \
  --collect-submodules interface.modules \
  --collect-submodules pdf_generators \
  --add-data "assets:assets" \
  --add-data "caploc.jpg:." \
  --add-data "logo.jpg:." \
  --add-data "cabeçalho.jpeg:." \
  --add-data "cabecalho.jpeg:." \
  main.py

echo "==> Pronto! Arquivo gerado em: dist/${APP_NAME}"
echo "Coloque o binário em uma pasta com permissão de escrita para criar 'data/' e o banco SQLite ao lado."

deactivate || true

