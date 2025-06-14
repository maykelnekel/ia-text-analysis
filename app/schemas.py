from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    word_count: int
    top_words: List[str]
    sentiment_summary: str

class TextSearchResponse(BaseModel):
    term: str
    found: bool
    text: str

class TextSaveAnalizys(BaseModel):
    text: str
    result: TextResponse

class ErrorResponse(BaseModel):
    detail: str