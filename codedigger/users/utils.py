#from codedigger.settings import EMAIL_HOST_USER
from django.core.mail import send_mail	
from dotenv import load_dotenv
load_dotenv()
import os

class Util:
    @staticmethod
    def send_email(data):
        send_mail(data['email_subject'],data['email_body'],os.getenv('EMAIL_HOST_USER'),[data['to_email']])