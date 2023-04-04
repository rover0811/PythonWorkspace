import sys
import math
input = sys.stdin.readline

N = int(input()) #입력 받은 수

for i in range(N,0,-1):
    print(i,math.factorial(i),str(math.factorial(i)).count("0"))

# count = 0
# while N >= 5: 
#     count += N//5 
#     N //= 5 
    
# print(count)
