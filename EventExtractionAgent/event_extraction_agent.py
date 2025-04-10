import google.generativeai as genai
import json
from Dependencies.get_api_key import get_gemini_key

genai.configure(api_key=get_gemini_key())

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')


def event_extraction(user_input):
    prompt = f"""
        Extract the event information from the following text and return it as a JSON object with the following format:

        {{'name': 'string name of event', 'date': 'string date of event', 'participants': ['participant1', 'participant2']}}

        Text: {user_input}

        JSON:        
        """

    error_response = {'error': "Unable to extract data based on the information provided"}

    try:
        response = model.generate_content(prompt)

        # Check if response is empty or None
        if not response or not response.text:
            print("Error: Model returned an empty response.")
            return error_response

        # Clean the response text to remove any leading/trailing whitespace or ```json blocks
        cleaned_response = response.text.strip()
        cleaned_response = cleaned_response.removeprefix("```json").removesuffix("```").strip()

        json_response = json.loads(cleaned_response)
        return json.dumps(json_response, indent=2)  # Return as formatted JSON string

    except json.JSONDecodeError:
        print("Error: Could not parse the model's response as valid JSON.")
        print("Raw Response:", response.text)
        return json.dumps(error_response, indent=2)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return json.dumps(error_response, indent=2)


