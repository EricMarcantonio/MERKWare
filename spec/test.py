import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'
api_key = "2517e33c5fcb245e7baede362f7b41a5c2e1e4c2b57c553a1cd74a8d052eecc6"
params = {'apikey': api_key, 'resource': 'b7f624fecf25afa9d7c1a8d7d1e1df4c780441a72b5709fbaad224f4bad023bf'}

response = requests.get(url, params=params)

print(response.json()["positives"])