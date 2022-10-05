import requests
import json

base_url = 'https://gold-pos.vvs.vn/parse/classes/PrintJob/D9UrWx2m0H'

headers = {
    "X-Parse-Application-Id":"SCWASRTWK1Y9AVMP1KFC"
}
with requests.Session() as s:
    res = s.delete(base_url,headers=headers)
    print(res.json())