# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

num_N = int(input("Enter the amount (N): "))
num_X = int(input("Enter the desired number X: "))
list_A = [i**2 for i in range(num_N)]              # Для большего разбега чисел
difference = abs(list_A[0] - num_X)
for i in range(1, len(list_A)):
    if abs(list_A[i] - num_X) < difference:
        difference = abs(list_A[i] - num_X)
print(num_N) 
print(*list_A)                                     # Чтобы вывод был по аналогии с примером
print(f'{num_X} \n -> {num_X - difference}') 