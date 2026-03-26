pipeline {
    agent any

    environment {
        // Credencial 'github-auth' deve estar com o ID correto no Jenkins (9090)
        GITHUB_AUTH = credentials('github-auth')
        // Comando sincronizado com o binário v2.27.0
        DOCKER_COMPOSE = "docker compose"
    }

    stages {
        stage('🧼 Limpeza de Campo') {
            steps {
                echo '🧼 Expulsando fantasmas para garantir exclusividade de nomes...'
                sh 'docker rm -f redis_frequencia postgres_hiperplano rails_governanca go_entrega envoy_proxy python_expert || true'
                sh "${DOCKER_COMPOSE} down --remove-orphans -v"
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                sh "${DOCKER_COMPOSE} up -d --build"
                echo '⏳ Aguardando a Âncora e o Motor estabilizarem (30s)...'
                sleep 30
            }
        }

        stage('🧪 Auditoria de Fase (Zeta 0.5)') {
            steps {
                echo '🧪 Verificando se o Rails ancorou o Benzeno no pgvector...'
                sh "docker exec rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                sh "curl -s http://localhost:8080/geometria/vizinhos | grep 'E1u'"
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                sh "curl -I --http2 -s http://localhost:10000/ | grep 'HTTP/2'"
            }
        }

        stage('⚡ Auditoria de Carga') {
            steps {
                echo '🚀 Testando o escoamento de vetores via Envoy (Porta 10000)...'
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
            sh "${DOCKER_COMPOSE} logs motor_quantico"
        }
    }
}

