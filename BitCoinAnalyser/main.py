import requests
import json
from api_config import API_KEY

BASE_URL = 'https://rest.coinapi.io/'

url = BASE_URL + 'v1/assets'
headers = {'X-CoinAPI-Key': API_KEY}
response = requests.get(url, headers=headers)



# 200 / sinon afficher le code d'erreur
if response.status_code == 200:
    print("L'appel à l'API a fonctionné")
    data = json.loads(response.text)
    nb_assets = len(data)
    # asset_id
    # name
    print("Nombre d'assets monétaires:", nb_assets)
    if nb_assets >= 10:
        for i in range(10):
            d = data[i]
            print(d["asset_id"] + ": " + d["name"])

    print()
    print("Quota restant", response.headers["x-ratelimit-remaining"])
else:
    # cas d'erreur
    print("L'appel à l'API a retourné une erreur:", response.status_code)

