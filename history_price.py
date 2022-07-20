import requests
import json
import time
import pandas as pd
def timetrans(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime
def get_history_price(pages):
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
    data={
        "page": pages,
        "page_size":30,
        "id":"e318e781bc3119e957640495e507e3235b05a781147ff48400cdeb4a2f2bd6db"
    }
    response = requests.session().post("https://api.ddpurse.com/phoenix/public/nft_intl_get_album_tx_history",headers=headers,json=data)
    data_json = json.loads(response.text)["data"]["record"]
    pr_dict={}
    for i in data_json:
        times=timetrans(i["created_time"])
        prices_info = i["option_info"]
        prices = prices_info.split()[0]
        pr_dict[times]=prices

    return pr_dict


if __name__ == '__main__':
    pt_dict={"time":"price"}
    for i in range(500,1200):
        print(f"正在获取{i+1}页")
        pr_dict=get_history_price(i+1)
        print(pr_dict)
        pt_dict.update(pr_dict)
    pt_dict = str(pt_dict).replace("\'", "\"")
    df =pd.read_json(pt_dict,lines=True,encoding='utf-8')
    df.to_excel(f"test2.xlsx")
