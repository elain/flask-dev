from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, datetime


msg = MIMEMultipart()

msg['to'] = 'xxxxxx@qq.com'
msg['from'] = 'aaaaaa@sina.com'
msg['subject'] = Header('test mail (' + str(datetime.date.today()) + ')','gb2312')

server = smtplib.SMTP('smtp.sina.com.cn')
server.login('aaaaaaa','bbbbbb')
error=server.sendmail(msg['from'], msg['to'], msg.as_string())
server.close()
print(error)

