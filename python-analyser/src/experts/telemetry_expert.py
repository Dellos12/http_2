
import numpy as np


compat_map = {
    'bool': bool, 
    'int': int, 
    'float': float, 
    'object': object,
    'Inf': np.inf, 'INF': np.inf, 'infty': np.inf, 'PZERO': 0.0,
    'alltrue': np.all,
    'sometrue': np.any,
    'round_': np.round,
    'product': np.prod,       # recria o alias removido
    'product_': np.prod,
    'cumproduct_': np.cumprod,
    'alen': lambda x: len(x)
}

for attr, value in compat_map.items():
    if not hasattr(np, attr):
        setattr(np, attr, value)
        
import mxnet as mx
import polars as pl
import json
import redis
import sys
import os



def send_handshake():
    caminho_gold = 'data/gold/gold_atlas.parquet'
    
    if not os.path.exists(caminho_gold):
        print(f"❌ [Telemetria] Falha de Handshake: Gold ausente.")
        sys.exit(1)

    # 1. O Polars extrai a Métrica do Espaço (Oscilação rápida)
    df = pl.read_parquet(caminho_gold)
    zetas_raw = df["zeta_calculado"].to_numpy()

    # 2. MXNet assume o processamento na CPU (O Colapso da Matriz)
    ctx = mx.cpu()
    # Transformamos os dados do Polars em um NDArray do MXNet
    zeta_nd = mx.nd.array(zetas_raw, ctx=ctx)
    
    # Calculamos a média e a norma via MXNet (Operação de Campo)
    media_zeta = mx.nd.mean(zeta_nd).asscalar()
    norma_campo = mx.nd.norm(zeta_nd).asscalar()

    # 3. O Objeto de Telemetria (A Assinatura da Onda com MXNet)
    payload = {
        "step": "Handshake_Gold_MXNet",
        "progress": 100,
        "message": "✅ Geometria Consolidada via MXNet (CPU)",
        "data": {
            "media_zeta": float(round(media_zeta, 4)),
            "norma_campo": float(round(norma_campo, 4)),
            "registros": len(df),
            "motor": "MXNet_CPU",
            "status_membrana": "INTEGRA" if media_zeta <= 0.6 else "RUPTURA"
        }
    }

    # 4. Envia para o Redis (Potencial de Repouso)
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        r.set("telemetria:gold:status", json.dumps(payload))
        print("📡 [Redis] Handshake estacionado na porta 6379 (via MXNet).")
    except:
        print("⚠️ [Aviso] Redis offline, pulso apenas via Stdout.")

    # 5. Envia para o Stdout (Captura do Jenkins)
    print(f"[TELEMETRY] {json.dumps(payload)}")
    sys.stdout.flush()

if __name__ == "__main__":
    send_handshake()
