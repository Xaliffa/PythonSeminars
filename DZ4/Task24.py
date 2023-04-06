# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

bushes_num = int(input("Enter the number of bushes: "))
berries_list = []
for i in range(bushes_num):
    berries_list.append(int(input(f"Enter the number of berries on {i+1} bush: ")))
print(berries_list)
berries_list.append(berries_list[0])
max_harvest = 0
current_harvest = berries_list[0] + berries_list[-1] + berries_list[1]
for i in range(1, len(berries_list)-1):
    current_harvest = berries_list[i] + berries_list[i+1] + berries_list[i-1]
    if current_harvest > max_harvest:
        max_harvest = current_harvest
print(max_harvest)
