import requests
import json
from coinapi_config import API_KEY, BASE_URL

headers = {'X-CoinAPI-Key': API_KEY}


'''def coinapi_service_get_all_assets():
    url = BASE_URL + 'v1/assets'
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
        print("Quota restant:", response.headers["x-ratelimit-remaining"])
    else:
        # cas d'erreur
        print("L'appel à l'API a retourné une erreur:", response.status_code)
'''


def coin_api_get_exchange_rates():
    
    url = BASE_URL + 'v1/exchangerate/BTC/EUR/history?period_id=1DAY&time_start=2021-01-01T00:00:00&time_end=2021-01-10T00:00:00'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("L'appel à l'API a fonctionné")
        data = json.loads(response.text)
        # print(data)
        return data
    else:
        print("L'appel à l'API a retourné une erreur:", response.status_code)
        return None
