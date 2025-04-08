from dotenv import load_dotenv
import os


def get_open_ai_key():
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')


def get_gemini_key():
    load_dotenv()
    return os.getenv('GEMINI_API_KEY')
