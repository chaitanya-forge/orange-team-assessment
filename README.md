# Machine Learning Engineering Assessment: RAG, FastAPI

## Overview
This assessment tests your ability to implement a simple Retrieval-Augmented Generation (RAG) pipeline using FastAPI, and basic vector retrieval. You will complete and containerize a minimal RAG API skeleton. You are expected to fill in the blanks (marked as `# TODO` or `# BLANK`) in the provided files.

**Important:** You must use only OpenAI APIs for both embeddings (e.g., `text-embedding-ada-002`) and LLM answer generation (e.g., `gpt-3.5-turbo` or `gpt-4`).


---

## Running the Application

### 1. Create a virtual environment and install dependencies
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Application
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload```
The API will be available at http://localhost:8000

---

## Instructions
1. **Clone the repository or download the files.**
2. **Complete the following tasks:**
    - Fill in the blanks in `src/retriever.py` to implement document embedding and retrieval.
    - Implement the embedding function in `src/generate.py` using the OpenAI Embedding API (see `openai_embed`).
    - Integrate answer generation in the `/query` endpoint using the OpenAI Chat Completion API (see `openai_llm_answer`).
3. **Build and run the application locally and/or in Docker.**
4. **Demonstrate the API by ingesting the document (data/FAQs.pdf).**

---

## File Guide
- `retriever.py`: In-memory vector retriever skeleton. Complete embedding and retrieval logic.
- `main.py`: FastAPI app. Complete embedding integration and RAG endpoint logic.
- `Dockerfile`: Containerization skeleton. Complete to run the FastAPI app in Docker.
- `requirements.txt`: Add any missing dependencies (e.g., for embeddings).

---

## Example API Usage
- `GET /health` with a query string.
- `POST /ingest` with a list of documents (strings).
- `POST /query` with a query string. Returns answer and context.

---

## Evaluation Criteria
- Correctness and completeness of the RAG pipeline
- Code clarity and organization
- Proper use of FastAPI and Docker



Part 1: (Setting up environment, running the app locally)

Part 2: (Implement the retriever)

Part 3: (Implement the generate function)

