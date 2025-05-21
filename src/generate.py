class AnswerGenerator:
    def __init__(self, prompts_file):
        self.prompts_file = prompts_file
        self.retriever = Retriever()
        self.system_prompt, self.user_prompt = self._read_prompts()

    def _read_prompts(self):
        with open(self.prompts_file, "r") as f:
            lines = f.readlines()
            return lines[0].strip(), lines[1].strip()

    def generate_answer(self, question):
        docs = []
        for file in os.listdir(self.data_dir):
            with open(os.path.join(self.data_dir, file), "r") as f:
                docs.append(f.read())
        self.retriever.add_documents(docs)
        context = self.retriever.get_closest_docs(question, n=1)
        prompt = f"{self.system_prompt}\n{self.user_prompt}\nQuestion: {question}\nContext: {context[0]}"
        answer = openai_llm_answer(prompt)
        return answer
