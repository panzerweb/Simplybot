# Module for retrieving weather data
# import requests for fetching https://goweather.xyz/weather/Davao%20City
import requests

def fetch_weather_by_location(location):
    api_url = f'https://goweather.xyz/weather/{location}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Error: {response.status_code}'

