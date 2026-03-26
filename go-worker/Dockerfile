# Mudamos de 1.21 para a versão que o seu go.mod exige
FROM golang:1.24-alpine

WORKDIR /app

# O restante permanece igual, pois já resolvemos o Vendor
COPY go-worker/go.mod go-worker/go.sum ./
COPY go-worker/vendor ./vendor
COPY go-worker/ .
COPY shared/proto/ ./shared/proto/

RUN go build -mod=vendor -o motor_go main.go

CMD ["./motor_go"]

