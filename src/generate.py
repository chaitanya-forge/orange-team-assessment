

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
        

        ## TODO Implement a generate_answer method that takes a query and returns an answer
        ## TODO Implement a get_closest_docs method that takes a query and returns the closest documents
        ## TODO Implement a openai_llm_answer method that takes a query and returns an answer
