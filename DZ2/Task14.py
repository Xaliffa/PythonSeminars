# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input("Enter the number N: "))
power = 0
while 2 ** power <= N:
    print(2 ** power)
    power += 1
