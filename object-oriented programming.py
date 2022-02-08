class TheExample:
    st_variable1 = 2
    st_variable2 = 3

    def __init__(self, din_variable1, din_variable2):
        self.din_variable1 = din_variable1
        self.din_variable2 = din_variable2

    def func(self):
        self.first_variable = 5
        print(self.first_variable)

    def func1(self):
        return self.st_variable1 + self.st_variable2

    def func2(self):
        return self.din_variable1**self.din_variable2

example = TheExample(4, 2)
print(example.st_variable1)
print(example.func1())
print(example.func2())
example.func()


