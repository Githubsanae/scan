import json
import time

import pymysql
import requests
from pymysql import ProgrammingError, OperationalError


class TimeJudge:
    def __init__(self,judge_time,rate):
        self.judge_time=judge_time
        self.rate=rate

def exchange_rate_query():
    rates=requests.get('https://webapi.huilv.cc/api/exchange?num=100&chiyouhuobi=USD&duihuanhuobi=CNY&type=0&_=1659019742112').json()['dangqianhuilv']
    return rates
def commit_data(db,cursor,sql,nft_info,time_obj):
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except ProgrammingError as Argument:
        # 如果发生错误则回滚
        print(f"ProgrammingError:{Argument}")
        db.rollback()
    except OperationalError as Argument:
        # 如果发生错误则回滚
        print(f"OperationalError:{Argument}")
        if '1054, "Unknown column' in str(Argument):
            print('开始修复')
            add_columns(db,cursor,nft_info)
            time.sleep(0.5)
            add_time_price(time_obj)
            return
        db.rollback()
def list_create(tup):
    list_temp=[]
    for i in tup:
        list_temp.append(i[0])
    return list_temp
def con_db():
    db = pymysql.connect(host='23.94.123.133',
                         user='root',
                         port=3306,
                         password='wml99999',
                         database='kutori')
    cursor = db.cursor()
    return db,cursor
def repeated_query(judge,db, cursor):

    check="SHOW COLUMNS FROM activities;"
    cursor.execute(check)
    results = cursor.fetchall()
    lists=list_create(results)
    if judge in lists:
        return True
    else:
        return False
def add_columns(db,cursor,nft_info):
    for key in nft_info.keys():
        add_db(key.replace(" ","").replace("\\",""),db, cursor)
        print(key.replace(" ",""))
def add_db(name,db, cursor):
    if not repeated_query(name,db, cursor) :
        sql=f" ALTER TABLE activities ADD `{name}` double"
        cursor.execute(sql)
def sql_create(time_obj):
    system_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+8*3600))
    nft_info=get_ui_price("6267b1f3319840000108ca65","",time_obj)
    name=str(list(nft_info.keys())).replace('\'',"`").replace('[','').replace(']','').replace(' ','').replace("\\","")
    price=str(list(nft_info.values())).replace('\'',"").replace('[','').replace(']','').replace(' ','')
    sql = f"INSERT INTO activities(时间,{name}) value ('{system_time}',{price})"
    return sql,nft_info
def add_time_price(time_obj):
    db, cursor = con_db()
    sql,nft_info=sql_create(time_obj)
    commit_data(db,cursor,sql,nft_info,time_obj)
    db.close()

def get_ui_price(hash_value,type_value,time_obj):
    body={
        "page":1,
        "page_size":1200,
        "filter":{"status":"on-shelf","keyword":"","type":f"{type_value}","category_id":f"{hash_value}","user_id":"","without_user_index":False}
    }

    response = requests.post("https://api.ddpurse.com/phoenix/public/nft_intl_get_work_group_list",json=body)
    data=json.loads(response.text)
    re_dict={}
    # 获取汇率
    now_time=time.time()
    if (time_obj.judge_time+3600)<now_time:
        print('重写')
        time_obj.rate=exchange_rate_query()
        time_obj.judge_time=time.time()
    for i in data["data"]["items"] :
        # print(i["nft_info"]["name"],i["nft_info"]["fiat_price_range"])
        re_dict[i["nft_info"]["name"]]=round(eval((i["nft_info"]["fiat_price_range"]).split()[0])*eval(time_obj.rate),2)
        # re_dict[i["nft_info"]["name"]]=i["nft_info"]["fiat_price_range"]
    return re_dict
def run():
    print('开始运行')
    judge_time=time.time()
    rates=exchange_rate_query()
    time_obj=TimeJudge(judge_time,rates)
    while True:
        try:
            add_time_price(time_obj)
            print('获取中')
            time.sleep(20)
        except:
            run()
if __name__ == '__main__':
    run()
    # print()
    # add_columns(nft_info)
    # print(get_ui_price("","recommend"))
    # print(add_db('1'))