# Dockerfile para Sistema CRM Compressores
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    tk \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação
COPY . .

# Criar diretório para dados
RUN mkdir -p data

# Expor porta (se necessário para web interface futura)
EXPOSE 8000

# Comando para executar o sistema
CMD ["python", "main.py"]