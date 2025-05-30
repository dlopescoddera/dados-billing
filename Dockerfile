FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expõe a porta exigida pelo App Runner
EXPOSE 8080

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
