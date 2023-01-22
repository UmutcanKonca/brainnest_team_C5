from email_sender import EmailSender

import requests
from email.mime.base import MIMEBase
from email import encoders
import os


path = "./files"
files = os.listdir(path)
new_file = None
for file in files:
    with open(os.path.join(path,file), 'rb') as attachment:
        # read binary
        our_file = MIMEBase('application',f'{file.split(".")[1]}', Name=file)
        our_file.set_payload(attachment.read())
        encoders.encode_base64(our_file)
    new_file=our_file


if __name__ == "__main__":
    response = requests.get(url='https://api.npoint.io/de5c3533349a7f588f4d')
    email_data = response.json()
    email = EmailSender(email_data)
    email.send_email(new_file)
