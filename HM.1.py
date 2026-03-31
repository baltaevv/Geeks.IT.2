class Person:
    def __init__(self,name, birth_data, occupation, higher_education):
        self.name = name
        self.birth_data = birth_data
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"меня зовут {self.name}, я родился {self.birth_data}, по профессии{self.occupation}, высшеe образование{self.higher_education},")

Person1 = Person("Эламан","15.05.2005","Экономист", True)
Person2 = Person("Али","12.08.2002","Програмист", True)
Person3 = Person("Курманбек","31.02.2005","Инжинер", False)

Person1.introduce()
Person2.introduce()
Person3.introduce()
