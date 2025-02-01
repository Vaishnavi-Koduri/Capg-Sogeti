from abc import ABC
class Father(ABC):
    def displine(self): #Abstract Method
        pass
    def show(self):
        print("Responsible")

class Son(Father):
    def displine(self): #uses the abstract method
        print("He is my son!")

class Daughter(Father):
    def discipline(self):
        print("She is my daughter!")

son= Son()
son.displine()
son.show()
daughter= Daughter()
daughter.discipline()
daughter.show()