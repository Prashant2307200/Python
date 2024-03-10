class Animal :
    def __init__(self,species):
        self.species = species
    def _info(self):
        print(f"I'm {self.species}") #private but excess in one inheritance level

class Person(Animal) :
    copaneyName = 'Apple' #class variable const in obj.
    noOfPerson = 0
    def __init__(self,species, name, value):
        super().__init__(species)
        self.name = name     #public
        self._value = value  #instance variable varies in obj.
        self.__bankBalance = 1000 #private name mangling
        Person.noOfPerson += 1
    @property
    def ten_value(self):
        return 10*self._value
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
    @staticmethod
    def add(a, b):
        return a + b
    def info(self):
        super()._info()
        print(f"My name is {self.name} and {self._value} and {self.copaneyName}")

Person1 = Person('Human','John', 10)
Person1.copaneyName = 'Apple ,India' #instance variable
Person.copaneyName = 'Apple ,Electronics'
print(Person.copaneyName) #class variable
# Person1.ten_value = 67
print(Person.add(1,2))
print(Person1.ten_value,Person1._Person__bankBalance)
Person1.info() #Person.info(Person1)
# Person1._show()
print(Person1.__dir__(),dir(Person1),Person1.__class__)
print(Person1.__dict__)
print(help(str) ,help(Person))