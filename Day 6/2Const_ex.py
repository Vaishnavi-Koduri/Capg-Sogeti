class Example:
    def __init__(self,name):
        print(f"My name is my: {name}")

    def __init__(self,age):
        print(f"This is my age: {age}") #when there are two constructors , only the 2nd one gets executed
    
obj= Example(47)

