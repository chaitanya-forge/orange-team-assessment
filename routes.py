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
    return {"status": "ok"}


@router.post("/query", response_model=RagResponse)
def rag_query(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query must not be empty.")

    # Generate answer and context using AnswerGenerator
    result = answer_generator.generate_answer(req.query)
    answer = result["answer"]
    context = result["context"]
    return RagResponse(answer=answer, context=context)

@router.post("/ingest")
def ingest_docs(docs: List[str]):
    if not docs:
        raise HTTPException(status_code=400, detail="No documents provided.")
    retriever.add_documents(docs)
    return {"status": "ok", "num_documents": len(docs)}
