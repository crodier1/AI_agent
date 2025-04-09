from dotenv import load_dotenv
import os


def get_weather_api_key():
    load_dotenv()
    return os.getenv('WEATHER_API_KEY')


def get_gemini_key():
    load_dotenv()
    return os.getenv('GEMINI_API_KEY')
