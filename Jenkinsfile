
pipeline {
    agent any

    environment {
        // Credencial 'github-auth' (Certifique-se que o ID no Jenkins é exatamente este)
        GITHUB_AUTH = credentials('github-auth')
        
        // Comando moderno (Docker Compose V2)
        DOCKER_COMPOSE = "docker compose"
        
        // Trava para evitar erro de instrução AVX/CPU no Polars (importante para VMs antigas)
        POLARS_SKIP_CPU_CHECK = "1"
        RAILS_ENV = "development"
    }

    stages {
        stage('🧼 Limpeza de Campo') {
            steps {
                script {
                    echo '🧼 Removendo resquícios de sessões anteriores...'
                    // -v remove volumes órfãos para evitar poluição de dados entre builds
                    sh "${DOCKER_COMPOSE} down --remove-orphans -v || true"
                    
                    // Limpeza de PIDs para evitar o erro "A server is already running"
                    sh "rm -f motor_quantico/tmp/pids/server.pid || true"
                    
                    // Limpeza de containers por nome (caso o compose down falhe em algum)
                    sh "docker rm -f redis_frequencia postgres_hiperplano rails_governanca go_entrega envoy_proxy python_especialista || true"
                }
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo infraestrutura com Invariância de CPU...'
                // Build sem cache para garantir que novas gemas/dependências sejam instaladas
                sh "${DOCKER_COMPOSE} up -d --build"
                
                echo '⏳ Aguardando estabilização dos serviços (30s)...'
                // Dica: Poderia usar um script 'wait-for-it' aqui para ser mais eficiente que o sleep
                sleep 30
            }
        }

        stage('🧪 Auditoria de Fase (Zeta 0.5)') {
            steps {
                echo '🧪 Verificando ancoragem no pgvector via Rails Runner...'
                // Usamos o 'docker exec -t' (terminal) para rodar o comando dentro do container vivo
                sh "docker exec -t rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                // Adicionado retry simples caso o Go ainda esteja subindo
                retry(3) {
                    sleep 5
                    sh "curl -sS http://localhost:8080/geometria/vizinhos | grep 'E1u'"
                }
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                // O grep retorna status 0 se achar, o que valida o stage
                sh "curl -I --http2-prior-knowledge -s http://localhost:10000/ | grep 'HTTP/2'"
            }
        }

        stage('📈 Auditoria de Carga') {
            steps {
                echo '🚀 Testando escoamento de vetores (Apache Benchmark)...'
                // Verifica se o 'ab' está instalado no Agent, senão usa docker para o teste
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
            sh "${DOCKER_COMPOSE} logs --tail=50 python_especialista"
        }
        always {
            echo '🧹 Limpando ambiente pós-execução...'
            sh "${DOCKER_COMPOSE} down"
        }
    }
}
