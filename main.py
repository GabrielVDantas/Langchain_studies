from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

my_gemini_api_key = os.getenv('GEMINI_API_KEY')

def generate_pet_name():
    llm = GoogleGenerativeAI(model = 'gemini-pro', temperature = 0.5, google_api_key = my_gemini_api_key)

    name = llm('''
               Eu tenho um gato branco e cinza e quero dar um nome legal para ele,
               Sugira cinco nomes. Use o formato de 'bullet points' para mostrá-los 
               ''')
    
    return name

if __name__ == "__main__":
    print(generate_pet_name())