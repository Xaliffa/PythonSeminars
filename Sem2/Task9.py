# n = int(input('Enter the number n: '))
# i = 1
# factorial = 1
# while i<=n:
#     factorial=factorial*i
#     i+=1
# print (factorial)


n = int(input('Enter the number n: '))
factorial = 1
while n>1:
    factorial=factorial*n
    n-=1
print (factorial)