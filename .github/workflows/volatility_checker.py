import requests


def get_volatility(symbol="BTCUSDT", interval="15m", limit=3):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": limit
    }
    response = requests.get(url, params=params)
    data = response.json()

    volatility_results = []
    for candle in data:
        open_price = float(candle[1])
        high_price = float(candle[2])
        low_price = float(candle[3])

        range_percent = ((high_price - low_price) / open_price) * 100
        volatility_results.append(round(range_percent, 2))

    avg_volatility = round(sum(volatility_results) /
                           len(volatility_results), 2)

    if avg_volatility < 2:
        risk = "Низкая волатильность. Можно использовать x5–x10."
    elif avg_volatility < 5:
        risk = "Средняя волатильность. Лучше x3–x5."
    else:
        risk = "Высокая волатильность. Лучше x1–x3 или не входить."

    return avg_volatility, risk


# Пример использования:
symbol = input("Введите монету (например, SOLUSDT): ")
vol, advice = get_volatility(symbol)
print(f"\nСредняя волатильность за 15м по {symbol}: {vol}%")
print(f"Рекомендация по плечу: {advice}")
