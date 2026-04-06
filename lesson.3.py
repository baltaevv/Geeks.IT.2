class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
        self._fined = False
        self.__max_speed = 0

    def _calulate_fuel(self):
        print(f"{self.color}")
        return 1

    def __test(self):
        self.__max_speed = 180
        fined = "yes" if self._fined else "no"

    def drive_to(self, destination):
        if self._calulate_fuel() > 0:
            self.chage_color("green")
            print(f"Car {self.color} driving to {destination}")

    def chage_color(self, new_color):
        self.color = new_color

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, new_speed):
        print(f"new speed in set_max_speed: {new_speed}")
        if new_speed < 0:
            raise ValueError("Error, new seed is negative")
        self.__max_speed = new_speed

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new_speed):
        print(f"new speed in set_max_speed: {new_speed}")
        if new_speed < 0:
            raise ValueError("Error, new speed is negative")
        self.set_max_speed = new_speed

car_1 = Car("silver", 1000)
print(car_1._fined)
car_1._calulate_fuel()
# ca1_1.__test()
# print(car_1._max_speed())
# print(car_1._Car__max_speed) # только для тестирование
print(car_1.get_max_speed())
car_1.__max_seed = 200 # не меняет настоящий атрибут
print(car_1.get_max_speed())
car_1.set_max_speed(200)
print(car_1.get_max_speed())
print(car_1.max_speed)
car_1.max_speed = -150
print(car_1.max_speed)

