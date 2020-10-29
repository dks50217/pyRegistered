from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

class Ctr_Email():
    def __init__(self,objParamEmail):
        self.objParamEmail = objParamEmail
    def sendMail(self):
        content = MIMEMultipart()
        content["subject"] = self.objParamEmail.mail_subject
        content["from"] = self.objParamEmail.mail_from
        content["to"] = self.objParamEmail.mail_to
        content.attach(MIMEText(self.objParamEmail.mail_text))
        content.attach(MIMEImage(Path(self.objParamEmail.mail_image).read_bytes()))

        with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.objParamEmail.mail_from,self.objParamEmail.mail_key)
                smtp.send_message(content)
                print("Complete!")
            except Exception as e:
                print("Error message: ", e)
        

