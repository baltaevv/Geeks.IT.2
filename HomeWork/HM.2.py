class Person:
    def __init__(self, name, birth_date, job):
        self.name = name
        self.age = birth_date
        self.job = job

    def introduce(self):
        print(f"Привет меня зовут  {self.name}, я родился {self.age}, работаю {self.job}")

class Classmate(Person):
    def __init__(self, name, birth_date, job, groub_name):
        super().__init__(name, birth_date, job)
        self.groub_name = groub_name

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я одноклассник Байэля из {self.groub_name}, я родился {self.age}, работаю {self.job}")

class Friend(Person):
    def __init__(self, name, birth_date, job, hobby):
        super().__init__(name, birth_date, job)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет меня зовут {self.name} я друг Байэля, я увилекаюсь {self.hobby}, я родился {self.age}, работаю {self.job}")

c1 = Classmate("Байсал","12.08.2000","Программистом", "IT.23")
c2 = Classmate("Айсенем", "10.03.2001", "дизайнером", "Design-2")

f1 = Friend("Алтын","23.04.2002","Актёром","Рисованием")
f2 = Friend("Нурик", "12.07.1999", "поваром", "игроми")

c1.introduce()
c2.introduce()
f1.introduce()
f2.introduce()
