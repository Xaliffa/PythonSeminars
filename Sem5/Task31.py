def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

N = int(input("Enter the number N: "))
print(fib(N))