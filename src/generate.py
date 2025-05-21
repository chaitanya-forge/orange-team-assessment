

from openai import OpenAI




class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI()
    
    def generate_answer(self, query):
        ## TODO: Implement generate_answer method

        ## TODO Implement a generate_answer method that takes a query and returns an answer
        ## TODO Implement a get_closest_docs method that takes a query and returns the closest documents
        ## TODO Implement a openai_llm_answer method that takes a query and returns an answer
