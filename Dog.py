#creating the dog class
class Dog:
    #atribute of every object in this class
    species = "Canis Familiaries"
    def __init__(self, name, age):
        #each object in the class should have these specified
        self.name = name
        self.age = age
#creating an object of the class
carlos = Dog("Carlos", 3)
palito = Dog("Palito", 4)
#acess the instance info with (object.info)
print(carlos.name)
