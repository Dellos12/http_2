# syntax=docker/dockerfile:1
ARG RUBY_VERSION=3.3.10
FROM docker.io/library/ruby:$RUBY_VERSION-slim AS base

WORKDIR /rails

# 1. Base: Garantindo o receptor sináptico (postgresql-client)
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y curl libjemalloc2 libvips postgresql-client && \
    ln -s /usr/lib/$(uname -m)-linux-gnu/libjemalloc.so.2 /usr/local/lib/libjemalloc.so && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

# Jemalloc para reduzir a latência de memória no hiperplano
ENV RAILS_ENV="production" \
    BUNDLE_DEPLOYMENT="1" \
    BUNDLE_PATH="/usr/local/bundle" \
    BUNDLE_WITHOUT="development" \
    LD_PRELOAD="/usr/local/lib/libjemalloc.so"

# 2. Build Stage: Onde a massa muscular é formada
FROM base AS build
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y build-essential git libpq-dev libvips libyaml-dev node-gyp pkg-config python-is-python3 && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

# Node e Yarn para os assets geométricos (CSS/JS)
ARG NODE_VERSION=20.11.1
ARG YARN_VERSION=latest
ENV PATH=/usr/local/node/bin:$PATH
RUN curl -sL https://github.com/nodenv/node-build/archive/master.tar.gz | tar xz -C /tmp/ && \
    /tmp/node-build-master/bin/node-build "${NODE_VERSION}" /usr/local/node && \
    rm -rf /tmp/node-build-master
RUN corepack enable && yarn set version $YARN_VERSION

# COPIA DAS GEMS (Ajustado para o contexto na raiz)
# Agora ele busca dentro da pasta motor_quantico
COPY motor_quantico/Gemfile motor_quantico/Gemfile.lock ./
RUN bundle install && \
    rm -rf ~/.bundle/ "${BUNDLE_PATH}"/ruby/*/cache "${BUNDLE_PATH}"/ruby/*/bundler/gems/*/.git && \
    bundle exec bootsnap precompile -j 1 --gemfile

# COPIA DO JS (Ajustado para o contexto na raiz)
COPY motor_quantico/package.json motor_quantico/yarn.lock ./
RUN yarn install --immutable

# COPIA DO CÓDIGO FONTE
COPY motor_quantico/ .

# Pré-compilação do Bootsnap e Assets
RUN bundle exec bootsnap precompile -j 1 app/ lib/
RUN SECRET_KEY_BASE_DUMMY=1 ./bin/rails assets:precompile
RUN rm -rf node_modules

# 3. Final Stage: O Colapso do Corpo Final
FROM base
RUN groupadd --system --gid 1000 rails && \
    useradd rails --uid 1000 --gid 1000 --create-home --shell /bin/bash

# Transfere os artefatos do build para a imagem final (Limpeza de resíduos)
COPY --chown=rails:rails --from=build "${BUNDLE_PATH}" "${BUNDLE_PATH}"
COPY --chown=rails:rails --from=build /rails /rails

# --- A SEÇÃO DE IGNIÇÃO (AMARRA FINAL) ---
# Copia o Entrypoint da pasta física correta para o binário do container
COPY motor_quantico/bin/docker-entrypoint /rails/bin/docker-entrypoint
RUN chmod +x /rails/bin/docker-entrypoint

USER 1000:1000

ENTRYPOINT ["/rails/bin/docker-entrypoint"]
EXPOSE 80
CMD ["./bin/thrust", "./bin/rails", "server"]

