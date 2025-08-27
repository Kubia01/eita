#!/bin/bash

echo "=== Instalador de Dependências - Proposta Comercial ==="
echo ""

# Detectar sistema operacional
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Sistema Linux detectado"
    echo "Instalando dependências..."
    
    # Verificar se é Ubuntu/Debian
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-tk python3-pip
        echo "✅ Dependências instaladas com sucesso!"
    else
        echo "❌ Sistema não suportado. Instale manualmente:"
        echo "   - Python 3.7+"
        echo "   - Tkinter"
        echo "   - Pip"
    fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Sistema macOS detectado"
    echo "Instalando dependências..."
    
    if command -v brew &> /dev/null; then
        brew install python3
        brew install python-tk
        echo "✅ Dependências instaladas com sucesso!"
    else
        echo "❌ Homebrew não encontrado. Instale manualmente:"
        echo "   brew install python3"
        echo "   brew install python-tk"
    fi

elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Sistema Windows detectado"
    echo "Para Windows, instale manualmente:"
    echo "1. Python 3.7+ de https://www.python.org/downloads/"
    echo "2. Tkinter (geralmente vem com Python)"
    echo "3. Se necessário: pip install tk"
else
    echo "❌ Sistema operacional não reconhecido"
    echo "Instale manualmente:"
    echo "- Python 3.7+"
    echo "- Tkinter"
fi

echo ""
echo "=== Verificação ==="
echo "Testando Python..."
python3 --version

echo ""
echo "Testando Tkinter..."
python3 -c "import tkinter; print('✅ Tkinter OK')" 2>/dev/null || echo "❌ Tkinter não encontrado"

echo ""
echo "=== Instalação Concluída ==="
echo "Agora você pode executar o sistema:"
echo "./Proposta-Comercial"