FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y docker.io curl
# Garante que o Jenkins pode falar com o Docker do WSL
RUN usermod -aG docker jenkins
USER jenkins
