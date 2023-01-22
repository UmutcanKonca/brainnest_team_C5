from email_sender import EmailSender
from files import FileService


files = FileService
email = EmailSender()
email.send_email(files.get_files())


    
