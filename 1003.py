def fib(n):
    if n==0:
        print(0)
        return 0
    elif n==1:
        print(1)
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib(22)