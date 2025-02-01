#An interface must contain the same abstrat method else it will throw an error

from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod 
    def flavor(self):
        pass
    @abstractmethod 
    def color(self):
        pass

class Juice(Fruit):
    def flavor(self):
        print("Blueberry")
    def color(self):
        print("Blue")

class Salad(Fruit):
    # pass
    def flavor(self):
        print("Mango")
    def color(self):
        print("Yellow")

juice= Juice()
juice.flavor()
juice.color()
salad= Salad()
salad.flavor()
salad.color()