class Person :
    name = 'Harry'
    occupation = 'Developer'
    networth = 10
    def info(self):
        print(f"{self.name} is {self.occupation} and networth is {self.networth}")

a = Person()
print(a.name ,a.occupation)
a.info()

b = Person()
b.name = 'Shubham'
b.occupation = 'UI/UX'
b.info()

c = Person()
c.name = 'Nikita'
c.occupation = 'HR'
c.info()