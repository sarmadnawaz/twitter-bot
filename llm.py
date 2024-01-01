from langchain.llms import OpenAI
import os

class LLM():
    def __init__(self):
        self.llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), temperature=0.7, max_tokens=100);

    def generate(self, prompt):
        return self.llm.invoke(prompt)