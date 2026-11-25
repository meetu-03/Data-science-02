import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = "padaliyameet558@gmail.com"
receiver_email = "padaliyameet558@gmail.com"
app_password = "retp tfio ppkk dlts"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "This is a test email from Python"

body = "Hello,\nThis is a test email from Python SMTP library."
message.attach(MIMEText(body, 'plain'))

file_path = "meet.jpeg"

server = None

try:
    # Attach file
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            'Content-Disposition',
            f'attachment; filename={file_path}'
        )

        message.attach(part)

    # Connect to Gmail SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Send email
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )

    print("Email sent successfully")

except Exception as e:
    print("Failed to send email:", e)

finally:
    if server is not None:
        server.quit()