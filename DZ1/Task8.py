# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter the n-size: '))
m = int(input('Enter the m-size: '))
k = int(input('Enter the piece-size: '))

remainder_n = n*m
remainder_m = n*m

if k <= n*m and (k >= n or k >= m):
    while remainder_n > 0 or remainder_m > 0:
        if remainder_n % k == 0 or remainder_m % k == 0:
            print('Yes')
            break
        remainder_n -= n
        remainder_m -= m
else:
    print('No')
