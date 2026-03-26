
import grpc
from concurrent import futures
import time
import os
import redis
import numpy as np
from geomstats.geometry.hypersphere import Hypersphere # Exemplo geométrico

# Importar os arquivos gerados pelo protoc
import geometria_pb2
import geometria_pb2_grpc

# Conexão com o Baú de Dados (Redis)
cache = redis.Redis(host='redis', port=6379, db=0)

class AnalisadorGeometrico(geometria_pb2_grpc.GeometriaServiceServicer):
    def AnalisarEspaco(self, request, context):
        # 1. Lógica de Geometria da Informação (Ex: Distância em uma Hipersfera)
        ponto = np.array([request.x, request.y, request.z])
        
        # Simulação de cálculo de densidade/curvatura
        densidade_calculada = np.linalg.norm(ponto) 
        
        # 2. Persistência no Redis
        cache.set(f"vetor:{request.id}", densidade_calculada)
        
        # 3. Resposta com Identidade do Node (Para o Load Balance)
        return geometria_pb2.AnaliseInfo(
            densidade=densidade_calculada,
            status="VETOR_CURVADO_E_SALVO",
            node_id=os.getenv('HOSTNAME', 'python-node-default')
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    geometria_pb2_grpc.add_GeometriaServiceServicer_to_server(AnalisadorGeometrico(), server)
    server.add_insecure_port('[::]:50051')
    print("Python Analyser: Motor Geométrico rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
