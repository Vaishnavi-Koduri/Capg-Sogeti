class Example1:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hey {args[0]}")
        elif len(args)==2:
            print(f"Hey {args[0]}, you are {args[1]} years old ")

class Example2:
    def __init__(self,**kwargs):
        # self.student_name= student_name 
        if "name" in kwargs and "age" in kwargs:
            print(f"Hey {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hey {kwargs}['name']")
        self.xfield= kwargs['name']
       
obj= Example1("Rohan", 100)
obj2= Example2(name= "Vaish",age= 21) 