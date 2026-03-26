class Simulation < ApplicationRecord
  # Ativa a busca por vizinhos no hiperplano do pgvector
  has_neighbors :embedding_zeta
end
