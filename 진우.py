from collections import deque
a=deque((0,1))
def fib(n):
    a.append(fib(n-1)+fib(n-2))


# fib(int(input()))
fib(10)

print(a)
