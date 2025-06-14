# Sentiment Analysis API

API com integração de IA para análise de texto

Essa API conta com um deploy realizado no render. Esse deploy está atualmente no `tier free`, portanto as primeiras requests podem demorar por conta do `sleep time` e podem haver instabilidades.

> 📢 Acesse a documentação **completa** em: [https://ia-text-analysis.onrender.com/docs](https://ia-text-analysis.onrender.com/docs)

## 📝 Descrição

Esta API permite analisar textos, retornando estatísticas básicas e um resumo de sentimento utilizando inteligência artificial (OpenAI GPT-4).

O projeto foi desenvolvido como desafio técnico para a [Arbitralis](https://www.arbitralis.com.br/).

## ⚙️ Tecnologias Utilizadas

- 🐍 **Linguagem:** Python 3.12
- 🚀 **Framework:** FastAPI
- 🤖 **IA:** OpenAI GPT-4
- 🏭 **Design Pattern:** Repository Pattern
- 📃 **Documentação:** Swagger

## ⚡ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone git@github.com:maykelnekel/sentiment-api.git
   cd sentiment-api
   ```
2. Crie e ative um ambiente virtual:
   - **Linux/MacOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (cmd):**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie o arquivo `.env`:
   ```bash
   touch .env
   ```
5. Configure a variável de ambiente `OPENAI_API_KEY` no arquivo `.env`:
   ```env
   OPENAI_API_KEY="sua-chave-openai"
   ```
6. Execute a API:
   ```bash
   uvicorn app.main:app --reload
   ```

## ✍️ Como usar a API

Essa api conta com uma documentação interativa utilizando Swagger.

Você poderá realizar testes utilizando a própria [documentação em produção](https://ia-text-analysis.onrender.com/docs), sem a necessidade de realizar chamadas à API por meios externos como bash, postman ou insomnia.

> Caso esteja rodando no seu ambiente local, acesse a documentação **completa** em: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📄 Documentação resumida

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
