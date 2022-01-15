# import time
# a=input()
# for i in range(97,123):
#     print(a.find(chr(i)),end=' ')
a=int(input())      
b,c= input().split()
b=int(b)

for i in range(len(c)):
    print(c[i]*b,end='')
