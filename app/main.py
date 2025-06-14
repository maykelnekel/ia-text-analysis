from fastapi import FastAPI, Query
from app.schemas import TextRequest, TextResponse, TextSearchResponse, ErrorResponse
from app.services.text_analysis import TextAnalysisService
from app.repositories.memory_repository import InMemoryRepository

app = FastAPI(
    title="Sentiment Analysis API",
    description=(
        "API desenvolvida para análise de sentimentos em textos, integrando inteligência artificial (OpenAI GPT-4) para classificação de sentimento, estatísticas de palavras e busca de termos. "
        "Desenvolvido por Maykel Nekel.\n\n"
        "**Contato:** [LinkedIn](https://www.linkedin.com/in/maykelnekel/) | [maykelnekel@gmail.com](mailto:maykelnekel@gmail.com)\n\n"
        "**Repositório no GitHub:** [ia-text-analysis](https://github.com/maykelnekel/ia-text-analysis)\n\n"
        "This is a challenge by [Coodesh](https://coodesh.com/) and [Arbitralis](https://www.arbitralis.com.br/)."
    ),
)

repository = InMemoryRepository()
service = TextAnalysisService(repository)

@app.post(
    "/analyze-text",
    responses={
        200: {"model": TextResponse, "description": "Análise feita com sucesso."},
        422: {"model": ErrorResponse, "description": "O campo 'text' não pode ser vazio."},
    },
    summary="Analisa o texto enviado"
)
def analyze_text_endpoint(data: TextRequest):
    """
    Analisa o texto enviado utilizando IA (OpenAI GPT-4). Informando:
    - a classificação do sentimento:
      - **positivo**
      - **negativo**
      - **neutro**
    - uma breve explicação sobre a classificação;
    - a contagem total de palavras analizadas;
    - as 5 palavras mais frequentes.
    """
    res = service.analyze(data.text)
    return res

@app.get(
    "/search-term",
    responses={
        200: {"model": TextSearchResponse, "description": "Termo encontrado com sucesso."},
        422: {"model": ErrorResponse, "description": "O termo fornecido não está de acordo com a regra de tipo."},
        404: {"model": ErrorResponse, "description": "Nenhuma análise foi realizada ainda."}
    },
    summary="Buscar termo na última análise",
)
def search_term(term: str = Query(..., description="Termo a ser buscado na última análise")):
    """
    Busca se o termo fornecido pelo parâmetro, foi encontrado na resposta da última análise realizada.
    """
    res = service.search_term(term)
    return res
