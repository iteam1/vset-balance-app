import requests
import json

base_url = 'https://vset.vvs.vn/parse/classes/PrintJob'

headers = {
    "X-Parse-Application-Id":"SCWASRTWK1Y9AVMP1KFC",
}

with requests.Session() as s:
    res = s.get(base_url,headers=headers)
    print(res.json())