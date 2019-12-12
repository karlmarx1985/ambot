import requests
import json

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(Valute):
    for exc in load_exchange():
        if Valute == exc['Valute']:
            return exc
    return False
