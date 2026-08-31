# Architecture

O SentinelAI separa ingestão, detecção, cálculo de risco e exposição por API.

## Camadas

1. API: recebe eventos.
2. Schemas: valida dados.
3. Rule Engine: aplica regras determinísticas.
4. ML Detector: identifica desvios do baseline.
5. Risk Engine: combina evidências.
6. Alert layer: representa o resultado de risco.

A arquitetura foi desenhada para permitir a substituição do SQLite por PostgreSQL e a inclusão futura de filas, observabilidade e dashboard.
