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
                echo '🧼 Expulsando fantasmas pelo nome (Garantia de Identidade)...'
                // Remove pelo nome exato para garantir que o 'Conflict' não ocorra
                sh 'docker rm -f python_expert postgres_hiperplano redis_frequencia rails_governanca go_entrega envoy_proxy || true'
                sh "${DOCKER_COMPOSE} down --remove-orphans -v"
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo o Motor Quântico (Python, Ruby, Go, Envoy)...'
                sh "${DOCKER_COMPOSE} up -d --build"
                
                echo '⏳ Aguardando 15s para a Fenda Sináptica estabilizar (Ressonância)...'
                sleep 15
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



