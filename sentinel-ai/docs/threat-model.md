# Threat Model

## Ativos

- Eventos de segurança
- Modelo de Machine Learning
- Credenciais
- Banco de dados
- API

## Ameaças consideradas

- Injeção de dados malformados
- Abuso de API
- Exposição de credenciais
- Manipulação de eventos
- Falsos positivos e negativos
- Modelo treinado com dados contaminados

## Mitigações iniciais

- Validação Pydantic
- Secrets via ambiente
- Testes automatizados
- Separação de configuração
- Baseline de treinamento controlado

Os cenários de ataque devem permanecer em laboratório autorizado.
