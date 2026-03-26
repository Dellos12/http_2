import polars as pl
import pandas as pd
import torch
import os
import sys

class VibrationExpert:
    def __init__(self):
        # A Tabela de Verdade das Simetrias (Zeta e Frequência)
        # O Substantivo Benzeno colapsa nessas 4 faces lógicas
        self.leis_simetria = {
            "E1u": {"zeta": 0.5, "freq": 1038},
            "E2g": {"zeta": 0.4, "freq": 1596},
            "B2u": {"zeta": 0.0, "freq": 1110},
            "A2g": {"zeta": 0.0, "freq": 1326}
        }

    def verificar_membrana(self, caminho):
        """Verifica se o filamento de dados existe no disco"""
        if os.path.exists(caminho):
            print(f"🔍 [Log Verificação] Arquivo localizado: {caminho}")
            return True
        else:
            print(f"❌ [Log Erro] Arquivo ausente na fenda: {caminho}")
            return False

    def processar_bronze_para_silver(self):
        # 1. Auditoria de Entrada (Bronze)
        caminho_bronze = 'data/bronze/raw_atlas.parquet'
        if not self.verificar_membrana(caminho_bronze):
            print("🛑 Abortando: O sangue bruto (Bronze) não chegou ao especialista.")
            return

        print("🧪 [Especialista Silver] Extraindo Faces Lógicas via Pandas/Torch...")
        
        # Polars percorre a oscilação (Rápido)
        # Nota: Ajustado para ler 'raw_atlas.parquet' conforme seu script de ingestion
        df_bronze = pl.read_parquet(caminho_bronze)
        
        # Pandas sustenta a face lógica na memória
        df_pd = df_bronze.to_pandas()
        
        # O Torch calcula a coerência de fase (Eliminando If/Else)
        def aplicar_geometria(row):
            # No seu ingestion o campo chama-se 'modo', vamos garantir a compatibilidade
            modo = row.get('modo') or row.get('modo_vibracional')
            lei = self.leis_simetria.get(modo, {"zeta": 0.85, "freq": 0}) # 0.85 = Ruptura/Anomalia
            
            # O Escalar Zeta vira um Tensor (Intensidade de Campo)
            zeta_tensor = torch.tensor([lei['zeta']], dtype=torch.float64)
            return zeta_tensor.item()

        df_pd['zeta_calculado'] = df_pd.apply(aplicar_geometria, axis=1)
        
        # 2. Consolidação da Camada Silver
        caminho_silver = 'data/silver/vibration_data.parquet'
        os.makedirs('data/silver', exist_ok=True)
        df_pd.to_parquet(caminho_silver, index=False)
        
        # 3. Auditoria de Saída (Silver)
        if self.verificar_membrana(caminho_silver):
            print(f"✅ Camada Silver Consolidada. Registros processados: {len(df_pd)}")
            print("🚀 O filamento está pronto para o Gold Generator.")

if __name__ == "__main__":
    expert = VibrationExpert()
    expert.processar_bronze_para_silver()

