class CreateSimulations < ActiveRecord::Migration[7.1]
  def change
    # Ativa a fenda sináptica no Postgres
    enable_extension "vector" unless extension_enabled?("vector")

    create_table :simulations do |t|
      t.string :substantivo
      t.string :modo_vibracional
      t.vector :embedding_zeta, limit: 3 # [Zeta, 0, 0]
      t.string :status
      t.jsonb :metadata, default: {}

      t.timestamps
    end
  end
end

