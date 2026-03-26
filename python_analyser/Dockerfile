FROM python:3.11-slim

# 1. Dependências de Sistema (O Músculo)
RUN apt-get update && apt-get install -y \
    graphviz \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Instalação do Kit de Sobrevivência (Usando o caminho do contexto raiz)
COPY python-analyser/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install numpy==1.26.4
RUN pip install mxnet>=1.9.1
RUN pip install grpcio-tools polars
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# 3. Gerar os stubs gRPC (Puxando da pasta shared na raiz)
COPY shared/proto/geometria.proto ./proto/
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/geometria.proto

# 4. Copiar o restante do código do especialista
COPY python-analyser/ .

CMD ["python", "app.py"]

