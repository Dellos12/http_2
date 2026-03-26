pipeline {
    agent any

    environment {
        // Credencial 'github-auth' (Certifique-se que o ID no Jenkins é exatamente este)
        GITHUB_AUTH = credentials('github-auth')
        
        // 💎 A CURA: Usamos o caminho absoluto que você confirmou no WSL
        DOCKER_BIN = "/usr/bin/docker"
        // No Docker moderno (V2), o compose é um subcomando do docker
        DOCKER_COMPOSE = "/usr/bin/docker compose"
        
        // Trava para evitar erro de instrução AVX/CPU no Polars
        POLARS_SKIP_CPU_CHECK = "1"
        RAILS_ENV = "development"
    }

    stages {
        stage('🧼 Limpeza de Campo') {
            steps {
                script {
                    echo '🧼 Expulsando fantasmas e limpando volumes...'
                    // Usamos a variável DOCKER_BIN para garantir a autoridade do comando
                    sh "${DOCKER_BIN} rm -f redis_frequencia postgres_hiperplano rails_governanca go_entrega envoy_proxy python_especialista || true"
                    
                    // -v remove volumes órfãos para evitar poluição de dados
                    sh "${DOCKER_COMPOSE} down --remove-orphans -v || true"
                    
                    // Limpeza de PIDs para evitar o erro "A server is already running" no Rails
                    sh "rm -f motor_quantico/tmp/pids/server.pid || true"
                }
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo infraestrutura com Invariância de CPU...'
                // Build garantindo que o Polars ignore a checagem de CPU
                sh "POLARS_SKIP_CPU_CHECK=1 ${DOCKER_COMPOSE} up -d --build"
                
                echo '⏳ Aguardando a Âncora e o Motor estabilizarem (30s)...'
                sleep 30
            }
        }

        stage('🧪 Auditoria de Fase (Zeta 0.5)') {
            steps {
                echo '🧪 Verificando ancoragem no pgvector via Rails Runner...'
                // O docker exec interroga o container vivo 'rails_governanca'
                sh "${DOCKER_BIN} exec -t rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                retry(3) {
                    sleep 5
                    // sS mostra erros mas esconde barra de progresso do curl
                    sh "curl -sS http://localhost:8080/geometria/vizinhos | grep 'E1u'"
                }
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                // Prior Knowledge força o HTTP/2 mesmo sem TLS (h2c)
                sh "curl -I --http2-prior-knowledge -s http://localhost:10000/ | grep 'HTTP/2'"
            }
        }

        stage('📈 Auditoria de Carga') {
            steps {
                echo '🚀 Testando escoamento de vetores (Apache Benchmark)...'
                // Testa a resiliência do Envoy sob estresse
                sh "ab -n 100 -c 10 -H 'Connection: Upgrade' -H 'Upgrade: h2c' http://localhost:10000/"
            }
        }
    }

    post {
        success {
            echo '🏆 [BUILD SAGRADO] A Geometria da Informação está estável!'
        }
        failure {
            echo '🚨 [RUPTURA DE FASE] Erro detectado. Extraindo logs para diagnóstico...'
            sh "${DOCKER_COMPOSE} logs --tail=50 motor_quantico"
            sh "${DOCKER_COMPOSE} logs --tail=50 python_analyser" 
        }
    }
}

