from Dependencies.get_api_key import get_gemini_key
from google import genai



client = genai.Client(api_key=get_gemini_key())

while True:
    query = input("What can I do for you? ")

    if not query:
        continue

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=query
    )
    print(response.text)

    end_chat = input("Would you like to continue y/n? ")

    if end_chat and end_chat.lower() == 'n':
        break

