import json

import requests

def get_ui_price(hash_value,type_value):
    headers={
        "user-agent": "Dart/2.14 (dart:io)",
        "accept-language": "zh-CN",
        # "client-id": "13f36a97f0250bc2ee128b572b85faa4",
        "accept-encoding": "gzip",
        "content-length": "160",
        # "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIxM2YzNmE5N2YwMjUwYmMyZWUxMjhiNTcyYjg1ZmFhNCIsImV4cCI6MTY1NzM4MzQ1MCwianRpIjoiMTU0NTc3NDE0NTUzNDMxNjU0NCIsInN1YiI6IjE1MjE4MTAzMzc4MjcxODg3MzYiLCJzY29wZSI6InVzZXIuYWxsIn0.qe_TpPrRZseXrdcI3-GYSw5vng5mOP1_bDhAyK_nKnlnoMsXF2zrw7bK3GVOx5NaEgtb0h9IFyw-vtGxQL4NFw",
        # "device-id": "f60da01dbf77ad5e",
        "host": "api.ddpurse.com",
        "content-type": "application/json; charset\u003dutf-8",
        "app-version": "1.8.0"
    }

    body={
        "page":1,
        "page_size":1000,
        "filter":{"status":"on-shelf","keyword":"","type":f"{type_value}","category_id":f"{hash_value}","user_id":"","without_user_index":False}
    }

    response = requests.post("https://api.ddpurse.com/phoenix/public/nft_intl_get_work_group_list",json=body)
    data=json.loads(response.text)
    re_dict={}
    for i in data["data"]["items"] :
        # print(i["nft_info"]["name"],i["nft_info"]["fiat_price_range"])
        re_dict[i["nft_info"]["name"]]=eval((i["nft_info"]["fiat_price_range"]).split()[0])*6.76
        # re_dict[i["nft_info"]["name"]]=i["nft_info"]["fiat_price_range"]
    return re_dict
if __name__ == '__main__':
    print(get_ui_price("","recommend"))