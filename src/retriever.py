import pandas as pd
from openai import OpenAI

class Retriever:
    def __init__(self):
        self.client = OpenAI()
        self.embeddings = {}

    def add_documents(self, docs):
        df = pd.DataFrame({"text": docs})
        embeddings = self.client.embeddings.create(input=df["text"], model="text-embedding-ada-002")
        for i, doc in enumerate(docs):
            self.embeddings[doc] = embeddings.data[i].embedding

    def get_embedding(self, doc):
        response = self.client.embeddings.create(input=doc, model="text-embedding-ada-002")
        return response.data[0].embedding
