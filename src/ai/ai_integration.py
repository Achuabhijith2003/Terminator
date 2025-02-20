import openai
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from utils import config

class AIIntegration:
    def __init__(self):
        # Initialize Chat Model
        self.llm = ChatOpenAI(
            model="gpt-4o",
            openai_api_key=config.OPENAI_API_KEY,  # FIXED API Key
            temperature=0,
            max_retries=2,
        )

        # Initialize Memory (FIXED: Added return_messages=True)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Define Prompt
        self.prompt_template = PromptTemplate(
            input_variables=["chat_history", "user_input"],
            template="This is the chat history: {chat_history}\nUser: {user_input}\nAI:"
        )

        # Create LLM Chain with Memory
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template, memory=self.memory)
    def generate_response(self, prompt):
        response = self.client.completions.create(
            model="gpt-4o-mini",  # Or use "gpt-4"
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def process_with_langchain(self, text):
        # Example of processing text with LangChain
        processed_text = self.langchain.process(text)
        return processed_text
    
    def generate_response_by_langchain(self, prompt):
        # FIXED: Removed dictionary & passed keyword arguments correctly
        result = self.chain.run(chat_history="", user_input=prompt)
        return result
