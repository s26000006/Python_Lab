class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

class Teacher(Person):
    def __init__(self, age, name,subject):
        super().__init__(age, name)
        self.subject=subject

    def display_info(self):
        print(f" Name:{self.name}, \n  Age:{self.age}, \n Subject:{self.subject}")

    def check_retirement(self):
        if self.age>60:
            print("Eligible for retirement")
        else:
            print("Not eligible for retirement")

t1=Teacher(50,'Kasun','Maths')
t1.display_info()
t1.check_retirement()