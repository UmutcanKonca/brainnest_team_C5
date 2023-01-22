# Noor
import os
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class FileService: 

    def getFiles() -> list[MIMEBase]:
        path = "./files"
        files = os.listdir(path)
        attachments : list[MIMEBase] =[]

        for file in files:
            with open(os.path.join(path,file), 'rb') as attachment:
                # read binary
                our_file = MIMEBase('application',f'{file.split(".")[1]}', Name=file)
                our_file.set_payload(attachment.read())
                encoders.encode_base64(our_file)
                attachments.append(our_file)
        return attachments