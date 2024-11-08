from dotenv import load_dotenv

from models import NewsRequest
from utils import parse_result_to_json, select_prompt_by_news_type

# Load .env file, this holds the secret keys and other important variables
load_dotenv()

# The FastAPI server that will be used to host the chatbot
from fastapi import FastAPI, HTTPException
from MyLLM import build_news_prompt, model
from langchain_core.output_parsers import StrOutputParser

# Make the FastAPI REST API
app = FastAPI(
  title="Langchain 3 news API",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces for the web application 3 news, which 3 news with ai, unbiased and fast.",
)


# API route to process the news query
@app.post("/news")
async def get_news(request: NewsRequest):
    try:
        # Build prompt template
        prompt_template = build_news_prompt()

        # Fetch the user-specific message
        user_message = select_prompt_by_news_type(request.news_type, request.location)

        if not user_message:
            raise ValueError("Invalid news type. Please choose from 'local', 'international', 'business', 'tech', or 'sports'.")
        
        # Define the parser and complete the chain
        parser = StrOutputParser()
        chain = prompt_template | model | parser | parse_result_to_json

        # Execute the chain with an empty string as input
        response = chain.invoke({"text": user_message})
        return response
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating news response: " +  str(e))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


