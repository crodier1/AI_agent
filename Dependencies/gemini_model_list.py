import google.generativeai as genai
import os

from Dependencies.get_api_key import get_gemini_key

genai.configure(api_key=get_gemini_key())

try:
    models = genai.list_models()

    for model in models:
        print(f"Model: {model.name}")
        print(f"  Description: {model.description}")
        print(f"  Version: {model.version}")
        print(f"  Supported Generation Methods: {model.supported_generation_methods}")
        print("-" * 20)

except Exception as e:
    print(f"An error occurred: {e}")