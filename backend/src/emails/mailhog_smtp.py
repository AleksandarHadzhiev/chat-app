import smtplib

from src.emails.base_smtp import BaseSMTP
from src.languages.translations.factory import TranslationsFactory

class SMTPServer(BaseSMTP):
    def __init__(self, language="EN", subject="verification"):
        self.subject=subject
        self.server = smtplib.SMTP("127.0.0.1", 1025)
        self.factory = TranslationsFactory(data={"language": language, "file": "emails"})
        self.translations = self.factory.get_translations().get_translations()
        self.email = "alekshadzhiev01@gmail.com"
        self.server.login("username", "password")

    def send_email(self, data, email):
        from_address = self.email
        to_address = email
        message = f"""\
            Subject: {self.translations[self.subject+"_subject"]}
            
            {self.translations[self.subject+"_body"]}: {data}
            {self.translations["warning"]}
            """
        self.server.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)
        self.server.quit()

