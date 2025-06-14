from collections import Counter
from fastapi import HTTPException
import nltk
from nltk.corpus import stopwords
from app.services.ai_client import get_sentiment_summary
from app.model.base_repository import BaseRepository
from app.schemas import TextResponse, TextSearchResponse

nltk.download("punkt")
nltk.download("stopwords")
nltk.download('punkt_tab')

stop_words = set(stopwords.words("portuguese"))

class TextAnalysisService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def _preprocess_top_words(self, text: str):
        tokens = nltk.word_tokenize(text.lower())
        
        words = [w for w in tokens if w.isalpha() and w not in stop_words]

        top_words = [word for word, _ in Counter(words).most_common(5)]

        return top_words

    def analyze(self, text: str) -> TextResponse:
        if not text or not text.strip():
            raise HTTPException(status_code=422, detail="O campo 'text' não pode ser vazio.")

        word_count = len(text.split(" "))

        top_words = self._preprocess_top_words(text)

        sentiment_summary = get_sentiment_summary(text)

        result: TextResponse = {
            "word_count": word_count,
            "top_words": top_words,
            "sentiment_summary": sentiment_summary,
        }

        self.repository.save_analysis(text, result)
        return result
    
    def search_term(self, term: str) -> TextSearchResponse:
        if not term or not term.strip():
            raise HTTPException(status_code=422, detail="O parâmetro 'term' não pode ser vazio.")
        
        data = self.repository.get_all()
        
        if not data:
          raise HTTPException(status_code=404, detail="Nenhuma análise foi realizada ainda.")
        
        result = self.repository.search_term(term)
        
        if not result["found"]:
          raise HTTPException(status_code=404, detail="Nenhum termo foi encontrado.")
            
        return {"term": term, "found": result["found"], "text": result["text"]}
