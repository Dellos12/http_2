#!/bin/bash
echo "🧼 [Limpeza] Iniciando Expurgo de Fantasmas com Superpoderes..."

# 1. Derruba o Compose e remove volumes (Matéria bruta)
docker compose down --remove-orphans -v

# 2. Mata containers pelo nome (Identidade)
docker rm -f postgres_hiperplano redis_frequencia rails_governanca \
           go_entrega envoy_proxy python_expert jenkins_auditor 2>/dev/null || true

# 3. O CORTE CIRÚRGICO (Aqui usamos sudo para vencer o Permission Denied)
sudo rm -f motor_quantico/tmp/pids/server.pid
sudo rm -rf motor_quantico/tmp/cache/bootsnap

# 4. Reset de Redes e Permissões
docker network prune -f
docker container prune -f
sudo chmod -R 777 motor_quantico/tmp # Abre a fenda para o próximo build

echo "✨ [Limpeza] Espaço de Trabalho Totalmente Purificado."

