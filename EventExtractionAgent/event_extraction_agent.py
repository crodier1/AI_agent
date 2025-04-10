import google.generativeai as genai
from Dependencies.CalendarEvent import CalendarEvent
import json
from Dependencies.get_api_key import get_gemini_key

genai.configure(api_key=get_gemini_key())

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')  # Or another recommended model

while True:
    user_prompt = input("Please provide the name of you next event, the date, and who is going. ")

    if not user_prompt:
        continue

    prompt = f"""
    Extract the event information from the following text and return it as a JSON object that conforms to this Python class:

    class CalendarEvent(BaseModel):
        name: str
        date: str
        participants: list[str]

    Text: {user_prompt}

    JSON:
    """

    try:
        response = model.generate_content(prompt)

        json_response = json.loads(response.text)
        calendar_event = CalendarEvent(**json_response)
        print(calendar_event.json(indent=2))

    except json.JSONDecodeError:
        print("Error: Could not parse the model's response as valid JSON.")
        print("Raw Response:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

    end_chat = input("Would you like to plan another event (y/n)? ")

    if end_chat and end_chat.lower() == 'n':
        break
