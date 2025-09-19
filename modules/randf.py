# Module for fetching API
# This handles only GET Request
import requests

def fetch_random_fact():
    api_url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()['text']
    else:
        return f'Error: {response.status_code}'