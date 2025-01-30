class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f"This car  is a {self.brand} {self.model}")

car1= Car("Skoda","Corolla")
car2= Car("Toyota","Honda")
car1.display()
car2.display()