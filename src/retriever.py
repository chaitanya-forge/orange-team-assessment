from openai import OpenAI

from langchain_openai import OpenAIEmbeddings

## Hint: You are free to use any vector store and document loader
# from langchain_core.vectorstores import InMemoryVectorStore
# from langchain_community.document_loaders import PyPDFLoader

from dotenv import load_dotenv
load_dotenv()

class Retriever:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        ## TODO: Initialize the vector store
        ## TODO: Add documents to the vector store
        self.add_documents("data/FAQs.pdf")

    def get_embedding(self, doc):
        response = self.embeddings.embed_query(doc)
        return response

    def add_documents(self, file_path):
        """
        TODO: Implement this method to load the PDF file, split it into pages, and add to the vector store using embeddings.
        Use PyPDFLoader and InMemoryVectorStore.
        """
        pass

    def retrieve(self, query, k=2):
        """
        TODO: Implement this method to retrieve the k most relevant documents from the vector store for the query.
        """
        pass


if __name__ == "__main__":
    retriever = Retriever()
    # print(retriever.get_embedding("Hello World"))
    retriever.add_documents("data/FAQs.pdf")
    print(retriever.retrieve("Will my offer be confidential?"))
    