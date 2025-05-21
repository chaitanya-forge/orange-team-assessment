# Machine Learning Engineering Assessment: RAG, FastAPI, Docker

## Overview
This assessment tests your ability to implement a simple Retrieval-Augmented Generation (RAG) pipeline using FastAPI, Docker, and basic vector retrieval. You will complete and containerize a minimal RAG API skeleton. You are expected to fill in the blanks (marked as `# TODO` or `# BLANK`) in the provided files.

**Important:** You must use only OpenAI APIs for both embeddings (e.g., `text-embedding-ada-002`) and LLM answer generation (e.g., `gpt-3.5-turbo` or `gpt-4`).

**Skills tested:**
- Vector search and retrieval (RAG)
- FastAPI web development
- Docker containerization
- Python best practices

---

## Running the Application with Docker

### 1. Build the Docker Image
```sh
docker build -t orange-team-assessment .
```
The API will be available at http://localhost:8000

### 3. Develop with Live Code Reload
For local development, mount your code as a volume and enable auto-reload:
```sh
docker run -p 8000:8000 -v $(pwd):/app orange-team-assessment uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Instructions
1. **Clone the repository or download the files.**
2. **Complete the following tasks:**
    - Fill in the blanks in `retriever.py` to implement document embedding and retrieval.
    - Implement the embedding function in `main.py` using the OpenAI Embedding API (see `openai_embed`).
    - Integrate answer generation in the `/query` endpoint using the OpenAI Chat Completion API (see `openai_llm_answer`).
    - **Do NOT hardcode any API keys; use environment variables or configuration.**
    - Complete the `Dockerfile` to containerize the FastAPI app.
    - Add any missing dependencies to `requirements.txt`.
    - (Optional) Fill in the test logic in `test_assessment.py`.
3. **Build and run the application locally and/or in Docker.**
4. **Demonstrate the API by ingesting documents and querying for answers.**
5. **Submit your completed code and a brief write-up (1-2 paragraphs) explaining your approach and any design decisions.**

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
- Ability to reason about and implement vector retrieval
- (Bonus) Test coverage

---

## Good luck!
If you have questions, please ask your interviewer or assessment contact.