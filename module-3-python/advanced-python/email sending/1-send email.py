# sending email via smtplib(simple mail transport protocol)


import smtplib
from email.mime.text import MIMEText#(multipurpos internet mail extenstion)
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import email


# send email to reciver and sender details

sender_email="padaliyameet558@gmail.com"
reciever_email="brijeshdeveloper36@gmail.com"
app_password="retp tfio ppkk dlts"

# creat a email servies setup for email sending

massage=MIMEMultipart()
massage['From']=sender_email
massage['To']=reciever_email
massage['Subject']="this is a test email from python"


body="hello : /n this is a test email from python smtp library"
massage.attach(MIMEText(body, 'plain'))


#used exception handling to send email and catch error if any
file_path="meet.jpeg"
try:
    #connect email with gmail smtp server
    with open(file_path,'rb') as attachment:
        part=MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        #attach the file with email web format send and read data

        part.add_header('Content-Disposition',f'attachment; filename={file_path}')  

        massage.attach(part)

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,app_password)
    text=massage.as_string()

        # send email to reciver
    server.sendmail(sender_email,reciever_email,massage.as_string())

        # print a success message if email is sent successfully
    print("email sent successfully")


except Exception as e:
    print("failed to send email")


finally:
    server.quit()



        