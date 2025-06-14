from typing import Protocol
from app.schemas import TextResponse, TextSearchResponse, TextSaveAnalizys

class BaseRepository(Protocol):
    _data: list[TextSaveAnalizys]
    
    def save_analysis(self, text: str, result: TextResponse) -> list[TextSaveAnalizys]:
        ...
    def get_all(self) -> list[TextResponse]:
        ...
    def search_term(self, term: str) -> TextSearchResponse:
        ...
