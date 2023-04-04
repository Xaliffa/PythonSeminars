# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

coins_number = int(input("Enter the number of coins: "))
side_0_num = 0
side_1_num = 0

for i in range(coins_number):
    side = int(input("Enter 1 or 0: "))
    if side == 0:
        side_0_num+=1
    else:
        side_1_num+=1
if side_0_num < side_1_num:
    print(f"Coins to turn: {side_0_num}")
else:
    print(f"Coins to turn: {side_1_num}")

