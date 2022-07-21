import json
from json import JSONDecodeError

import requests

def get_price(tx):
    header={
        "user-agent": "Dart/2.14 (dart:io)",
        "accept-language": "zh-CN",
        "accept-encoding": "gzip",
        "content-length": "160",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIxM2YzNmE5N2YwMjUwYmMyZWUxMjhiNTcyYjg1ZmFhNCIsImV4cCI6MTY1ODM5MDQwNCwianRpIjoiMTU0OTk5NzYyMDUxMDkwNDMyMCIsInN1YiI6IjE1NDM4MjI3NTU4MDIzMTI3MDQiLCJzY29wZSI6InVzZXIuYWxsIn0.iCYRkWEeQIuuuM2EWF8z_hGrHJn4ebN6HgdubYZ8BUIVAMp6KRReMY0wWUxaIykbc2_5qrjwNhE_kJVok2SbLQ",
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
        result=re_price.split()[0]
        return eval(result)
    except TypeError:
        return "warning"
    except JSONDecodeError:
        return "warning"
if __name__ == '__main__':

    s=get_price("e318e781bc3119e957640495e507e3235b05a781147ff48400cdeb4a2f2bd6db")
    print(type(s))

