import os
import time
import json


f = open('C:/Users/rover0811/Desktop/숭실대 폴더/밸리언트데이터 인턴/Paper/사전 검증 데이터/사전 검증 데이터/a.log', 'r')
dict = {}

start_time = time.perf_counter()

keyClass = {}
for i in range(100):
    tempKey = "{}~{}".format(5*i, 4+5*i)
    keyClass[tempKey] = 0
key = list(keyClass)

for i in range(2652823):  # 2652823
    a = f.readline().strip().rstrip('",').rstrip()
    if a.startswith("---------- A.LOG"):
        continue
    elif a == "":
        continue

    if a.startswith("----------"):
        tempJson = a.lstrip('---------- ').rstrip("\n")
        dict[tempJson] = keyClass
    tempNum = a.count(" ")
    tempIndex = tempNum//5
    dict[tempJson][key[tempIndex]] += 1

with open('./data.json', 'w') as hi:
    json.dump(dict, hi, ensure_ascii=False, indent=4)

end_time = time.perf_counter()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")
