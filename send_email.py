import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
def send_email(text)->str:
    code = "zvjpxmvyuzlwdjjd"
    sender = '2424252675@qq.com'   #发送人邮箱，你自己的邮件如yourname@126.com
    authcode = 'zvjpxmvyuzlwdjjd' #发送人邮箱授权码
    receivers = '2424252675@qq.com' #收件人的邮箱，例如yourfriendname@126.com
    smtpserver ='smtp.qq.com' # 例如smtp.126.com
    smtpport =465 #smtp服务端口，通常为465，可根据邮箱服务的信息进行更改

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receivers

    msg.attach(MIMEText(f'{text}','plain','utf-8'))

    try:
        s = smtplib.SMTP_SSL(smtpserver,smtpport)
        s.login(sender,authcode)
        s.sendmail(sender,receivers,msg.as_string())
    except Exception:
        print("邮件发送出错")
if __name__ == '__main__':
    send_email("kutori")