
# syntax=docker/dockerfile:1
ARG RUBY_VERSION=3.3.10
FROM docker.io/library/ruby:$RUBY_VERSION-slim AS base

WORKDIR /rails

# 1. Base: Adicionando o que o Rails 8 precisa para respirar
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y \
    curl libjemalloc2 libvips postgresql-client libpq-dev build-essential && \
    ln -s /usr/lib/$(uname -m)-linux-gnu/libjemalloc.so.2 /usr/local/lib/libjemalloc.so && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

# AJUSTE: Removemos o BUNDLE_DEPLOYMENT="1" para permitir flexibilidade no volume
ENV RAILS_ENV="development" \
    BUNDLE_PATH="/usr/local/bundle" \
    LD_PRELOAD="/usr/local/lib/libjemalloc.so"

# 2. Build Stage
FROM base AS build
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y git libyaml-dev node-gyp pkg-config python-is-python3 && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

# Node/Yarn (Mantemos sua lógica que está correta)
ARG NODE_VERSION=20.11.1
ARG YARN_VERSION=latest
ENV PATH=/usr/local/node/bin:$PATH
RUN curl -sL https://github.com/nodenv/node-build/archive/master.tar.gz | tar xz -C /tmp/ && \
    /tmp/node-build-master/bin/node-build "${NODE_VERSION}" /usr/local/node && \
    rm -rf /tmp/node-build-master
RUN corepack enable && yarn set version $YARN_VERSION

# CÓPIA DAS GEMS: O ponto de colapso
COPY motor_quantico/Gemfile motor_quantico/Gemfile.lock ./
# Rodamos o bundle sem o --deployment para que ele aceite o volume do Compose
RUN bundle install

# ... (Restante do seu COPY motor_quantico/ . e Assets)
