from dotenv import load_dotenv
import os
from google import genai
from google.genai.errors import ClientError
from google.genai.errors import ServerError
from pydantic import BaseModel
from google.genai import types
from Review import Review

#load environment variables
load_dotenv()

# define contants
initial_message = "Hi there, Please type yor review and allow me to analyze it in details. "

# Initialize Gemini client
def get_gemini_Client():
    return genai.Client()

def ReviewAnalyzer(user_review):
    client = get_gemini_Client()
    try:
        return client.models.generate_content(
        model= os.getenv("GEMINI_MODEL_NAME"),
        contents= user_review, 
        config= types.GenerateContentConfig(
            response_mime_type= "application/json",
            response_schema= Review,
        ))
    except ClientError as client_excp:
        return client_excp
    except Exception as excp:
        return excp

   
def AnalyzeCustomerReview():
    print(initial_message)
    customer_review = input() # "Product is awesome and value for money. It serves the purpose but i do not like the build quality. Not sure if i can recommend this product for long term use.",
    review_analysis = ReviewAnalyzer(customer_review)
    #print(review_analysis.text)

     # Validate before using
    if not hasattr(review_analysis, "parsed"):
        print("Error analyzing review:", review_analysis)
        return
    
    review_obj = review_analysis.parsed
    print (f"Overall rating: {review_obj.Rating}")
    print (f"Customer Sentiment: {review_obj.Sentiment}")
    print (f"Pros: {', '.join(review_obj.Pros)}")
    print (f"Cons: {', '.join(review_obj.Cons)}")
     

AnalyzeCustomerReview()



