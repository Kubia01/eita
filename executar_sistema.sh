#!/bin/bash

echo "========================================"
echo "    SISTEMA CRM COMPRESSORES"
echo "========================================"
echo

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não está instalado!"
    echo
    echo "Para instalar o Python:"
    echo "Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "CentOS/RHEL: sudo yum install python3 python3-pip"
    echo "macOS: brew install python3"
    echo
    exit 1
fi

echo "Python OK! Verificando dependências..."

# Verificar se tkinter está disponível
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "ERRO: Tkinter não está disponível!"
    echo
    echo "Para instalar Tkinter:"
    echo "Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "CentOS/RHEL: sudo yum install python3-tkinter"
    echo "macOS: brew install python-tk"
    echo
    exit 1
fi

# Instalar dependências se necessário
if [ ! -f "requirements_installed" ]; then
    echo "Instalando dependências..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        touch requirements_installed
        echo "✅ Dependências instaladas!"
    else
        echo "❌ Erro ao instalar dependências!"
        exit 1
    fi
else
    echo "✅ Dependências já instaladas!"
fi

# Criar diretórios necessários
mkdir -p data output logs

echo
echo "Iniciando sistema..."
echo
echo "IMPORTANTE:"
echo "- O sistema será executado em uma janela separada"
echo "- Todos os dados serão salvos na pasta 'data'"
echo "- Para parar o sistema, feche a janela do CRM"
echo

# Executar o sistema
python3 main.py

echo
echo "Sistema encerrado."