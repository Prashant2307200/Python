# constructors are special methods in a class used to create or intialize object of a class
# constructors are auto invoked with creation of class objects and are 3 types
# default ,copy and parameterized
# syntax : def __init__(self):
#              code

class Person :

    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

employee1 = Person('raj','Bussiness Executive')
employee1.info()

employee2 = Person('Divya','HR')
employee2.info()