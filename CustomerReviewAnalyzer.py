from dotenv import load_dotenv
import os
from google import genai
from google.genai.errors import ClientError
from google.genai.errors import ServerError
from pydantic import BaseModel
from google.genai import types
from Review import Review

class Review(BaseModel):
    Review: str
    Rating: int
    Pros: list[str]
    Cons: list[str]


#load environment variables
load_dotenv()

# define contants
initial_message = "Hi there, Plese type yor review and i can analyze it in details. "

# Initialize Gemini client
def get_gemini_Client():
    return genai.Client()

def ReviewAnalyzer(user_review):
    client = get_gemini_Client()
    return client.models.generate_content(
        model= os.getenv("GEMINI_MODEL_NAME"),
        contents= user_review, 
        config= types.GenerateContentConfig(
            response_mime_type= "application/json",
            response_schema= Review,
        ),
    )
   
def AnalyzeCustomerReview():
     print(initial_message)
     customer_review = input() # "Product is good and it serves the purpose but i do not like the build quality. NOt sure if i can recommend this product.",
     review_analysis = ReviewAnalyzer(customer_review)
     print(review_analysis.text)


AnalyzeCustomerReview()



