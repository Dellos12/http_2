pipeline {
    agent any

    environment {
        // Usamos o ID da credencial que criamos no Jenkins
        GITHUB_AUTH = credentials('github-auth')
        // Comando sincronizado com o binário v2.27.0 que instalamos
        DOCKER_COMPOSE = "docker compose"
    }

    stages {
        stage('🧼 Limpeza de Campo') {
            steps {
                echo '🧼 Removendo ruídos de builds anteriores...'
                sh "${DOCKER_COMPOSE} down --remove-orphans"
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo o Motor Quântico (Python, Ruby, Go, Envoy)...'
                sh "${DOCKER_COMPOSE} up -d --build"
            }
        }

        stage('🧪 Auditoria de Fase (Zeta 0.5)') {
            steps {
                echo '🧪 Verificando se o Rails ancorou o Benzeno no pgvector...'
                // O Jenkins entra no Rails e confirma se o AROM_001 existe no banco
                sh "docker exec rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                // Validamos se o Go entrega os vizinhos (E1u -> E2g)
                sh "curl -s http://localhost:8080/geometria/vizinhos | grep 'E1u'"
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                // A prova final: o duto binário HTTP/2 está aberto?
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

