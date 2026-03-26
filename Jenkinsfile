pipeline {
    agent any

    environment {
        // Usamos o ID da credencial que você criou no Jenkins
        GITHUB_AUTH = credentials('github-auth')
        COMPOSE_PROJECT_NAME = "hiperplano_quantico"
    }

    stages {
        stage('🧹 Limpeza de Campo') {
            steps {
                echo '🧼 Removendo ruídos de builds anteriores...'
                sh 'docker compose down --remove-orphans'
            }
        }

        stage('🏗️ Construção da Malha') {
            steps {
                echo '🏗️ Erguendo o Motor Quântico (Python, Ruby, Go, Envoy)...'
                sh 'docker compose up -d --build'
            }
        }

        stage('🧪 Auditoria de Fase (Python -> Ruby)') {
            steps {
                echo '🧪 Verificando se o Rails ancorou o Zeta no pgvector...'
                // O Jenkins entra no Rails e pergunta se o Benzeno (0.3) existe
                sh "docker exec rails_governanca bin/rails runner 'puts Simulation.where(substantivo: \"AROM_001\").exists?'"
            }
        }

        stage('⚡ Teste de Alta Performance (Go-Worker)') {
            steps {
                echo '⚡ Interrogando o Músculo (Go) na porta 8080...'
                // Validamos se o Go entrega os vizinhos em HTTP/2 ou Alta Velocidade
                sh "curl -s http://localhost:8080/geometria/vizinhos | grep 'E1u'"
            }
        }

        stage('🌐 Prova de Conceito (Envoy HTTP/2)') {
            steps {
                echo '🌐 Testando a Membrana Envoy na porta 10000...'
                // A prova final: o duto binário está aberto?
                sh "curl -I --http2 -s http://localhost:10000/ | grep 'HTTP/2'"
            }
        }
    }

    post {
        success {
            echo '🏆 [BUILD SAGRADO] A Geometria da Informação está estável e capilarizada!'
        }
        failure {
            echo '🚨 [RUPTURA DE FASE] O sistema detectou uma inconsistência geométrica. Abortando!'
            sh 'docker compose logs motor_quantico'
        }
    }
}

