from coinapi_service import coin_api_get_exchange_rates

rates = coin_api_get_exchange_rates()

if rates:
    print("BTC/EUR, nombre de cours:", len(rates))
    for r in rates:
        print(r["time_period_start"][:10], ":", r["rate_close"])