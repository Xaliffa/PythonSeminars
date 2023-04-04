# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


# Моё решение:
# import math 

# sum = int(input("Enter the sum of numbers: "))
# mult = int(input("Enter the multiply of numbers: "))

# print((sum - math.sqrt(sum**2 - 4*mult))/2)
# print((sum + math.sqrt(sum**2 - 4*mult))/2)

# Эталонное решение:
x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)
