from email_service import EmailService
from files import FileService
from logging_email import LoggingModule


logger = LoggingModule()

try:
    files = FileService
    email = EmailService()
    email.send_email(files.get_files())
    logger.log_info('Emails were sent successfully')
except Exception as e:
    logger.log_error(f"ERROR: {str(e)}")






    
