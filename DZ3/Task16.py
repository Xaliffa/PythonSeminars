# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

num_N = int(input("Enter the amount (N): "))
num_X = int(input("Enter the desired number X: "))
counter = 0
list_A = []
for i in range(num_N):
    i = int(input(f"Enter the {i+1} element: "))
    list_A.append(i)
    if i == num_X:
        counter += 1
print(num_N) 
print(*list_A)                                # Чтобы вывод был такой же, как в примере
print(f'{num_X} \n -> {counter}') 
