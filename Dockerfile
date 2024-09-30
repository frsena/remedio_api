# Define a imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -U flask-openapi3[swagger]

# Copia o código-fonte para o diretório de trabalho
COPY . .

# Execute o script de banco de dados
RUN python script_insert_banco.py

# Define o comando de execução da API
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]