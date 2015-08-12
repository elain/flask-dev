from flask import Flask
from flask.ext.mail import Message, Mail


app = Flask(__name__)

app.config.update(dict(
#    DEBUG = True,
    MAIL_SERVER = 'smtp.sina.com.cn',
    MAIL_PORT = 25,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'aaaaaa',
    MAIL_PASSWORD = 'bbbbbb',
))

mail = Mail(app)
msg = Message("Hello",sender="aaaaaa@sina.com",recipients=["xxxxxx@qq.com"])

msg.body = "this is a test"
msg.html = "<b>okokok</b>"
with app.app_context():
    mail.send(msg)
