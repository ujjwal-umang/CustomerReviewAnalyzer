from pydantic import BaseModel
from google import genai
from google.genai import types

class Review(BaseModel):
    Review: str
    Rating: int
    Pros: list[str]
    Cons: list[str]





    
