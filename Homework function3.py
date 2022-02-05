# 1. Написать функцию is_prime, принимающую 1 аргумент
# — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     limit = n ** (1 / 2)
#     i = 2
#     while i <= limit:
#         if n % i == 0:
#             return False
#         i += 1
#     return True
# print(is_prime(int(input("Число: "))))

# Написать функцию square, принимающую 1 аргумент —
# сторону квадрата, и возвращающую 3 значения (с помощью
# кортежа : периметр квадрата, площадь квадрата и диагональ квадрата
#
# def my_box(a):
#    perimeter = a * 4
#    square = a * a
#    diagonal = (2 ** 0.5) * a
#    return a*4, a**2, a * 2**(1/2)
# print(f"Периметр, площадь, диагональ квадрата - {my_box(float(input('Сторона квадрата: ')))}")

# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
# / — разделить (первое на второе). В остальных случаях вернуть строку
# "Неизвестная операция".
#
# x = int(input('Введите первое число : '))
# y = int(input('Введите второе чиcло : '))
# z = input('Введите знак (+, -, *, / ) : ')
# def arithmetic (x, y, z):
# 	if z == "+" :
# 		return (x + y)
# 	elif z == "-":
# 		return (x - y)
# 	elif z == "*":
# 		return (x * y)
# 	elif z == "/":
# 		return (x / y)
# 	else :
# 		return ("Invalid operation")
# print (arithmetic(x, y, z))

# Напишите функцию, которая проверяет, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева
# направо и справа налево.

#
# s = input("Enter a word: ")
# reverse = s[::-1]
#
#
# def palindrom(s):
#     while True:
#         if s[::1] == reverse:
#             print(s, "is palindrome ")
#             break
#         if s != reverse:
#             print(s, "not a palindrome !")
#             break
#
#
# print(palindrom(s))