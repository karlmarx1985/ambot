import requests


def get_usd():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    r = requests.get(url).json()
    print(r["Valute"]["USD"]["Value"])
