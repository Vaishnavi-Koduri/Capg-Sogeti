from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass
    
class Email(Mail):
    @abstractmethod
    def send(self):
        print("The Email has been sent!! ")

class SMS(Mail):
    @abstractmethod
    def send(self):
        print("The SMS has been sent!! ")

class Whatsapp(Mail):
    @abstractmethod
    def send(self):
        print("The Whatsapp message has been sent!! ")

mail= Mail()
email= Email()
sms= SMS()
whatsapp= Whatsapp()
mail.send()
email.send()
sms.send()
whatsapp.send()