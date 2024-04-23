import json
import requests


def run_req(params):
    func = json.load(open("tool_calling/get_tariffs.json"))
    url = func["base_url"]
    res = requests.get(url, params=params)
    return res.json()


res = run_req({"country": "US", "service": "tariff"})
print(res)
print(json.dumps(res))