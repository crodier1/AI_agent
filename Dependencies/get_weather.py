from Dependencies.get_api_key import get_weather_api_key
import requests


def get_response(url):
    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        # Success: Process the response JSON
        return response.json()
        # print("Response Data:", data)
    else:
        # Handle errors
        print("Error:", response.status_code, response.text)


def get_weather_by_city_name(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={get_weather_api_key()}&q={city}&aqi=no"
    return get_response(url)
