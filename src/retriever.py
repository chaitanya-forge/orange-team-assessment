from openai import OpenAI
import numpy as np

class Retriever:
    def __init__(self):
        self.client = OpenAI()

    def get_embedding(self, doc):
        response = self.client.embeddings.create(input=doc, model="text-embedding-ada-002")
        return response.data[0].embedding

    def add_documents(self, docs):
        ## TODO: Implement add_documents method


    def ingest_docs(self, docs):
        ## TODO: Implement ingest_docs method
        
