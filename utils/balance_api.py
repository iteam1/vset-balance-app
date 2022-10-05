import requests
import json

base_url = 'https://gold-pos.vvs.vn/parse/classes/GoldWeight/IXvPHGKTen'

data = {"value":5.2}

headers = {
    'X-Parse-Application-Id':'SCWASRTWK1Y9AVMP1KFC',
    'Content-Type':'application/json'
}

with requests.Session() as s:
    res = s.put(base_url,headers=headers,data=json.dumps(data))
    print(res.text)