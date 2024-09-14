import openai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_response(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    model_engine = "text-davinci-003"
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

def generate_response_35(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.organization = os.getenv('OPENAI_ORGANIZATION')
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=prompt,
        temperature=0.5
    )
    message = response.choices[0].message.content.strip()
    return message