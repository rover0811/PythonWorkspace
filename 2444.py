n = int(input())

for i in range(n):
    print(' ' * (n - i - 1), end='')
    print('*' * (2*i + 1))

for i in range(n-1, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * (2*i - 1))

# 한줄 풀이
