# 🛡️ SentinelAI

### Intelligent Security Analytics & Threat Detection Platform

O **SentinelAI** é uma plataforma de Security Analytics desenvolvida em Python para ingestão, normalização e análise de eventos de segurança, combinando **detecção baseada em regras** com **Machine Learning** para identificação de comportamentos anômalos.

> Projeto educacional para laboratório controlado de Cybersecurity, Machine Learning e DevSecOps.

## ✨ Principais recursos

- Ingestão de eventos de segurança em JSON.
- API REST com FastAPI.
- Persistência em SQLite por padrão e possibilidade de PostgreSQL.
- Rule Engine para detecção determinística.
- Isolation Forest para detecção de anomalias.
- Risk Score de 0 a 100.
- Geração de alertas.
- Dataset sintético para treinamento e testes.
- Testes automatizados com Pytest.
- Docker e Docker Compose.
- GitHub Actions para CI.
- Estrutura preparada para Grafana/Prometheus.

## 🏗️ Arquitetura

```text
                    ┌─────────────────────┐
                    │ Security Events     │
                    │ JSON / API / Logs   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Event Normalizer    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │ Rule Engine  │      │ ML Detector  │
             │ Deterministic│      │ Isolation    │
             └──────┬───────┘      │ Forest       │
                    │              └──────┬───────┘
                    └──────────┬──────────┘
                               ▼
                       ┌──────────────┐
                       │ Risk Engine  │
                       │    0 - 100   │
                       └──────┬───────┘
                              ▼
                       ┌──────────────┐
                       │   Alerts     │
                       └──────┬───────┘
                              ▼
                       ┌──────────────┐
                       │ REST API     │
                       └──────────────┘
```

## 🧰 Stack

- Python 3.12+
- FastAPI
- Pydantic
- SQLAlchemy
- scikit-learn
- pandas
- NumPy
- pytest
- Uvicorn
- Docker / Docker Compose
- GitHub Actions

## 🚀 Executando localmente

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/sentinel-ai.git
cd sentinel-ai
```

### 2. Ambiente virtual

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a API

```bash
uvicorn app.main:app --reload
```

A documentação interativa estará em:

```text
http://127.0.0.1:8000/docs
```

### 5. Execute os testes

```bash
pytest -q
```

## 🐳 Docker

```bash
docker compose up --build
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## 🤖 Machine Learning

O projeto utiliza inicialmente **Isolation Forest**, adequado para detecção de comportamento fora do padrão sem exigir classes previamente rotuladas.

Treinamento:

```bash
python -m ml.train
```

O modelo será salvo em:

```text
ml/models/isolation_forest.joblib
```

O pipeline utiliza features como:

- failed logins;
- requests por minuto;
- bytes transferidos;
- número de conexões;
- hora do evento;
- quantidade de eventos recentes.

## 🔎 Rule Engine

Exemplos de regras:

```text
failed_logins >= 10
requests_per_minute >= 120
connections >= 50
```

Cada regra contribui para o Risk Score.

## 📊 Risk Score

```text
00-29   LOW
30-59   MEDIUM
60-79   HIGH
80-100  CRITICAL
```

O score combina evidências provenientes das regras e do detector de anomalias.

## 🧪 Simulação segura

O repositório inclui geração de dados sintéticos para laboratório:

```bash
python -m data.generate_dataset
```

Isso cria eventos normais e anômalos sem interagir com sistemas externos.

## 📁 Estrutura

```text
sentinel-ai/
├── app/
│   ├── api/
│   ├── core/
│   ├── detection/
│   ├── models/
│   ├── schemas/
│   └── main.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── generate_dataset.py
├── ml/
│   ├── train.py
│   ├── inference.py
│   └── models/
├── tests/
├── infrastructure/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🔐 Segurança

Boas práticas consideradas:

- validação de entrada com Pydantic;
- secrets via variáveis de ambiente;
- separação entre configuração e código;
- logs estruturados;
- princípio do menor privilégio;
- testes automatizados;
- execução em ambiente controlado.

**Nunca coloque senhas, tokens, chaves privadas ou arquivos `.env` no GitHub.**

## 🗺️ Roadmap

- [x] API inicial
- [x] Rule Engine
- [x] Risk Score
- [x] Dataset sintético
- [x] Isolation Forest
- [x] Testes
- [x] Docker
- [x] CI
- [ ] PostgreSQL
- [ ] Redis/Celery
- [ ] Prometheus
- [ ] Grafana
- [ ] Autenticação JWT
- [ ] Threat Intelligence
- [ ] Dashboard web
- [ ] Benchmark de modelos
- [ ] Deploy em cloud

## ⚠️ Disclaimer

Este projeto é destinado a fins educacionais, acadêmicos e de pesquisa. Simulações devem permanecer em ambientes autorizados e controlados.

## 👩‍💻 Autora

**Alessandra**

`Python` · `Cybersecurity` · `Machine Learning` · `DevSecOps` · `Security Analytics`
