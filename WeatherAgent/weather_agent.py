from Dependencies.get_weather import get_weather_by_city_name
from Dependencies.get_api_key import get_gemini_key
import google.generativeai as genai
import re
from Dependencies.Tool import Tool
from Dependencies.LocationExtraction import extract_location

genai.configure(api_key=get_gemini_key())

tools = [
    Tool(
        name="get_weather_by_city_name",
        description="Gets the current weather given the name of the city and state.",
        func=get_weather_by_city_name,
    ),
]


def generate_weather_report(prompt: str, tools: list[Tool]):
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

    tool_descriptions = "\n".join([f"- {tool.name}: {tool.description}" for tool in tools])

    system_prompt = f"""
    You are a weather reporting agent. You have access to the following tools:
    {tool_descriptions}

    When the user asks for weather information, analyze the prompt to extract the city and state if provided.
    If the city and state are found, call the tool directly with those parameters.
    If the city and state are not found, ask the user to provide them.
    If the user provides the parameters, call the tool.
    If you have the data from the tool, create a weather report based on it.
    If you don't need to use a tool, generate a response based on the users prompt.
    """

    response = model.generate_content(
        contents=[system_prompt, prompt]
    )

    city_state = extract_location(prompt)
    if city_state:
        # city, state = city_state_match.groups()
        try:
            weather_data = tools[0].func(city_state)  # Corrected function call
            # Generate a weather report.

            report = f"The current weather in {weather_data['location']['name']}, {weather_data['location']['region']} is {weather_data['current']['condition']['text']}. The temperature is {weather_data['current']['temp_f']} degrees Fahrenheit."
            return report
        except Exception as e:
            return f"Error getting weather data: {e}"
    return response.text


while True:
    user_prompt = input("What would you like to know about the weather? ")

    if not user_prompt:
        continue

    print(generate_weather_report(user_prompt, tools))

    stop_app = input("Would you like to continue discussing the weather? (y/n) ")

    if stop_app and stop_app.lower() == 'n':
        break
