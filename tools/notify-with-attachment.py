import os
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sys = platform.system()
sender = os.environ['EMAIL_ADDRESS']
receivers = ['ywsong@aceinna.com']

message = MIMEMultipart()
#message['From'] = Header("notifications@aceinna.com", 'utf-8')
#message['To'] = "ywsong"
subject = 'CI Executable'
message['Subject'] = Header(subject, 'utf-8')

message.attach(
    MIMEText('Built executable on {0}'.format(sys), 'plain', 'utf-8'))


file_name = 'ans-devices.exe' if sys == "Windows" else 'ans-devices'

att1 = MIMEText(open(os.path.join(os.getcwd(), 'dist', file_name),
                     'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP('smtp.office365.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender, os.environ['EMAIL_PASSWORD'])
    smtpObj.sendmail(sender, receivers, message.as_string())
except smtplib.SMTPException as error:
    print(error)
