
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci

def medir_fluidez_campo(id_contexto, zeta_base, tensao_topologica):
    G = nx.Graph()
    
    # Adicionamos nós que representam a "Fenda Sináptica"
    # O peso aqui representa a 'distância' entre os conceitos.
    # Quanto menor o peso, mais 'próximos' e curvos eles estão.
    
    # Conexão Substantivo -> Fase (Zeta do Especialista)
    G.add_edge("Substantivo", "Fase", weight=1.0 / (zeta_base + 0.1)) 
    
    # Conexão Fase -> Topologia (Orto/Meta/Para)
    G.add_edge("Fase", "Topologia", weight=tensao_topologica)
    
    # Conexão Topologia -> Farmaco (A Gramática que amarra)
    G.add_edge("Topologia", "Farmaco", weight=0.1) # Gramática técnica 'puxa' a topologia

    # Calculamos o Colapso de Ricci
    orc = OllivierRicci(G, alpha=0.5, verbose="ERROR")
    orc.compute_ricci_curvature()
    
    # Extraímos a curvatura da aresta de transição
    curvatura = G["Fase"]["Topologia"].get("ricciCurvature", 0)
    
    return round(curvatura, 4)

# Cenário: Benzeno (0.3) em posição Orto (0.12)
f1 = medir_fluidez_campo("AROM_001", 0.3, 0.12)
# Cenário: Benzeno (0.45) em posição Orto (0.12) - Mais 'vibrante'
f2 = medir_fluidez_campo("AROM_001", 0.45, 0.12)

print(f"📊 [Ricci] Curvatura Estática (Zeta 0.3): {f1}")
print(f"🌊 [Ricci] Curvatura Dinâmica (Zeta 0.45): {f2}")



