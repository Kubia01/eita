#!/usr/bin/env python3
"""
Script de teste para verificar se todas as funcionalidades do sistema estão funcionando
"""

import sys
import os
import sqlite3
import importlib

def test_imports():
    """Testa se todas as dependências estão disponíveis"""
    print("🔍 Testando importações...")
    
    required_modules = [
        'tkinter',
        'fpdf2',
        'PIL',
        'openpyxl',
        'sqlite3',
        'hashlib',
        'requests'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            if module == 'PIL':
                import PIL
            else:
                importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    return len(failed_imports) == 0

def test_database():
    """Testa se o banco de dados pode ser criado e acessado"""
    print("\n🗄️ Testando banco de dados...")
    
    try:
        from database import criar_banco, DB_NAME
        
        # Criar banco
        criar_banco()
        print("✅ Banco criado com sucesso")
        
        # Testar conexão
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Verificar tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        expected_tables = [
            'usuarios', 'clientes', 'contatos', 'produtos', 
            'kit_items', 'tecnicos', 'cotacoes', 'itens_cotacao',
            'relatorios_tecnicos', 'eventos_campo'
        ]
        
        existing_tables = [table[0] for table in tables]
        
        for table in expected_tables:
            if table in existing_tables:
                print(f"✅ Tabela {table}")
            else:
                print(f"❌ Tabela {table} não encontrada")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro no banco de dados: {e}")
        return False

def test_modules():
    """Testa se todos os módulos podem ser importados"""
    print("\n📦 Testando módulos do sistema...")
    
    modules_to_test = [
        'interface.login',
        'interface.main_window',
        'interface.modules.clientes',
        'interface.modules.produtos',
        'interface.modules.cotacoes',
        'interface.modules.relatorios',
        'interface.modules.usuarios',
        'interface.modules.dashboard',
        'pdf_generators.relatorio_tecnico',
        'utils.formatters'
    ]
    
    failed_modules = []
    
    for module in modules_to_test:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_modules.append(module)
    
    return len(failed_modules) == 0

def test_files():
    """Testa se todos os arquivos necessários existem"""
    print("\n📁 Testando arquivos...")
    
    required_files = [
        'main.py',
        'database.py',
        'requirements.txt',
        'logo.jpg',
        'caploc.jpg',
        'cabeçalho.jpeg',
        'modelo-crm.jpg',
        'interface/__init__.py',
        'interface/login.py',
        'interface/main_window.py',
        'interface/modules/__init__.py',
        'interface/modules/clientes.py',
        'interface/modules/produtos.py',
        'interface/modules/cotacoes.py',
        'interface/modules/relatorios.py',
        'interface/modules/usuarios.py',
        'interface/modules/dashboard.py',
        'pdf_generators/__init__.py',
        'pdf_generators/relatorio_tecnico.py',
        'utils/__init__.py',
        'utils/formatters.py'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - NÃO ENCONTRADO")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def test_tkinter():
    """Testa se o Tkinter está funcionando"""
    print("\n🖥️ Testando interface gráfica...")
    
    try:
        import tkinter as tk
        
        # Criar janela de teste
        root = tk.Tk()
        root.withdraw()  # Esconder janela
        
        # Testar widgets básicos
        label = tk.Label(root, text="Teste")
        button = tk.Button(root, text="Teste")
        
        print("✅ Tkinter funcionando")
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Erro no Tkinter: {e}")
        return False

def test_pdf_generation():
    """Testa se a geração de PDF está funcionando"""
    print("\n📄 Testando geração de PDF...")
    
    try:
        from fpdf import FPDF
        
        # Criar PDF de teste
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Teste de PDF", ln=True)
        
        # Salvar PDF de teste
        test_pdf_path = "teste_pdf.pdf"
        pdf.output(test_pdf_path)
        
        # Verificar se arquivo foi criado
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)  # Limpar arquivo de teste
            print("✅ Geração de PDF funcionando")
            return True
        else:
            print("❌ PDF não foi criado")
            return False
            
    except Exception as e:
        print(f"❌ Erro na geração de PDF: {e}")
        return False

def main():
    """Função principal de teste"""
    print("=" * 60)
    print("    TESTE COMPLETO DO SISTEMA CRM COMPRESSORES")
    print("=" * 60)
    
    tests = [
        ("Importações", test_imports),
        ("Arquivos", test_files),
        ("Banco de Dados", test_database),
        ("Módulos", test_modules),
        ("Interface Gráfica", test_tkinter),
        ("Geração de PDF", test_pdf_generation)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erro no teste {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumo final
    print("\n" + "=" * 60)
    print("    RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nResultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n🎉 SISTEMA PRONTO PARA DISTRIBUIÇÃO!")
        print("Todas as funcionalidades estão funcionando corretamente.")
        print("\nPróximos passos:")
        print("1. Execute: gerar_executavel.bat")
        print("2. Ou use Docker: docker-compose build")
        print("3. Siga o GUIA_DISTRIBUICAO.md")
    else:
        print(f"\n⚠️ {total - passed} problema(s) encontrado(s)")
        print("Corrija os problemas antes de distribuir o sistema.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)