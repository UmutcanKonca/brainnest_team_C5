import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os
import requests
from datetime import date
import logging
from files import FileService

import schedule
import time


today = date.today().strftime("%d %B %Y")
logging.basicConfig(filename='email.log',level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                   )

class EmailSender:
    def __init__(self,email_data):
        self.emails =[email for index, email in enumerate(email_data['emails'])] 
        self.subject = email_data['subject']
        self.content = email_data['content']
        self.sender_email = email_data['sender_email']['email']
        self.sender_password = email_data['sender_email']['password']
        

    def send_email(self):
        file_service = FileService
        
        try:
            with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
                subject = self.subject.replace('[DATE]',today)
            
                connection.starttls()
                connection.login(user=self.sender_email,password=self.sender_password)
                
                
                for email in self.emails:
                    attachments = file_service.getFiles()
                    message = MIMEMultipart()
                    message['From'] = self.sender_email
                    message['To'] = email
                    message['Subject'] = subject

                    message_content = f'{self.content.replace("[NAME]",email_data["emails"][email]["name"].title()).replace("[DATE]",today)}'
                    message.attach(MIMEText(message_content))     
                    for attachment in attachments:
                         message.attach(attachment)
                    connection.sendmail(from_addr=self.sender_email, to_addrs=email, msg=message.as_string())
            logging.info('Emails were sent successfully')
        except Exception as e:
	        logging.info("ERROR : "+str(e))


if __name__ == "__main__":
    response = requests.get(url='https://api.npoint.io/de5c3533349a7f588f4d')
    email_data = response.json()

    email = EmailSender(email_data)
    schedule.every().day.at("16:06").do(email.send_email)

    schedule.run_all()
    time.sleep(10)
    schedule.clear()

