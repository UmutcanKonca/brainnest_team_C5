import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date


class EmailSender:
    def __init__(self,email_data):
        self.email_data = email_data
        self.emails = [email for index, email in enumerate(email_data['emails'])] 
        self.subject = email_data['subject']
        self.content = email_data['content']
        self.sender_email = email_data['sender_email']['email']
        self.sender_password = email_data['sender_email']['password']
        self.today = date.today().strftime("%d %B %Y")
        

    def send_email(self,files):
            with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
                subject = self.subject.replace('[DATE]',self.today)
                connection.starttls()
                connection.login(user=self.sender_email,password=self.sender_password)
                
                for email in self.emails:
                    message = MIMEMultipart()
                    message['From'] = self.sender_email
                    message['To'] = email
                    message['Subject'] = subject

                    message_content = f'{self.content.replace("[NAME]",self.email_data["emails"][email]["name"].title()).replace("[DATE]",self.today)}'
                    message.attach(MIMEText(message_content))     
                    message.attach(files)
                    connection.sendmail(from_addr=self.sender_email, to_addrs=email, msg=message.as_string())

