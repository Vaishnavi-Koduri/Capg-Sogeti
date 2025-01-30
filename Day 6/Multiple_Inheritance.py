# parent class 1
class man:
    def quality1(self):
        return "Men are CRUEL!! "

# parent class 2
class woman:
    def quality2(self):
        return "Women are ADORABLE!! "

# child class
class human(man,woman):
    pass #combines both the classes(man and woman)
    def dance(self):
        return "They can dance well"

Human= human()
print(Human.quality1()) #Inherited from quality1
print(Human.quality2()) #Inherited from quality2
print(Human.dance()) 
x= woman()
x=Human
print(x.dance())