# Define a imagem base do Docker
FROM python:3.11.3

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt

# Expõe a porta em que o servidor do Django vai rodar
EXPOSE 8000

# Define o comando para executar o servidor do Django
CMD python manage.py runserver 0.0.0.0:8000