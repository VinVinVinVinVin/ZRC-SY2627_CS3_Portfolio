# This code demonstrates method overriding in Python using a simple animal hierarchy. Enjoy!

class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound."

    def eat(self):
        return f"{self.name} eats food."


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!"

    def eat(self):
        return f"{self.name} eats fresh meat."


class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"

    def eat(self):
        return f"{self.name} eats grass and fruits."


class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"

    def eat(self):
        return f"{self.name} eats bananas."


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print("-----") # extra space for better readability