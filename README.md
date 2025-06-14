# Sentiment Analysis API

API com integração de IA para análise de texto

## Descrição

Esta API permite analisar textos, retornando estatísticas básicas e um resumo de sentimento utilizando inteligência artificial (OpenAI GPT-4). O projeto foi desenvolvido como parte do desafio técnico para a [Arbitralis](https://www.arbitralis.com.br/).

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **IA:** OpenAI GPT-4
- **Design Pattern:** Repository Pattern

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd sentiment-api
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure a variável de ambiente `OPENAI_API_KEY` no arquivo `.env`:
   ```env
   OPENAI_API_KEY="sua-chave-openai"
   ```
5. Execute a API:
   ```bash
   uvicorn app.main:app --reload
   ```

## Como usar a API

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

### 1. Análise de Texto

- **Endpoint:** `POST /analyze-text`
- **Request Body:**
  ```json
  {
    "text": "Seu texto livre aqui..."
  }
  ```
- **Possíveis respostas:**
  - **200**: Análise feita com sucesso.
    ```json
    {
      "word_count": 10,
      "top_words": ["exemplo", "palavra", ...],
      "sentiment_summary": "Resumo em markdown...",
      "sentiment": "positivo"
    }
    ```
  - **422**: O campo 'text' não pode ser vazio.
    ```json
    { "detail": "O campo 'text' não pode ser vazio." }
    ```

### 2. Buscar termo na última análise

- **Endpoint:** `GET /search-term?term=palavra`
- **Possíveis respostas:**
  - **200**: Termo encontrado com sucesso.
    ```json
    {
      "term": "palavra",
      "found": true,
      "text": "Trecho da análise onde o termo aparece"
    }
    ```
  - **422**: O termo fornecido não está de acordo com a regra de tipo.
    ```json
    { "detail": "O parâmetro 'term' não pode ser vazio." }
    ```
  - **404**: Nenhuma análise foi realizada ainda.
    ```json
    { "detail": "Nenhuma análise foi realizada ainda." }
    ```

## Challenge by Coodesh

This is a challenge by [Coodesh](https://coodesh.com/).
