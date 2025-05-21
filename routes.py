from fastapi import APIRouter, HTTPException
from typing import List
from models import QueryRequest, RagResponse
## TODO: Import generate function from src.generate or src.retriever

router = APIRouter()

## TODO: Add a Health Check endpoint
## COde Here


@router.post("/query", response_model=RagResponse)
def rag_query(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query must not be empty.")

    # TODO: Generate answer using context and query using OpenAI LLM
    # BLANK: Candidate to implement OpenAI LLM call
    # Example: answer = openai_llm_answer(req.query, context)
    answer = "BLANK: Candidate to implement OpenAI LLM answer generation."
    return RagResponse(answer=answer, context=context)

@router.post("/ingest")
def ingest_docs(docs: List[str]):
    if not docs:
        raise HTTPException(status_code=400, detail="No documents provided.")
    retriever.add_documents(docs)
    return {"status": "ok", "num_documents": len(docs)}
