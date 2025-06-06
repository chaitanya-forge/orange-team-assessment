from fastapi import  APIRouter, HTTPException
from typing import List
from models import QueryRequest, RagResponse
from src.generate import AnswerGenerator

# Instantiate once for reuse
answer_generator = AnswerGenerator()

router = APIRouter()

## TODO: Add a Health Check endpoint
## COde Here

@router.get("/health")
def health_check():
    ## TODO: Implement a health check endpoint
    pass

@router.post("/query", response_model=RagResponse)
def rag_query(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query must not be empty.")

    # TODO: Generate answer and context using AnswerGenerator
    # Call answer_generator.generate_answer(req.query) and return RagResponse
    # Example:
    # result = answer_generator.generate_answer(req.query)
    # return RagResponse(answer=result["answer"], context=result["context"])
    pass

@router.post("/ingest")
def ingest_docs(docs: List[str]):
    if not docs:
        raise HTTPException(status_code=400, detail="No documents provided.")
    # TODO: Call answer_generator.retriever.add_documents with the provided docs
    pass 