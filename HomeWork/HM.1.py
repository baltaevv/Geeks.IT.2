class Person:
    def __init__(self,name, birth_data, occupation, higher_education):
        self.name = name
        self.birth_data = birth_data
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"меня зовут {self.name}, я родился {self.birth_data}, по профессии{self.occupation}, высшеe образование{self.higher_education},")

person1 = Person("Эламан","15.05.2005","Экономист", True)
person2 = Person("Али","12.08.2002","Програмист", True)
person3 = Person("Курманбек","31.02.2005","Инжинер", False)

person1.introduce()
person2.introduce()
person3.introduce()
