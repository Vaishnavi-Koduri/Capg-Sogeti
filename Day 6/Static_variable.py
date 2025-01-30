class Cat:
    meow= "Meowww"
    @staticmethod
    def sound1():
        print(Cat.meow)

class Dog:
    bark="Barkkk"
    @staticmethod
    def sound2():
        print(Dog.bark)
animal= Cat()
animal1= Dog()
animal.sound1()
animal1.sound2()