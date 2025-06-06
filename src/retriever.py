from openai import OpenAI

from langchain_openai import OpenAIEmbeddings

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()

class Retriever:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.vector_store = InMemoryVectorStore(self.embeddings)
        self.add_documents("data/FAQs.pdf")

    def get_embedding(self, doc):
        response = self.embeddings.embed_query(doc)
        return response

    def add_documents(self, file_path):
        # Use the synchronous PyPDFLoader and load method
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        self.vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings())

    def retrieve(self, query, k=2):
        docs = self.vector_store.similarity_search(query, k=k)
        return docs


if __name__ == "__main__":

    import asyncio
    

    retriever = Retriever()
    # print(retriever.get_embedding("Hello World"))
    asyncio.run(retriever.add_documents("data/FAQs.pdf"))
    print(retriever.retrieve("Will my offer be confidential?"))
    