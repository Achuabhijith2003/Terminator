import openai
import langchain

class AIIntegration:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)  # Initialize OpenAI client

    def generate_response(self, prompt):
        response = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Or use "gpt-4"
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def process_with_langchain(self, text):
        # Example of processing text with LangChain
        processed_text = self.langchain.process(text)
        return processed_text
    
    