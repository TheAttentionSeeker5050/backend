from dotenv import load_dotenv
import os

# Load .env file, this holds the secret keys and other important variables
load_dotenv()

# The OpenAI model that will be used to generate responses
from langchain_openai import ChatOpenAI

# The methods to send user and system messages
from langchain_core.messages import HumanMessage, SystemMessage

#Output parser
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-4-turbo", api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    SystemMessage(content="Return a json array format response for the following query with the keys being name, content, source and date:"),
    HumanMessage(content="Show me the top 3 news of the last 24h, my location is nova scotia canada"),
]

result = model.invoke(messages)

parser = StrOutputParser()

parsedResult = parser.invoke(result)

print("Parsed Result: ", parsedResult)

