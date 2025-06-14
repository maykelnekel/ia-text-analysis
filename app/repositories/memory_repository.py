from ..model.base_repository import BaseRepository
from app.schemas import TextSearchResponse

class InMemoryRepository(BaseRepository):
    def __init__(self):
        self._data = []

    def save_analysis(self, text, result):
        self._data.append({"text": text, "result": result})

    def get_all(self):
        return self._data

    def search_term(self, term):
        found = False
        text = ""
        if not self._data:
            return {"found": found, "text": text}
        
        last = self._data[-1]["result"]["sentiment_summary"]
        
        if term.lower() in last.lower():
            text = last
            found = True
            
        result: TextSearchResponse = {
            "term": term,
            "found": found,
            "text": text
        }

        return result
    