import pandas as pd
import numpy as np
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import socket
# import time

MY_ADDRESS='nanfeizhenkuangou@163.com'
PASSWORD='xx'

data=pd.read_excel('Grades.xlsx')
length=data.shape[0]
message_template=Template('Hi $name,\n\n Your final exam score is $final points. The average score is 92.09 points and the median score is 88.20 points.\n\nRegards,\nInstructors')

s = smtplib.SMTP(host='smtp.163.com', port=25)
s.ehlo()
#s.starttls()
s.login(MY_ADDRESS,PASSWORD)

for i in range(length):
    data_i=dict(data.loc[i])

    msg = MIMEMultipart()       # create a message # 可带附件

    message = message_template.substitute(data_i)
    # print(data_i)

    msg['From']=MY_ADDRESS
    msg['To']=data_i['email']
    msg['Subject']="CS211: Final exam score"
    msg.attach(MIMEText(message, 'plain'))

    #附件
    att1=MIMEText(open(data_i['attach']+'.pdf','rb').read(),'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename='+data_i['attach']+'.pdf'
    msg.attach(att1)

    while True:
        time.sleep(2)
        try:
            s.send_message(msg)
            print("SENT EMAIL TO ", data_i['name']," sucessfully!")
            del msg
            break
        except:
            print("Fail to SENT EMAIL TO ", data_i['name'], ". Retry...")
            
s.quit()