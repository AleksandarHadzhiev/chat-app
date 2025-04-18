import smtplib

from src.emails.base_smtp import BaseSMTP


class SMTPServer(BaseSMTP):
    def __init__(self):
        self.server = smtplib.SMTP("127.0.0.1", 1025)
        self.email = "alekshadzhiev01@gmail.com"
        self.server.login("username", "password")

    def send_email(self, code, email):
        from_address = self.email
        to_address = email
        message = f"""\
            Subject: Verification Code
            
            Thank you for registering. This is your verification code: {code}
            """
        self.server.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)
        self.server.quit()
