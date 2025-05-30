FROM python:3.10-slim

WORKDIR /app

# Copia o requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para o container
COPY . .

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar o Streamlit no container, liberando conexões externas
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
