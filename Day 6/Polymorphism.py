class Popcorn:
    def Flavour(self):
        print("Cheeseee")

class Drink:
    def Flavour(self):
        print("Minttt")
    
for flavour in [Popcorn(),Drink()]:
    flavour.Flavour()