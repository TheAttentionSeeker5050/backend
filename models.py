from pydantic import BaseModel


class NewsRequest(BaseModel):
    news_type: str
    location: str = None