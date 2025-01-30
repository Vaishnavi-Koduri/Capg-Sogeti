class Destructor:
    def __init__(self,name):
        self.name= name
        print(f"The object {self.name} is created")

    def __del__(self):
        print(f"The object {self.name} is destroyed")

object= Destructor("Sample")
del object