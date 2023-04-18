# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithm_progression(start_elem, step, amount_elems):
    ar_progression = []
    for i in range(1, amount_elems + 1):
        ar_progression.append(start_elem + (i - 1) * step)
    return ar_progression

print(arithm_progression(7, 2, 5))