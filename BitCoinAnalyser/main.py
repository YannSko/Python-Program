import requests
import json
from api_config import API_KEY

BASE_URL = 'https://rest.coinapi.io/'

url = BASE_URL + 'v1/assets'
headers = {'X-CoinAPI-Key': API_KEY}
response = requests.get(url, headers=headers)

data = json.loads(response.text)

print()