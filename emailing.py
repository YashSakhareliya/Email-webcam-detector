import smtplib
import os
import imghdr
from email.message import EmailMessage

PASSWORD = os.environ["PASSWORD"]
SENDER = "sakhareliyayash03@gmail.com"
RECEIVER = "sakhareliyayash03@gmail.com"


def send_mail(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = "New customer showed up!"
    email_message.set_content("Hey, We just show new customer!")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_mail(image_path="images/10.png")
