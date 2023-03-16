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

# N=int(input()) #6
# W=int(input()) #3

# ary=list(map(int, input().split()))
# # 1 0 2 0 4 3 

# #현재 frontidx는 3이어야함
# tempsum=sum(ary[:W])
# sumary=[sum(ary[:W])]
# frontidx=0
# rearidx=W

# for i in ary[N:]:
#     sum=sum-ary[frontidx]+ary[rearidx]

# M=4
# N=4
# dp = [[0] * (M+1) for _ in range(N+1)]

# print(dp)

# 1844번
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 부분의 개수 입력
# K = int(input())
# dp = [[0] * (M+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

# print(dp)

# from collections import deque


# a=deque()

# a.append(3)
# a.append(2)
# a.append(1)

# print(sum(a))

# from collections import deque
# N=int(input())
# W=int(input())
# temp_sum=0
# sum_ary=[]
# ary=deque(map(int,input().split()))

# for i in range(W):
#     if i==0:
#         last=ary.popleft()
#         temp_sum+=last
#     else:
#         temp_sum+=ary.popleft()


        
# sum_ary.append(temp_sum)

# print(sum_ary)
# print(ary)

# for index,value in enumerate(ary):
#     temp_sum=ary.

# N=int(input())
# W=int(input())

# ary=list(map(int,input().split()))

# a=[]
# for i in range(N-W+1):
#     a.append(sum(ary[i:W]))
#     W+=1
# # print(a)
# print(max(a))

# sample_dict = {"key_1": "foo", "key_2": "bar", "key_3": "baz"}
# # key_list = sample_dict.keys() # 딕셔너리의 key들을 iterable 객체로 돌려준다.
# *value_list, = sample_dict.values() # 딕셔너리의 value들을 iterable 객체로 돌려준다.
# # print(type(sample_dict.items()))
# # *key_value_list, = sample_dict.items() # 딕셔너리의 (key, value) 튜플들을 iterable 객체로 돌려준다.
# # print(key_list)
# # print(value_list)
# # print(key_value_list)
# sample_dict = {"key_1": "foo", "key_2": "bar", "key_3": "baz"}
# sample_dict.update([("key_4", "qux")])

# print(sample_dict)

# dic = {1:1, 2:1}

# def fib_memoization(n):
#     if n in dic:
#         return dic[n]
#     dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
#     return dic[n]

# fib_memoization(10)

# print(dic)

# import streamlit as st


# st.area_chart()

# import pandas as pd
# import numpy as np

# # Create a sample dataframe
# df = pd.DataFrame({
#     'x': np.arange(10),
#     'y': np.random.randn(10)
# })

# # Draw a line chart using the 'line_chart' function
# st.line_chart(df)

# import streamlit as st
# import pandas as pd
# import altair as alt

# # Load data into a Pandas DataFrame
# data = {'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
#         'time_series_1': [10, 12, 8, 14, 16],
#         'time_series_2': [20, 18, 22, 24, 26],
#         'time_series_3': [30, 34, 32, 28, 36]}
# df = pd.DataFrame(data)
# df['date'] = pd.to_datetime(df['date'])
# df.set_index('date', inplace=True)

# # Create a Streamlit app
# st.title('Visualizing Multiple Time Series Data')
# st.subheader('Using Streamlit and Altair')

# # Create a Streamlit sidebar
# time_series = st.sidebar.selectbox('Select Time Series', df.columns)

# # Create a range slider for date selection
# start_date = st.sidebar.date_input('Start Date', df.index.min())
# end_date = st.sidebar.date_input('End Date', df.index.max())

# # Filter the DataFrame based on the date range
# filtered_df = df.loc[start_date:end_date]

# # Create a line chart using Altair
# chart = alt.Chart(filtered_df.reset_index()).mark_line().encode(
#     x='date',
#     y=time_series
# ).properties(
#     width=600,
#     height=400
# )

# # Add the chart to the Streamlit app
# st.altair_chart(chart, use_container_width=True)

# print(oct(int(input(),2))[2:])

# n=int(input())

# for i in range(1,n+1):
#     for k in range(1,n+1):
#         if (i!=n):
#             if (k==1):
#                 print("*",end="")
#             elif(k==n):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# a=input()

# if (a==a[::-1]):print(True)
# else:print(False)

# if len(a)%2==0:
#     if (a[:len(a)/2]==a[len(a)/2::-1]):
#         print(True)
#     else:
#         print(False)
# else:
#     if (a[:len()])


# a=list((range(10),range(10),range(10)))

# b=a

# c=[*a]
# a.append(1)
# c.pop()

# print(a)
# print(b)
# print(c)

# a,*b=range(10)

# from sys import stdin

# N,M=map(int,stdin.readline().split())

# a={}
# b=[]
# for i in range(N):
#     temp=tuple(stdin.readline().split())
#     a[temp[0]]=temp[1]


# for i in range(M):
#     b.append(stdin.readline().strip())


# for i in b:
#     print(a[i])

# import Fibonacci

# Fibonacci.fib(2)

# from sys import stdin

# N=int(stdin.readline())
# a=[]
# for i in range(N):
#     a.append(int(stdin.readline()))


# N=int(input())
# M=map(int, input().split())
# K=int(input())
# a=[]
# for i in range(K):
#     a.append(tuple(map(int, input().split())))
# print(K)
# for i in range(K):
#     for t in M:
#         print(t)

# a = set("11122")
# b = set("22333")
# print(f"a: {a}, b: {b}")
# print(f"a | b: {a | b}")  # 집합 a와 b에 존재하는 모든 요소 출력

# a = set("11122")
# b = set("22333")
# print(f"a: {a}, b: {b}")
# print(f"a & b: {a & b}")

# def intersect(x,y):
#     return {*x}&{*y}

# print(intersect([1,2,3,4],[2,3,4]))

# def get_factorial(n):
#     """n!의 값을 돌려준다."""
#     result = 1
#     for item in range(2, n + 1):
#         result *= item
#     return result


# for item in range(2):
#     print(f"{item}! = {get_factorial(item)}")

# a=[]

# def add():
#     a.extend(list(range(10)))

# add()

# print(a)

def initialize():
    global count
    count=0


def counter():
    cnt = count

    def increment():
        nonlocal cnt
        cnt += 1

    increment()
    return cnt


initialize()

count=counter()

print(count)




    

    



