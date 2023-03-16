from math import factorial, log10,log2
from sys import stdin

N=int(stdin.readline())

a=[(k[0],*map(int,k[1:]))for k in [list(stdin.readline().split()) for i in range(N)]]

#시간복잡도, 입력의 최대 범위, 테스트 케이스의 수, 제한시간
# print(a)
PERFORMANCE=100000000
#채점 시스템은 1초에 100000000가지 연산을 할 수 있음
for i in a:
    if i[0]=="O(N)":
        if i[3]*PERFORMANCE>=i[1]*i[2]*1:
            print("May Pass.")
        else:
            print("TLE!")
    elif i[0]=="O(N^2)":
        if i[3]*PERFORMANCE>=i[1]**2*i[2]:
            print("May Pass.")
        else:
            print("TLE!") 
    elif i[0]=="O(N^3)":
        if i[3]*PERFORMANCE>=i[1]**3*i[2]:
            print("May Pass.")
        else:
            print("TLE!") 
    elif i[0]=="O(2^N)":
        if i[3]*PERFORMANCE>=2**i[1]*i[2]:
            print("May Pass.")
        else:
            print("TLE!") 
    elif i[0]=="O(N!)":
        if i[3]*PERFORMANCE>=factorial(i[1])*i[2]:
            print("May Pass.")
        else:
            print("TLE!") 

# O (N), O (N^2), O (N^3), O (2^N), O (N!)