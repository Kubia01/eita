# 🚀 Proposta Comercial - Executável

## 📦 O que está incluído

Este pacote contém o sistema **Proposta Comercial** completo e funcional:

- ✅ **Executável principal**: `Proposta-Comercial`
- ✅ **Arquivos de imagem**: `logo.jpg`, `caploc.jpg`
- ✅ **Configurações**: Pasta `assets/` com configurações de filiais
- ✅ **Banco de dados**: Será criado automaticamente na primeira execução
- ✅ **Script de instalação**: `instalar_dependencias.sh`
- ✅ **Instruções**: `INSTRUCOES_INSTALACAO.md`

## 🔧 Instalação Rápida

### Linux/macOS:
```bash
# 1. Dar permissão de execução
chmod +x Proposta-Comercial
chmod +x instalar_dependencias.sh

# 2. Instalar dependências (se necessário)
./instalar_dependencias.sh

# 3. Executar o sistema
./Proposta-Comercial
```

### Windows:
1. Instale Python 3.7+ de https://www.python.org/downloads/
2. Execute o arquivo `Proposta-Comercial.exe`

## 🔐 Primeiro Acesso

- **Usuário:** `admin`
- **Senha:** `admin123`

## 📋 Funcionalidades

### Módulos Disponíveis:
- 👥 **Clientes**: Gestão completa de clientes
- 📦 **Produtos**: Cadastro de produtos, serviços e kits
- 💼 **Serviços**: Cotações de serviços com PDF
- 📄 **Locação**: Cotações de locação com PDF
- 📋 **Relatórios**: Relatórios técnicos com PDF
- 👤 **Usuários**: Gestão de usuários do sistema
- 🔐 **Permissões**: Controle de acesso por módulo

### Recursos:
- ✅ Interface moderna e intuitiva
- ✅ Geração de PDFs profissionais
- ✅ Sistema de permissões
- ✅ Banco de dados SQLite
- ✅ Backup automático de dados

## ⚠️ Requisitos do Sistema

### Mínimos:
- **Sistema Operacional**: Windows 10+, Linux, macOS
- **Python**: 3.7+ (para execução do código fonte)
- **Tkinter**: Para interface gráfica
- **Memória**: 512MB RAM
- **Espaço**: 100MB em disco

### Recomendados:
- **Python**: 3.11+
- **Memória**: 2GB RAM
- **Espaço**: 500MB em disco

## 🛠️ Solução de Problemas

### Erro "No module named 'tkinter'"
**Linux:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
```bash
pip install tk
```

### Erro de permissão (Linux/macOS)
```bash
chmod +x Proposta-Comercial
```

### Sistema não inicia
1. Verifique se Python 3.7+ está instalado
2. Execute: `python3 -c "import tkinter; print('OK')"`
3. Verifique se todos os arquivos estão na mesma pasta

## 📞 Suporte

Para suporte técnico:
1. Verifique as instruções em `INSTRUCOES_INSTALACAO.md`
2. Execute o script `instalar_dependencias.sh`
3. Verifique se todos os requisitos estão atendidos

## 🔄 Atualizações

Para atualizar o sistema:
1. Faça backup do arquivo `crm_compressores.db`
2. Substitua o executável pelo novo
3. Restaure o banco de dados se necessário

---

**Desenvolvido com ❤️ para World Compressores**