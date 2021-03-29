import requests
import json
import time

url = "https://api.coinranking.com/v1/public/coin/1/history/30d"
response = requests.get(url)

if response.status_code == 200:
    json_data = json.loads(response.content)
    _price_history_dict = json_data["data"]["history"]

    prev_price = -1
    price_change = ''
    price_direction = ''
    highest = ''
    lowest = ''

    highest_since_start = 0
    lowest_since_start = float('inf')

    k = 0
    output_list = [ ]
    price_history_dict = sorted(_price_history_dict, key = lambda price:price['timestamp'])

    for price_history in price_history_dict:
        price_ts = int(price_history["timestamp"] / 1000)

        _time = time.strftime('%H:%M:%S', time.gmtime(price_ts))

        price = float(price_history["price"])
        if _time != "00:00:00":
            if price > highest_since_start:
                highest_since_start = price
            if price < lowest_since_start:
                lowest_since_start = price
            continue

        output_data = { }
        price_direction = "same"

        if prev_price > 0:
            price_change = price - prev_price
            if price_change < 0:
                price_direction = "down"
            else:
                price_direction = "up"
 
            highest = 'false'
            if price > highest_since_start:
                highest = 'true'
                highest_since_start = price

            lowest = 'false'
            if price < lowest_since_start:
                lowest = 'true'
                lowest_since_start = price
        else:
            price_change = "na"
            price_direction = "na"
            highest = 'true'
            lowest = 'true'
            highest_since_start = price
            lowest_since_start = price

        output_data["date"] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(price_ts))
        output_data["price"] = price
        output_data["direction"] = price_direction
        output_data["change"] = price_change
        output_data["dayOfWeek"] = time.strftime('%A', time.gmtime(price_ts))
        output_data["highSinceStart"] = highest
        output_data["lowSinceStart"] = lowest

        prev_price = price
        output_list.append(output_data)

    with open("coin_ranking_data.json", "a") as f:
        json.dump(output_list, f, indent=2)
