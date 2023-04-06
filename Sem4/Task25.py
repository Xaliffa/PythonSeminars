# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Моё решение:
# my_list = 'g h l m slu p r l r g g l m slu'.split()
# print(my_list)
# for i in range (len(my_list)-1):
#     count = 1
#     for j in range (i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             my_list[j] = my_list[i] + f'_{count}'
#             count += 1
# print(' '.join(my_list))


# Можно использовать словарь (как счетчик):
s = ('a h k a a h l k l l a').split()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end = ' ')
    elif i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end = ' ')
        