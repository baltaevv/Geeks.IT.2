class Car:
    def __init__(self, color, horse_power):
        self.color =color
        self.horse_power = horse_power

    def drive_to(self, destination):
        print(f"{self.color} driving to {destination}")

    def chage_color(self, new_color):
        self.color = new_color

car1 = Car("silver", 1000)
car2 = Car("black", 1000)
print(car1)
print(car1.color< car2.color)
print(type(car1))
car1.drive_to("Karakol")
car1.chage_color("blue")
print(car1.color)

