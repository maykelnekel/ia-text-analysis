import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_sentiment_summary(text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Você é um analisador de sentimentos. Os sentimentos possíveis são: positivo, negativo, neutro. Sua resposta deve estar formatada utilizando markdown"},
                {"role": "user", "content": f"Faça uma análise de sentimento do texto a seguir e diga qual é o sentimento e porque tomou essa decisão: '{text}'"},
                {"role": "user", "content": "extraia o nome do sentimento em uma palavra"}
            ],
            temperature=0.5,
            max_tokens=150
        )
        print(response)
        return response.choices[0].message.content

    except Exception as e:
        return f"Erro na análise de sentimento: {e}"