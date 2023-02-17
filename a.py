# from dataclasses import dataclass 
# from math import *
# from random import *

# @dataclass
# class nodetype:
#     parent:int=None
#     depth:int=None

# @dataclass
# class edge:
#     first:int=None
#     second:int=None
#     weight:int=None

# a=edge(1,2,3)
# b=nodetype(1,3)
# print(b

# # 

# random_num=floor(random()*(20-5))

# from math import *
# from random import *

# num_list = []
# for i in range(5):
#     num_list.append(randint(1, 5))

# mean = sum(num_list) / len(num_list)
# squared_deviation_sum = 0
# for num in num_list:
#     squared_deviation_sum += pow(num - mean, 2)
# variance = squared_deviation_sum / len(num_list)
# standard_deviation = sqrt(variance)

# print(f"데이터: {num_list}")
# print(f"평균: {mean}")
# print(f"편차 제곱의 합: {squared_deviation_sum}")
# print(f"분산: {variance}")
# print(f"표준 편차: {standard_deviation}")

money, day=map(int,input().split())
today=1
def getmoney(today,tempmoney,day,multi):
    if today<day:
        getmoney(today=today+1,tempmoney=tempmoney*multi,multi=multi)
    print(f"today:{today}\ntempmoney:{tempmoney}\nday:{day}\nmulti:{multi}")
getmoney(today=1,tempmoney=money,day=day,multi=money)
