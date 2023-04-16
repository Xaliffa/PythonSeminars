# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                     Вывод:
# 7                         3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1            (каждое число вводится с новой строки)


def fill_list(num):
    new_list = []
    for i in range(num):
        new_list.append(int(input(f"Enter the {i+1} element: ")))
    return new_list

num_N = int(input("Enter the N-number: "))
list_N = fill_list(num_N)
num_M = int(input("Enter the M-number: "))
list_M = fill_list(num_M)

result_list = []
for i in list_N:
    if i not in list_M:
        result_list.append(i)
            
print(result_list)
        
