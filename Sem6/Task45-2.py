import datetime
a = datetime.datetime.now()

def divider_sum(number):
    div_sum, i = 1, 2
    while i*i < number:
        if number % i == 0:
            div_sum += i
            div_sum += number // i
        i += 1
    return div_sum
            
num_k = int(input("Enter the k-number: "))

for m in range(1, num_k + 1):
    n = divider_sum(m)
    if m < n <= num_k and m == divider_sum(n):
        print(m, n)

print(datetime.datetime.now() - a)