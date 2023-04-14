# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def sum(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return sum(a + 1, b - 1)

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print(sum(num_1, num_2))