#!/usr/bin/env python3
"""
Script de instalação automática de dependências para o Sistema CRM Compressores
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Executa um comando e mostra o progresso"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ERRO")
        print(f"Erro: {e.stderr}")
        return False

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 ou superior é necessário!")
        print(f"Versão atual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def install_dependencies():
    """Instala todas as dependências necessárias"""
    print("🚀 Iniciando instalação de dependências...")
    
    # Verificar Python
    if not check_python_version():
        return False
    
    # Atualizar pip
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Atualizando pip"):
        return False
    
    # Instalar dependências do requirements.txt
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Instalando dependências do sistema"):
        return False
    
    # Verificar se tkinter está disponível
    try:
        import tkinter
        print("✅ Tkinter - OK")
    except ImportError:
        print("❌ Tkinter não está disponível!")
        print("No Windows: Reinstale o Python marcando 'tcl/tk and IDLE'")
        print("No Linux: sudo apt-get install python3-tk")
        print("No macOS: brew install python-tk")
        return False
    
    # Verificar outras dependências
    dependencies = ['fpdf2', 'PIL', 'openpyxl']
    for dep in dependencies:
        try:
            if dep == 'PIL':
                import PIL
            else:
                __import__(dep)
            print(f"✅ {dep} - OK")
        except ImportError:
            print(f"❌ {dep} não está instalado!")
            return False
    
    return True

def create_directories():
    """Cria diretórios necessários"""
    print("\n📁 Criando diretórios...")
    
    directories = ['data', 'output', 'logs']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Criado: {directory}/")
        else:
            print(f"✅ Existe: {directory}/")

def main():
    """Função principal"""
    print("=" * 50)
    print("    SISTEMA CRM COMPRESSORES")
    print("    Instalador de Dependências")
    print("=" * 50)
    
    # Detectar sistema operacional
    system = platform.system()
    print(f"\n🖥️  Sistema: {system}")
    
    # Instalar dependências
    if not install_dependencies():
        print("\n❌ Falha na instalação de dependências!")
        print("Verifique os erros acima e tente novamente.")
        input("\nPressione Enter para sair...")
        return 1
    
    # Criar diretórios
    create_directories()
    
    print("\n" + "=" * 50)
    print("✅ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 50)
    print("\nPara executar o sistema:")
    print("python main.py")
    print("\nOu use o script de execução:")
    if system == "Windows":
        print("executar_sistema.bat")
    else:
        print("./executar_sistema.sh")
    
    input("\nPressione Enter para sair...")
    return 0

if __name__ == "__main__":
    sys.exit(main())