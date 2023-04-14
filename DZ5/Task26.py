# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power_a_to_b(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    return a * power_a_to_b(a, b - 1)

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print(power_a_to_b(num_1, num_2))