import random

from scaner import scaner
import time
import multiprocessing
from send_email import send_email
from get_ui_price import get_ui_price
def run():
    limit_price ={
  '自由勋章': 50.0,
  '幸运勋章': 100.0,
  '相依': 200.0,
  '快乐勋章': 50.9,
  '《小柯基》': 200.0,
  '恒境返利券': 200.0,
  '理性勋章': 50.9,
  '守护勋章': 50.0,
  '团结勋章': 50.9,
  '十二生肖全家福': 7000.0,
  '自律勋章': 50.0,
  '优先券': 100.0,
  '花猫儿 系列1': 1000.0,
  '《润物无声·水中花》': 1000.0,
  '辰龙': 400.0,
  '寅虎': 400.0,
  '子鼠': 400.0,
  '巳蛇': 400.0,
  '丑牛': 400.0,
  '权益值双倍券': 100.0,
  '卯兔': 400.0,
  '消费返现券': 50.0,
  '午马': 500.0,
  '申猴': 600.0,
  '未羊': 600.0,
  '亥猪': 600.0,
  '酉鸡': 600.0,
  '戌狗': 600.0
}
    data=get_ui_price("6267b1f3319840000108ca65","")
    for key,value in data.items():
        print(f"{key}当前价格为：{value}")
        try:
            if value < limit_price[key]:
                send_email(f"{key}当前价格为：{value}")
        except KeyError:
            print("KeyError")
def get_sort_image():
    data=get_ui_price("","recommend")
    data=sorted(data.items(), key=lambda kv: (kv[1], kv[0]))
    msg = ""
    for i in data:
        msg = msg + f"{i[0]}当前价格为：{i[-1]}\n"
    print("邮件发送中")
    send_email(f"{msg}")
def task1():
    while True:
        run()
        time.sleep(random.randint(10,20))
def task2():
    while True:
        get_sort_image()
        time.sleep(3600)
def task3():
    while True:
        data = get_ui_price("6267b1f3319840000108ca65", "")
        msg=""
        for key, value in data.items():
            msg =msg+ f"{key}当前价格为：{value}\n"
        print("邮件发送中")
        send_email(f"{msg}")
        time.sleep(3600)
if __name__ == '__main__':
    copy_process = multiprocessing.Process(target=task1)
    copy_process.start()
    copy_process = multiprocessing.Process(target=task2)
    copy_process.start()
    copy_process = multiprocessing.Process(target=task3)
    copy_process.start()


