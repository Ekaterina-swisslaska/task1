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


class TheExample:
    def __init__(self):
        self.func4()

    def func(self):
        return self.a + self.b
    def func1(self):
        return self.a - self.b
    def func2(self):
        return self.a * self.b
    def func3(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b
    def func4(self):
        self.a = int(input())
        self.b = int(input())
while True:
    print("+,-,*,/")
    x = input()
    print("Number: ")
    example = TheExample()
    if x == "6":
        break
    if x == "+":
        print(example.func())
    if x == "-":
        print(example.func1())
    if x == "*":
        print(example.func2())
    if x == "/":
        print(example.func3())

