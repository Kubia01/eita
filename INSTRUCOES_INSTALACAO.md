# Instruções de Instalação - Proposta Comercial

## 📋 Pré-requisitos

### Para Windows:
1. **Python 3.7+** (recomendado Python 3.11)
   - Baixe em: https://www.python.org/downloads/
   - Marque "Add Python to PATH" durante a instalação

2. **Tkinter** (geralmente vem com Python)
   - Se não estiver disponível, instale via pip:
   ```bash
   pip install tk
   ```

### Para Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-tk python3-pip
```

### Para macOS:
```bash
brew install python3
brew install python-tk
```

## 🚀 Instalação

### Opção 1: Executável (Recomendado)
1. Baixe o arquivo `Proposta-Comercial` (Linux) ou `Proposta-Comercial.exe` (Windows)
2. Execute o arquivo diretamente
3. O sistema criará automaticamente o banco de dados na primeira execução

### Opção 2: Código Fonte
1. Clone ou baixe o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute:
   ```bash
   python main.py
   ```

## 🔐 Primeiro Acesso

- **Usuário:** admin
- **Senha:** admin123

## 📁 Estrutura de Arquivos

O sistema precisa dos seguintes arquivos na mesma pasta do executável:
- `logo.jpg` - Logo para relatórios
- `caploc.jpg` - Imagem de capa para cotações
- `assets/` - Pasta com configurações de filiais

## ⚠️ Solução de Problemas

### Erro "No module named 'tkinter'"
**Windows:**
```bash
pip install tk
```

**Linux:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### Erro de permissão (Linux/macOS)
```bash
chmod +x Proposta-Comercial
```

### Banco de dados não encontrado
- O sistema criará automaticamente o banco na primeira execução
- Certifique-se de que o diretório tem permissões de escrita

## 📞 Suporte

Em caso de problemas, verifique:
1. Se Python 3.7+ está instalado
2. Se tkinter está disponível
3. Se todos os arquivos estão na mesma pasta
4. Se há permissões de escrita no diretório

## 🔄 Atualizações

Para atualizar o sistema:
1. Faça backup do arquivo `crm_compressores.db`
2. Substitua o executável pelo novo
3. Restaure o banco de dados se necessário