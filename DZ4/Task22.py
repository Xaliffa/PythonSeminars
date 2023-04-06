# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

amount_n = int(input("Enter the amount of first set(n): "))
list_n = []
for i in range(amount_n):
    list_n.append(int(input(f"Enter the {i+1} element: ")))
amount_m = int(input("Enter the amount of second set(m): "))
list_m = []
for i in range(amount_m):
    list_m.append(int(input(f"Enter the {i+1} element: ")))
print(sorted(set(list_n).intersection(set(list_m))))

