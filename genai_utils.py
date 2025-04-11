from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_reviews(reviews: str) -> str:
    prompt = f"""
    Summarize the following product reviews into:
    - Pros
    - Cons
    - Overall sentiment

    Reviews:
    {reviews}
    """

    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the following reviews..."},
            {"role": "user", "content": reviews}
        ]
    )
    
    summary = response.choices[0].message.content
    return summary

def answer_question(reviews: str, question: str) -> str:
    prompt = f"""
    Based on these product reviews:
    {reviews}

    Answer the following question:
    {question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()
