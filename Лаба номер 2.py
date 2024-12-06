# Задача 1
# name = input()
#
#
# def greet(name):
#     a = "Hello" + " " + name
#     return a
#
#
# print(greet(name))
#########################
# number = int(input())
#
#
# def square(number):
#     return number ** 2
#
#
# print(square(number))
##########################
# x = int(input())
# y = int(input())
#
# def max_of_two(x, y):
#     if x > y:
#         print(x)
#     elif x == y:
#         print("Они равны")
#     else:
#         print(y)
#
#
#
# max_of_two(x, y)
##########################
# Задача 2
name = input()
age = int(input())


def describe_person(name, age=30):
    return f'My name is {name} i am {age}'


print(describe_person(name, age))
############################


#
# number = int(input())
#
#
# def is_prime(number):
#     a = 0
#     for i in range(1, number):
#         if number % i == 0:
#             a += 1
#     if a == 1:
#         print("True")
#     else:
#         print("False")
#
# is_prime(number)
