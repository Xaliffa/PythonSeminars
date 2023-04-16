# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                 Ввод:
# 5                     5
# 1 2 3 4 5             1 5 1 5 1
# Вывод:                Вывод:
# 0                     2
# (каждое число вводится с новой строки)

def fill_list(num):
    new_list = []
    for i in range(num):
        new_list.append(int(input(f"Enter the {i+1} element: ")))
    return new_list

num_N = int(input("Enter the N-number: "))
list_N = fill_list(num_N)

counter = 0
for i in range(1,num_N-1):
    if list_N[i-1] < list_N[i] > list_N[i+1]:
        counter += 1
        
print(f'{list_N} \n {counter}')