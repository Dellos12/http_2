package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"

    _ "github.com/lib/pq" // Driver de conexão com Postgres
)

func main() {
    // 1. Conexão com a Âncora (Postgres / pgvector) na porta 5432
    connStr := "postgres://devildev:password_quantica@postgres:5432/hiperplano_db?sslmode=disable"
    db, err := sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // 2. Rota de Projeção de Geometria (A Interface do Usuário Final)
    http.HandleFunc("/geometria/vizinhos", func(w http.ResponseWriter, r *http.Request) {
        // O Go interroga o Hiperplano usando o operador de distância do pgvector (<->)
        // Buscamos quem está perto da fase 0.5 (E1u)
        rows, err := db.Query(`
            SELECT modo_vibracional, embedding_zeta
            FROM simulations
            ORDER BY embedding_zeta <-> '[0.5, 0.0, 0.0]'
            LIMIT 3
        `)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        defer rows.Close()

        fmt.Fprintln(w, "🧬 [Go-Worker] Projeção de Vizinhança em Alta Performance:")
        for rows.Next() {
            var modo string
            var zeta string
            if err := rows.Scan(&modo, &zeta); err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }
            fmt.Fprintf(w, " -> Modo: %s | Vetor: %s\n", modo, zeta)
        }
    })

    fmt.Println("🚀 [Go-Worker] Motor de Entrega online na porta 8080...")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

