

from openai import OpenAI

import getpass
import os


from dotenv import load_dotenv
load_dotenv()

from src.retriever import Retriever
from src.prompts import FAQ_PROMPT

retriever = Retriever()

class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI()
        self.retriever = retriever
    
    def generate_answer(self, query):
        

        # Retrieve relevant docs from the FAQ
        docs = self.retriever.retrieve(query, k=2)
        docs_content = "\n\n".join(doc.page_content for doc in docs)
        
        # Prepare the prompt
        prompt = FAQ_PROMPT.format(question=query, context=docs_content)
        
        # Use OpenAI API to get answer
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI Assistant that answers questions based on the provided context."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=256,
        )
        answer = response.choices[0].message.content.strip()
        return {"answer": answer, "context": [doc.page_content for doc in docs]}


        ## TODO Implement a generate_answer method that takes a query and returns an answer
        ## TODO Implement a get_closest_docs method that takes a query and returns the closest documents
        ## TODO Implement a openai_llm_answer method that takes a query and returns an answer
