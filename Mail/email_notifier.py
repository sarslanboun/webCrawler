import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotifier:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body, attachment_path=None):
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        message.attach(MIMEText(body, "plain"))

        if attachment_path:
            attachment = open(attachment_path, "rb")
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment_path}",
            )
            message.attach(part)
        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(self.sender_email, self.sender_password)
            smtpserver.sendmail(self.sender_email, receiver_email, message.as_string())
            print("mail gitti")
        except smtplib.SMTPException as e:
            print(e)
        finally:
            smtpserver.quit()


