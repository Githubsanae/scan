import json
import requests

def get_price(tx):
    header={
        "user-agent": "Dart/2.14 (dart:io)",
        "accept-language": "zh-CN",
        "accept-encoding": "gzip",
        "content-length": "160",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIxM2YzNmE5N2YwMjUwYmMyZWUxMjhiNTcyYjg1ZmFhNCIsImV4cCI6MTY1NzU1NjQ4MywianRpIjoiMTU0NjQ5OTkwMTk1MzI4NjE0NCIsInN1YiI6IjE1NDM4MjI3NTU4MDIzMTI3MDQiLCJzY29wZSI6InVzZXIuYWxsIn0.yT6s-TY_REnrf8b-Wl7yJYjCjLEIAMjAfQcttw0KkvnfJgFex__e71UlSv4PLgC3WXwtBuD2yM7bzlbuDaIQSw",
        "host": "api.ddpurse.com",
        "content-type": "application/json; charset\u003dutf-8",
    }
    json_data={
            "page":1,
          "page_size":1,
          "id":f"{tx}",
          "sort":"price",
          "only_on_shelf":True,
          "user_index":1656911262664
    }
    try:
        con=requests.get("https://api.ddpurse.com/phoenix/user_nft/nft_intl_get_album_list",headers=header,json=json_data)
        con=con.text
        con=json.loads(con)
        re_price=con["data"]["items"][0]["money_label"]
        return re_price
    except TypeError:
        return 0
if __name__ == '__main__':

    s=get_price("e318e781bc3119e957640495e507e3235b05a781147ff48400cdeb4a2f2bd6db")
    print(s)

