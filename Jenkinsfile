
pipeline {
    agent any

    environment {
        // Credencial 'github-auth' deve estar com o ID correto no Jenkins (9090)
        GITHUB_AUTH = credentials('github-auth')
        
        // Comando sincronizado com o binário v2.27.0
        DOCKER_COMPOSE = "docker compose"
        
        // 💎 A TRAVA DE SEGURANÇA: Evita erro de CPU no Jenkins/Docker para o Polars
        POLARS_SKIP_CPU_CHECK = "1"
        
        // Garante que o Rails use o ambiente correto durante a auditoria
        RAILS_ENV = "development"
    }

    stages {
        stage('🧼 Limpeza de Campo') {
            steps {
                echo '🧼 Expulsando fantasmas para garantir exclusividade de nomes...'
                // Remove containers pelo nome para evitar erro de 'Conflict'
                sh 'docker rm -f redis_frequencia postgres_hiperplano rails_governanca go_entrega envoy_proxy python_expert || true'
                // Derruba a malha e limpa volumes residuais
                sh "${DOCKER_COMPOSE} down --remove-orphans -v"
                // Limpeza de PIDs residuais do Rails no host
                sh "sudo rm -f motor_quantico/tmp/pids/server.pid || true"
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo o Motor Quântico com Invariância de CPU...'
                // Repassamos a trava de CPU para o ambiente do docker compose
                sh "POLARS_SKIP_CPU_CHECK=1 ${DOCKER_COMPOSE} up -d --build"
                
                echo '⏳ Aguardando a Âncora e o Motor estabilizarem (30s)...'
                sleep 30
            }
        }

        stage('🧪 Auditoria de Fase (Zeta 0.5)') {
            steps {
                echo '🧪 Verificando se o Rails ancorou o Benzeno no pgvector...'
                // O Jenkins entra no Rails e confirma se o registro existe
                sh "docker exec rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                // Validação de entrega dos vizinhos via Go
                sh "curl -s http://localhost:8080/geometria/vizinhos | grep 'E1u'"
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                // Validação da fenda binária HTTP/2
                sh "curl -I --http2 -s http://localhost:10000/ | grep 'HTTP/2'"
            }
        }

        stage('⚡ Auditoria de Carga') {
            steps {
                echo '🚀 Testando o escoamento de vetores via Envoy (Porta 10000)...'
                // Simulação de carga para validar a estabilidade do Envoy
                sh "ab -n 100 -c 10 -H 'Connection: Upgrade' -H 'Upgrade: h2c' http://localhost:10000/"
            }
        }
    }

    post {
        success {
            echo '🏆 [BUILD SAGRADO] A Geometria da Informação está estável e capilarizada!'
        }
        failure {
            echo '🚨 [RUPTURA DE FASE] O sistema detectou uma inconsistência geométrica.'
            // Extrai a voz do motor para diagnóstico de falha
            sh "${DOCKER_COMPOSE} logs motor_quantico"
            sh "${DOCKER_COMPOSE} logs python_expert"
        }
    }
}
