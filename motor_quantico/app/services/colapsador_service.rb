
class ColapsadorService
  def self.executar
    # O Ruby acessa a fenda sináptica para ler a Norma do Gênesis
    caminho = Rails.root.join("data", "gold", "gold_atlas.parquet")
    
    unless File.exist?(caminho)
      return "❌ [Erro] Gold Atlas não encontrado em: #{caminho}"
    end

    # Polars percorre a oscilação do Parquet (Alta Velocidade)
    df = Polars.read_parquet(caminho.to_s)
    
    # Transformamos o DataFrame em uma coleção de 'faces' (hashes)
    faces = df.to_hashes
    
    if faces.any?
      contagem = 0
      
      # O Colapso em Massa: Ancorando cada modo vibracional no pgvector
      faces.each do |data|
        # Evita duplicidade para não poluir o Hiperplano (Opcional)
        next if Simulation.exists?(substantivo: data["molecule_id"], modo_vibracional: data["modo"])

        Simulation.create!(
          substantivo: data["molecule_id"],
          modo_vibracional: data["modo"],
          # O vetor 3D que define a coordenada no espaço químico
          embedding_zeta: [data["zeta_calculado"].to_f, 0.0, 0.0],
          status: "ESTÁVEL",
          metadata: { 
            fonte: "MXNet_CPU", 
            camada: "Gold", 
            timestamp: Time.now.to_s 
          }
        )
        contagem += 1
      end
      
      "✅ [Sucesso] Nuvem de Dados Ancorada: #{contagem} novas faces no Hiperplano."
    else
      "⚠️ [Aviso] Atlas Gold está sem registros para colapsar."
    end
  rescue => e
    "🚨 [Ruptura] Erro no transporte: #{e.message}"
  end
end
