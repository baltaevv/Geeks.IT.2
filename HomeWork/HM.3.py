class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. У меня {edu}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, grade):
        super().__init__(name, birth_date, occupation, higher_education)
        self.grade = grade

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учусь в {self.grade}. У меня {edu}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Моё хобби {self.hobby}. У меня {edu}.")

cl1 = Classmate("Иван", "20.02.2000", "студент", True, "1-курс")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()