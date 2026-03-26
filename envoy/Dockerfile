FROM envoyproxy/envoy:v1.29-latest
# Copiamos a configuração que definimos anteriormente
COPY envoy/envoy.yaml /etc/envoy/envoy.yaml
# Permissão para o Envoy ler o mapa da fenda
RUN chmod go+r /etc/envoy/envoy.yaml
EXPOSE 10000

