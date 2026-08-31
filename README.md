# SentinelAI
Intelligent Security Analytics &amp; Threat Detection Platform

# 🛡️ SentinelAI

### Intelligent Security Analytics & Threat Detection Platform

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Sobre o projeto

O **SentinelAI** é uma plataforma de **Security Analytics e detecção de ameaças** desenvolvida em Python.

O sistema combina **detecção baseada em regras** com **Machine Learning**, permitindo identificar comportamentos suspeitos e gerar uma classificação de risco para eventos de segurança.

O projeto foi desenvolvido com foco em conceitos de:

* 🔐 Cybersecurity
* 🤖 Machine Learning
* 🐍 Python
* 🛡️ Security Analytics
* 🚨 Intrusion Detection
* 🔎 Anomaly Detection
* ⚙️ DevSecOps
* 🐳 Docker
* 🧪 Automated Testing

> ⚠️ O projeto utiliza dados sintéticos e deve ser executado em ambientes controlados e autorizados.

---

# 🎯 Objetivos

O principal objetivo é desenvolver uma plataforma capaz de:

* Receber eventos de segurança;
* Validar e normalizar os dados;
* Identificar comportamentos suspeitos;
* Aplicar regras de detecção;
* Utilizar Machine Learning para identificar anomalias;
* Calcular um nível de risco;
* Gerar informações para investigação;
* Disponibilizar os resultados por meio de uma API REST;
* Automatizar testes utilizando CI/CD.

---

# 🏗️ Arquitetura

```text
                         SECURITY EVENTS
                                │
                                ▼
                    ┌─────────────────────┐
                    │    FastAPI REST     │
                    │        API          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Data Validation    │
                    │      Pydantic       │
                    └──────────┬──────────┘
                               │
                     ┌─────────┴─────────┐
                     │                   │
                     ▼                   ▼
              ┌──────────────┐    ┌──────────────┐
              │ Rule Engine  │    │ ML Detector  │
              │              │    │              │
              │ Deterministic│    │ Isolation    │
              │ Detection    │    │ Forest       │
              └──────┬───────┘    └──────┬───────┘
                     │                   │
                     └─────────┬─────────┘
                               ▼
                    ┌─────────────────────┐
                    │     Risk Engine     │
                    │                     │
                    │      0 ── 100       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Security Alert    │
                    └─────────────────────┘
```

---

# 🔎 Como funciona

O fluxo principal do SentinelAI pode ser representado por:

```text
Event
  │
  ▼
Validation
  │
  ▼
Normalization
  │
  ├───────────────┐
  ▼               ▼
Rules             ML
  │               │
  └───────┬───────┘
          ▼
      Risk Score
          │
          ▼
        Alert
```

O sistema analisa diferentes características de um evento, como:

* Tentativas de autenticação;
* Quantidade de requisições;
* Número de conexões;
* Volume de dados transferidos;
* Horário do evento;
* Padrões de comportamento.

---

# 🛡️ Rule Engine

O **Rule Engine** realiza uma primeira camada de detecção utilizando regras determinísticas.

### Exemplos

```text
failed_logins >= 10
        ↓
Brute Force
```

```text
requests_per_minute >= 120
        ↓
API Abuse
```

```text
connections >= 50
        ↓
Connection Spike
```

```text
bytes_transferred >= 10 MB
        ↓
High Data Transfer
```

Cada regra possui um peso específico para o cálculo do risco.

---

# 🤖 Machine Learning

Para detecção de anomalias, o projeto utiliza inicialmente o algoritmo:

### Isolation Forest

O modelo aprende o comportamento considerado normal e identifica eventos que apresentam características significativamente diferentes desse padrão.

```text
                DATASET
                   │
                   ▼
            Data Processing
                   │
                   ▼
          Feature Engineering
                   │
                   ▼
           Isolation Forest
                   │
                   ▼
          Anomaly Detection
                   │
             ┌─────┴─────┐
             ▼           ▼
           Normal     Anomaly 🚨
```

### Features utilizadas

```text
failed_logins
requests_per_minute
connections
bytes_transferred
hour
```

---

# 📊 Risk Score

O SentinelAI combina os resultados das regras e do detector de Machine Learning para produzir um **Risk Score entre 0 e 100**.

|    Score | Nível       |
| -------: | ----------- |
|   0 – 29 | 🟢 LOW      |
|  30 – 59 | 🟡 MEDIUM   |
|  60 – 79 | 🟠 HIGH     |
| 80 – 100 | 🔴 CRITICAL |

Exemplo:

```json
{
  "risk": {
    "score": 85,
    "level": "CRITICAL"
  }
}
```

---

# 🧪 Dataset

O projeto possui um gerador de **dados sintéticos**, permitindo executar experimentos sem utilizar sistemas reais.

Para gerar o dataset:

```bash
python -m data.generate_dataset
```

O arquivo será criado em:

```text
data/raw/security_events.csv
```

---

# 🧠 Treinamento do modelo

Após gerar o dataset:

```bash
python -m ml.train
```

O modelo treinado será salvo em:

```text
ml/models/isolation_forest.joblib
```

Para realizar uma inferência:

```bash
python -m ml.inference
```

---

# 🚀 Instalação

## Pré-requisitos

* Python 3.12+
* Git
* Docker — opcional

---

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/sentinel-ai.git

cd sentinel-ai
```

---

## 2. Crie o ambiente virtual

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando a API

Execute:

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa do Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 Endpoints

### Health Check

```http
GET /health
```

Resposta:

```json
{
  "status": "healthy"
}
```

---

### Analisar evento

```http
POST /api/v1/events/analyze
```

Exemplo:

```json
{
  "event_id": "evt-001",
  "timestamp": "2026-08-31T14:00:00Z",
  "source_ip": "192.0.2.10",
  "event_type": "authentication",
  "failed_logins": 20,
  "requests_per_minute": 250,
  "connections": 80,
  "bytes_transferred": 20000000,
  "hour": 2
}
```

O sistema retorna informações relacionadas às regras, anomalias e risco.

---

# 🐳 Docker

O projeto também pode ser executado utilizando Docker.

```bash
docker compose up --build
```

Verifique os containers:

```bash
docker compose ps
```

Visualize os logs:

```bash
docker compose logs -f
```

---

# 🧪 Testes

O projeto utiliza **Pytest**.

Execute:

```bash
pytest -q
```

Os testes verificam componentes como:

* API;
* Health Check;
* Rule Engine;
* Detecção;
* Risk Engine.

---

# ⚙️ CI/CD

O projeto possui um workflow do **GitHub Actions**.

O pipeline realiza:

```text
Push / Pull Request
        │
        ▼
   Checkout
        │
        ▼
 Setup Python
        │
        ▼
Install Dependencies
        │
        ▼
Generate Dataset
        │
        ▼
Train Model
        │
        ▼
    Run Tests
```

Isso permite validar automaticamente o projeto a cada alteração.

---

# 📁 Estrutura do projeto

```text
sentinel-ai/
│
├── app/
│   ├── api/
│   │   ├── routes_events.py
│   │   └── routes_health.py
│   │
│   ├── detection/
│   │   ├── anomaly_detector.py
│   │   ├── risk_engine.py
│   │   └── rule_engine.py
│   │
│   ├── schemas/
│   │   └── event.py
│   │
│   └── main.py
│
├── data/
│   ├── raw/
│   └── generate_dataset.py
│
├── ml/
│   ├── models/
│   ├── inference.py
│   └── train.py
│
├── tests/
│   ├── test_api.py
│   ├── test_health.py
│   └── test_rules.py
│
├── docs/
│   ├── architecture.md
│   └── threat-model.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 🔐 Segurança

O projeto segue algumas práticas básicas de segurança:

* Validação de entrada com Pydantic;
* Separação de configuração e código;
* Variáveis de ambiente para configurações;
* Não versionamento de arquivos `.env`;
* Testes automatizados;
* Logs e análise de eventos;
* Princípio do menor privilégio;
* Execução de testes em ambiente controlado.

### Threat Modeling

O projeto também possui documentação de Threat Modeling em:

```text
docs/threat-model.md
```

Entre os riscos considerados estão:

* Manipulação de eventos;
* Abuso da API;
* Dados malformados;
* Exposição de credenciais;
* Contaminação do dataset;
* Falsos positivos;
* Falsos negativos;
* Manipulação do modelo.

---

# 📈 Próximas evoluções

## Backend

* [ ] PostgreSQL
* [ ] SQLAlchemy Repository
* [ ] Redis
* [ ] Celery
* [ ] Autenticação JWT
* [ ] RBAC

## Machine Learning

* [x] Isolation Forest
* [ ] Random Forest
* [ ] XGBoost
* [ ] Comparação de modelos
* [ ] Feature importance
* [ ] Cross-validation
* [ ] ROC-AUC
* [ ] Precision-Recall Curve

## Security Analytics

* [x] Rule Engine
* [x] Risk Score
* [x] Anomaly Detection
* [ ] Threat Intelligence
* [ ] IOC matching
* [ ] Correlation Engine
* [ ] MITRE ATT&CK mapping

## Observabilidade

* [ ] Prometheus
* [ ] Grafana
* [ ] Métricas da API
* [ ] Alertas
* [ ] Dashboard de segurança

## DevSecOps

* [x] Docker
* [x] GitHub Actions
* [x] Automated Testing
* [ ] SAST
* [ ] Dependency Scanning
* [ ] Container Scanning
* [ ] Security Quality Gate

---

# 🗺️ Roadmap

```text
              SENTINELAI
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
    SECURITY                 ML
        │                     │
    Rule Engine         Anomaly Detection
        │                     │
        └──────────┬──────────┘
                   ▼
              Risk Engine
                   │
                   ▼
             Security API
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   Dashboard              Alerts
        │                     │
        └──────────┬──────────┘
                   ▼
              DevSecOps
```

---

# 📚 Documentação

| Documento              | Descrição                 |
| ---------------------- | ------------------------- |
| `README.md`            | Documentação principal    |
| `docs/architecture.md` | Arquitetura do sistema    |
| `docs/threat-model.md` | Modelo de ameaças         |
| `.env.example`         | Variáveis de configuração |

---

# ⚠️ Disclaimer

O **SentinelAI** foi desenvolvido para fins **educacionais, acadêmicos e de pesquisa**.

Os testes e simulações devem ser realizados exclusivamente em ambientes próprios ou com autorização explícita.

O projeto não deve ser utilizado para monitorar, atacar ou interferir em sistemas de terceiros.

---

# 👩‍💻 Autora

### Alessandra

Projeto desenvolvido como laboratório prático de:

**Cybersecurity · Python · Machine Learning · Security Analytics · DevSecOps**

---

# ⭐ Contribuições

Sugestões, melhorias e contribuições são bem-vindas.

Se o projeto foi útil para você, considere deixar uma ⭐ no repositório.

---

# 📄 License

Este projeto está distribuído sob a licença **MIT**.
