lamb_mod = lambda x, y: {x%y}

m = lamb_mod(1, 9)
print(m)


2 map
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))

map
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print (abs_values)

filter
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

out_filter = filter(filter_odd_num, numbers)

print("Отфильтрованный список: ", list(out_filter))

# чистая функция

def fun_clear(data):
    data = data[:]
    if len(data) > 0:
        data[0] += 10
    return data*2
d1 = [1, 2, 3]
d2 = fun_clear(d1)
print(d1)
print(d2)

def fun_2(num):    # Чистая
    return num * 2


list_f = []


def fun_8(num): # Нечистая
    list_f.append(num)

# аналогично min
result = max(4, -5, 23, 5)
print("The maximum number is:", result)

 # 6 • Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции.
def decor(f):
    def wr():
        print('//////////')
        f()
        print('!!!!!!!!!!')
    return wr
@decor
def Pirat():
    print('Arrr')
Pirat()""''
# 10 Написать функцию, которая определяет, является ли год високосным. Пользователь вводит год, если он високосный,
# # то функция возвращает True. Если нет, то False.
def fun_10(year):
    return (year - 1764) % 4 == 0


print(fun_10(1772))