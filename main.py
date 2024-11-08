from dotenv import load_dotenv
import os
import json

# Load .env file, this holds the secret keys and other important variables
load_dotenv()

# The FastAPI server that will be used to host the chatbot
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

# The OpenAI model that will be used to generate responses
from langchain_openai import ChatOpenAI

# The methods to send user and system messages
from langchain_core.messages import HumanMessage, SystemMessage

#Output parser
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-4-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# Make the templates for requests
system_template = "Return a json array format response for the following query with the keys being name, content, source and date:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 3 news in Nova Scotia, Canada
user_template_local = "Show me the top 3 news of the last 24h, my location is nova scotia canada"



# a method to strip the json top and bottom headers from the response
def strip_json_headers(response):
    return response.strip("```json").strip("```")

# Method to parse the result into a JSON object
def parse_result_to_json(result):
    try:
        return json.loads(strip_json_headers(result))  # Parse the response content into a structured JSON object
        
    except json.JSONDecodeError as e:
        print("Error parsing JSON")
        return None
    
# Create output parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | model | parser | parse_result_to_json

# Make the FastAPI REST API
app = FastAPI(
  title="Langchain 3 news API",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces for the web application 3 news, which 3 news with ai, unbiased and fast.",
)

# Adding routes
add_routes(
    app,
    chain,
    path="/news",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


