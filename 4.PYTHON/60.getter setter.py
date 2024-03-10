class myClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self,value):
        self._value = value/10

a = myClass(5)
a.ten_value = 67
print(a.ten_value)
a.show()