import google.generativeai as genai
import re

from Dependencies.get_api_key import get_gemini_key

genai.configure(api_key=get_gemini_key())


def extract_location(prompt: str) -> str:
    """Extracts a location name from a weather-related prompt."""

    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

    system_prompt = """
    You are a location extraction tool. Your task is to identify and extract the location name from a weather-related sentence.
    Return only the location name. Do not include any additional text. If the location is not found, return an empty string.
    """

    response = model.generate_content(
        contents=[system_prompt, prompt]
    )

    extracted_location = response.text.strip()  # remove extra whitespace.
    if extracted_location == "''" or extracted_location == '""':
        extracted_location = ""  # handle empty string edge case.
    return extracted_location


