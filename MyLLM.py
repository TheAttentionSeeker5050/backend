from langchain.prompts import ChatPromptTemplate
from utils import select_prompt_by_news_type
from langchain_openai import ChatOpenAI
import os



model = ChatOpenAI(model="gpt-4-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# System template for standard JSON response format
system_template = "Return a JSON array format response for the following query with the keys being name, content, source, and date."

# Define a function to create the LangChain prompt
def build_news_prompt():

    # Construct the prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ('system', system_template),
        ('user', '{text}')
    ])
    
    return prompt_template