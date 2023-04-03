A = int(input('Enter the number A>1: '))
first = 0
second = 1
# if A == 0:
#     print(1)
# elif A == 1:
#     print(2)
    
count = 2
while second < A:
    buffer = first + second
    first = second
    second = buffer
    count+=1
if second == A:
    print(count)
else: 
    print(-1)
 