import json
import redis

class HiperplanoGramatical:
    def __init__(self):
        # Mapeamento de Tensão (O que entorta o Zeta Zero)
        self.topologia = {"para": 0.01, "meta": 0.05, "orto": 0.12}
        self.conectores = {"e": 1.1, "com": 1.15}
        self.sujeito_ativo = "AROM_001" # Benzeno Base

    def processar_sentenca(self, query, zeta_base):
        # 1. Resolver Endófora (Pronomes: este, deste)
        if "este" in query.lower() or "deste" in query.lower():
            sujeito = self.sujeito_ativo
            print(f"🔗 [Endófora] Vinculando ao Sujeito: {sujeito}")
        else:
            sujeito = "DESCONHECIDO"

        # 2. Aplicar Tensão Topológica (Nomenclatura)
        desvio_topologico = 0.0
        for p in query.lower().split():
            if p in self.topologia:
                desvio_topologico = self.topologia[p]
                print(f"📐 [Topologia] Desvio {p.upper()} detectado: {desvio_topologico}")

        # 3. Ajuste de Fase (Conectores)
        multiplicador_fase = 1.0
        for p in query.lower().split():
            if p in self.conectores:
                multiplicador_fase *= self.conectores[p]

        # 4. Cálculo do Novo Escalar (O Colapso Gramatical)
        zeta_final = (zeta_base * multiplicador_fase) + desvio_topologico
        
        return {
            "sujeito": sujeito,
            "zeta_final": round(zeta_final, 4),
            "tensao": desvio_topologico,
            "fase_adj": multiplicador_fase
        }

if __name__ == "__main__":
    # Teste de Ignição Gramatical
    motor = HiperplanoGramatical()
    # "Este benzeno com posição orto"
    resultado = motor.processar_sentenca("Este com posição orto", 0.3)
    print(f"📡 [Resultado] Zeta Final: {resultado['zeta_final']} | Sujeito: {resultado['sujeito']}")

