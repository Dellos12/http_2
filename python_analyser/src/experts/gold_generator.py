import polars as pl
import os  # <-- Importação vital adicionada para sustentar a pasta data/gold

def mature_to_gold():
    caminho_silver = 'data/silver/vibration_data.parquet'
    caminho_gold = 'data/gold/gold_atlas.parquet'

    # 1. Auditoria de Entrada (Silver)
    if not os.path.exists(caminho_silver):
        print(f"❌ [Log Erro] Camada Silver ausente: {caminho_silver}")
        return

    print("🏆 [Maturação Gold] Destilando a Norma do Gênesis via Polars...")

    # 2. Polars percorre a Silver em alta velocidade (Sem Booleanos)
    # Filtramos apenas o que não rompe o Hiperplano (Zeta <= 0.6)
    df = pl.read_parquet(caminho_silver)
    df_gold = df.filter(pl.col("zeta_calculado") <= 0.6)

    # 3. Ancoragem Física
    os.makedirs('data/gold', exist_ok=True)
    df_gold.write_parquet(caminho_gold)

    # 4. Auditoria de Saída (Gold)
    if os.path.exists(caminho_gold):
        print(f"🔍 [Log Verificação] Norma do Gênesis ancorada: {caminho_gold}")
        print(f"✅ [Gold] Registros estáveis no Atlas: {len(df_gold)}")
        print("🚀 Hiperplano consolidado. O Ruby já pode iniciar as Migrations.")

if __name__ == "__main__":
    mature_to_gold()

