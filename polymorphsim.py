class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Tweet!")

# Demonstrating polymorphism
def play_sound(animal):
    animal.make_sound()

# List of different animals
animals = [Dog(), Cat(), Bird()]

for creature in animals:
    play_sound(creature)
