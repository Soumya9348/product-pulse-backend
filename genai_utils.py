from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client instance
client = OpenAI(api_key=api_key)

def summarize_reviews(reviews: str) -> str:
    prompt = f"""
    Summarize the following product reviews into:
    - Pros
    - Cons
    - Overall sentiment

    Reviews:
    {reviews}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful assistant that summarizes product reviews."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

def answer_question(reviews: str, question: str) -> str:
    prompt = f"""
    Based on these product reviews:
    {reviews}

    Answer the following question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful assistant that answers questions about product reviews."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
