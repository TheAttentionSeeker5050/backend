
# a method to strip the json top and bottom headers from the response
import json

from constants import LOCAL_NEWS, INTERNATIONAL_NEWS, BUSINESS_NEWS, TECH_NEWS, SPORTS_NEWS


def strip_json_headers(response):
    return response.strip("```json").strip("```")

# Method to parse the result into a JSON object
def parse_result_to_json(result):
    try:
        return json.loads(strip_json_headers(result))  # Parse the response content into a structured JSON object
        
    except json.JSONDecodeError as e:
        print("Error parsing JSON")
        return None
    

# Function to select and build the prompt
def select_prompt_by_news_type(news_type, location=None):
    news_type = news_type.lower()
    if news_type == "local":
        return LOCAL_NEWS + (location or " Canada")
    elif news_type == "international":
        return INTERNATIONAL_NEWS
    elif news_type == "business":
        return BUSINESS_NEWS + (location or " North America (USA and Canada)")
    elif news_type == "tech":
        return TECH_NEWS
    elif news_type == "sports":
        return SPORTS_NEWS + (location or " North America (USA and Canada)")
    else:
        return None
    