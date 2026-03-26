
import polars as pl
import os

def run_ingestion():
    print("🏗️ [Bronze] Ancorando Substantivos no Hiperplano...")
    
    # Catálogo de Simetria: Benzeno (AROM_001) e suas Faces
    catalogo = [
        {'molecule_id': 'AROM_001', 'modo': 'E1u', 'hibridizacao': 'sp2'},
        {'molecule_id': 'AROM_001', 'modo': 'E2g', 'hibridizacao': 'sp2'},
        {'molecule_id': 'AROM_001', 'modo': 'B2u', 'hibridizacao': 'sp2'},
        {'molecule_id': 'SAT_001',  'modo': 'CH_STRETCH', 'hibridizacao': 'sp3'}
    ]
    
    df = pl.DataFrame(catalogo)
    os.makedirs('data/bronze', exist_ok=True)
    df.write_parquet('data/bronze/raw_atlas.parquet')
    print("✅ [Bronze] raw_atlas.parquet gerado com sucesso.")

if __name__ == "__main__":
    run_ingestion()
