# import itertools

# arr = [1, 2]
# nCr = itertools.permutations(arr, 2)
# print(list(nCr))



# N=int(input())
# a=[]
# for i in range(1,N+1):
#     a.append("*"*(2*i-1))
# asterisk='*'
# t=0
# width=0
# for i in range(N):
#     print("{0:{width}}".format("*"*(2*i-1),width=i))

# a.reverse()

# for i in range(N):
#     print(a[i])

# def asterisk(num:int):
#     return "*"*(2*num-1)
# width=1
# # print(asterisk(3))
# for num in range(1,10,2): 
#     width=num
#     print('{0:^{width}s}'.format(asterisk(num),width=width))

# def re(n:int):
#     if (n>1):
#         re(n-1)
#     for i in range(1,n+1):
#         print(i,end=" ")
#     print()

# re(5)

# def re(n:int, width:int):
#     if (n>1):
#         re(n-1,width)
#     print("*"*width)

# re(4,4)

# a,b=map(float,input().split())

# while(a<b):
#     print("%.2f"%a)
#     a+=0.01

# N=int(input())

# def re(n:int,limit:int):
#     if(n>1):
#         re(n-1,limit)
#     print(n, end=" ")
#     if (n==limit):
#         for i in range(n-1,0,-1):
#             print(i,end=" ")

# re(N,N)

# a=[5,34,56,-12,3,19]

# for i in range(len(a)):
#     max=a[0]
#     if (max<a[i]):
#         max=a[i]

# for index,value in enumerate("IT_CookBook_Python"[::-1]):
#     if (index%2==1):
#         print("#",end="")
#     else:
#         print(value, end="")

# a={""}



# [print(i, end="") for index,value in enumerate("IT_CookBook_Python"[::-1]) if index%2==0]

# from itertools import product

# n, m = map(int, input().split())
# items= []
# for i in range(1, n+1):
#     items.append(i)

# for i in product(items, repeat=m):
#     print(*i, end='\n')

# N=int(input())

# list=[i for i in range(1,N+1)]

# for index,value in enumerate(list):
#     for i in list[:index+1]:
#         print(i,end=" ")
#     print()
# print()
# for index,value in enumerate(list):
#     for i in list[:N-index]:
#         print(i,end=" ")
#     print()
# print()
# for index,value in enumerate(list):
#     print(str(value)*(index+1))
# print()
# for index,value in enumerate(list[::-1]):
#     print(str(value)*(N-index))


# # a=[1,2,3,4,5,6,7,8,9,10]

# # for i in a:
# #     print(i)

# a=map(int,input().split())

# a,b=3,4

# a,b=b,a

# print(a,b)

# array = [[0 for col in range(5)] for row in range(5)]
# k=0

# for row in array:
#     for i in row:
#         print(i,end=" ")
#     print()


# array = [[0 for col in range(5)] for row in range(5)]

# start=2
# end=4-start
# num=0
# for row in array:
#     for k in range(start,end):
#         row[k]=num
#         num+=1
    
#     start-=1
#     end=4-start
#     print(start,end)

# for i in range(5):
#     for k in range(5):
#         print(array[i][k], end=" ")
#     print()
# import math
# a,b=map(int,input().split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))
# sum=0
# a=[]
# for i in range(1,1000001):
#     sum=0
#     for item in str(i):
#         sum+=int(math.factorial(int(item)))
#     if(i==sum):
#         a.append(i)

# print(a)

# N=int(input())
# W=int(input())
# ary=map(int,input().split())
# sum=0
# front=0
# rear=0

# for i in range(len()): 

# sample_set = {"hello", 42, (1, 2, 3)}
# sample_set.add("world")
# sample_set.update("abc")  # set("abc") => {"a", "b", "c"}를 기존 집합에 더한다.
# sample_set.remove(42)
# for item in sample_set:
#     print(item, type(item))
# print(sample_set)

N=int(input()) #6
W=int(input()) #3

ary=list(map(int, input().split()))
# 1 0 2 0 4 3 

#현재 frontidx는 3이어야함
tempsum=sum(ary[:W])
sumary=[sum(ary[:W])]
frontidx=0
rearidx=W

for i in ary[N:]:
    sum=sum-ary[frontidx]+ary[rearidx]


    

    



