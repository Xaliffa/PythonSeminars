# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Моё решение: 

# num_amount = int(input("Enter the amount: "))
# my_list = []
# max = 0
# for i in range(num_amount):
#     i = int(input(f"Enter the {i+1} number: "))
#     my_list.append(i)
#     if i > max:
#         max = i
#     if i == 0:
#         break
# print(max)


# Через моржовый оператор:

max_num = 0
while(i := int(input()))!=0:
    if i > max_num:
        max_num = i
print(max_num)
    
    