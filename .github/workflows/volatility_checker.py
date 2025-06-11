import requests


def get_volatility(symbol="BTCUSDT", interval="15m", limit=3):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),  # Приводим к верхнему регистру (btc → BTC)
        "interval": interval,      # Таймфрейм: 1m, 5m, 15m, 1h, 4h и т.д.
        "limit": limit             # Кол-во последних свечей
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Бросает ошибку если код ответа != 200
        data = response.json()

        if not data or len(data) < limit:
            return None, "Недостаточно данных для анализа."

        volatility_results = []
        for candle in data:
            open_price = float(candle[1])
            high_price = float(candle[2])
            low_price = float(candle[3])
            range_percent = ((high_price - low_price) / open_price) * 100
            volatility_results.append(round(range_percent, 2))

        avg_volatility = round(sum(volatility_results) /
                               len(volatility_results), 2)

        # Вывод рекомендаций
        if avg_volatility < 2:
            risk = "Низкая волатильность. Можно использовать x5–x10."
        elif avg_volatility < 5:
            risk = "Средняя волатильность. Лучше x3–x5."
        else:
            risk = "Высокая волатильность. Лучше x1–x3 или не входить."

        return avg_volatility, risk

    except requests.exceptions.RequestException:
        return None, "Ошибка подключения к Binance API. Проверь интернет."
    except Exception as e:
        return None, f"Произошла ошибка: {str(e)}"


# --- ОСНОВНОЙ БЛОК ---
if __name__ == "__main__":
    symbol = input("Введите монету (например, SOLUSDT): ")
    interval = input("Введите таймфрейм (например, 15m, 1h, 4h): ")
    try:
        limit = int(
            input("Введите количество свечей для анализа (например, 3, 5, 10): "))
    except ValueError:
        print("Ошибка: количество свечей должно быть числом.")
        exit()

    vol, advice = get_volatility(symbol, interval, limit)
    if vol is not None:
        print(
            f"\nСредняя волатильность по {symbol} за {limit} свечей ({interval}): {vol}%")
        print(f"Рекомендация по плечу: {advice}")
    else:
        print(f"\nОшибка: {advice}")
