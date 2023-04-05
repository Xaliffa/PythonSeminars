# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]

# вариант 1
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
k = 12 % len(my_list) 
my_list = my_list[-k:] + my_list[:-k]
print(my_list)


# вариант2
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 10 % len(my_list)
# for i in range(k):
#     num = my_list.pop(-1)
#     my_list.insert(0, num)
# print(my_list)
    