count_wm = int(input('--> '))
min_wm = int(input('wm--> ')) #чтобы взять реальное минимальное значение, т.к. вес не мб меньше нуля
max_wm = min_wm

min_wm_i = 0
max_wm_i = 0
for i in range(1, count_wm): # с 1-го, т.к. 0-й уже спросили
    wm = int(input('wm--> '))
    if wm > max_wm:
        max_wm = wm
        max_wm_i = i
    if wm < min_wm:
        min_wm = wm
        min_wm_i = i
        
print(f'max = {max_wm}, max_ind = {max_wm_i}, min = {min_wm}, min_ind = {min_wm_i}')