class Animal:
    def __init__(self, fname, lname, age, n_legs): # constructor, called when instantiating class
        self.fname = fname
        self.lname = lname
        self.age = age
        self.n_legs = n_legs

    @property # getter aka accessor
    def name(self):
        return f"{self.fname} {self.lname}" # string concatenation

    @name.setter # setter aka mutator
    def name(self, nm):
        nm = nm.split(" ") # split string using " "
        self.fname = nm[0]
        self.lname = nm[1]

class Fish(Animal): # inherit from Animal class
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age, 0) # pass values to parent class

class LandAnimal(Animal): # inherit from Animal class
    def __init__(self, fname, lname, age, n_legs):
        super().__init__(fname, lname, age, n_legs) # pass values to parent class

    def talk(self): # create an `abstract` method that is implemented differently by the child classes
        raise NotImplementedError # raise error if one attempts to call this function when it hasn't been implemented yet

class Human(LandAnimal):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age, 2) # pass values to parent class

    def talk(self): # override parent method
        print(f"{self.name} says hello!")

class Dog(LandAnimal):
    def __init__(self, fname, lname, age, breed):
        super().__init__(fname, lname, age, 4) # pass values to parent class
        self.breed = breed

    def talk(self): # override LandAnimal method
        print(f"{self.name} says woof!")

class Crazy(Human, Dog): # multiple inheritance to demonstrate the diamond inheritance problem
    def __init__(self, fname, lname, age, breed):
        super().__init__(fname, lname, age) # python resolves the method by order of classes (Method Resolution Order)
        self.breed = breed

human = Human("Alchemy", "Altair", 17) # instantiate class
print(human.name) # call getter
human.name = "Altair Alchemy" # pass values to name's setter
print(human.name)
human.talk()

c = Crazy("A", "B", 1, "Chihuahua")
c.talk()