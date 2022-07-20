from get_price import get_price
from send_email import send_email
import time
# 柯基
def scaner(tx,name,min_price):
    while True:
        price =get_price(tx)
        print(f"获取中,{name}当前价格为{price}")
        time.sleep(15)
        if price<min_price:
            text=f"{name}当前价格:{price}"
            send_email(text)
if __name__ == '__main__':
    tx = "64c2d95a052cfaebd96bf9ea9c0b011edb70bec95ecbe51d820e799c1af0a4d2"
    scaner(tx,"小柯基",400)