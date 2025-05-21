from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str

class RagResponse(BaseModel):
    answer: str
    context: List[str]
