class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


doggy = Dog("Шарик", 3)
kitty = Cat("Мурка", 1)

print(f"{doggy.get_name()} говорит: {doggy.make_sound()}")
print(f"{kitty.get_name()} говорит: {kitty.make_sound()}")

kitty.set_age(2)

print(f"Новый возраст кошки: {kitty.get_age()}")