# Usa a imagem oficial do Python 3 como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo app.py para o diretório de trabalho
COPY app.py .

# Executa o script Python quando o container for iniciado
CMD ["python", "app.py"]