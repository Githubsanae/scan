import requests
import json
headers={
    'POST /phoenix/user_nft/nft_intl_buy_order HTTP/1.1'
    "user-agent": "Dart/2.14 (dart:io)",
    "accept-language": "zh-CN",
    "client-id": "13f36a97f0250bc2ee128b572b85faa4",
    "accept-encoding": "gzip",
    "content-length": "78",
    "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIxM2YzNmE5N2YwMjUwYmMyZWUxMjhiNTcyYjg1ZmFhNCIsImV4cCI6MTY1Nzg4MDM1MiwianRpIjoiMTU0Nzg1ODMwNDM1OTU1NTA3MiIsInN1YiI6IjE1NDM4MjI3NTU4MDIzMTI3MDQiLCJzY29wZSI6InVzZXIuYWxsIn0.7E_hUaPvjsx-OANwE6POrGtKo0E3WXP9_kkKwAQLId-Tp_aQY1gm3thJQO2rqzL50ICxfv5Ru3WrJerz_cZ5ZA",
    "device_id" :"f40597048a7ee04f",
    "host": "api.ddpurse.com",
    "content-type": "application/json; charset\u003dutf-8",
    "app-version": "1.7.5"
}
json_data={
   "order_id":730706666244747264,
    "user_index":1656911004467,
    # "ignore_fee":True
    "payment_method": 1
}
json_data = json.dumps(json_data)
print(json_data)
content = requests.session().post("https://api.ddpurse.com/phoenix/user_nft/nft_intl_buy_order",headers=headers,json=json_data)
print(content.text)