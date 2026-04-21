from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def test(self):
        print("test in Animal")

class Dog(Animal):
    def make_sound(self):
        print("Гаав")

class Cat(Animal):
    ...

puppy = Dog()
print(puppy)
