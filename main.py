from get_price import get_price
from list_get import list_get
from send_email import send_email
import time
tx=""
while True:
    price =get_price(tx)
    time.sleep(0.3)
    if price<50:
        text=f"xxx当前价格:{price}"
        send_email(text)
