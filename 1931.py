# N = int(input())
# a = []
# count = 0

# for i in range(N):
#     a.append(list(map(int, input().split())))
#     a[i].append(a[i][1]-a[i][0])
#     a[i].append(a[i][2]+a[i][0])

# while True:
#     wantKnow = min(a, key=lambda x: x[3])
#     a = [a[i] for i in range(len(a)) if a[i][0] >= wantKnow[1]]
#     count += 1
#     for i in range(len(a)):
#         a[i][3] = a[i][3] - wantKnow[3]
#     if not a:
#         break
# print(count)

'''
    기존 풀이
'''
# from sys import stdin
# from collections import deque
# N = int(stdin.readline())
# a = []

# count=0
# for i in range(N):
#     a.append(tuple(map(int, stdin.readline().split())))

# front=min(a,key=lambda x:x[0])[0] #가장 빠른 회의 시작
# ary=deque(sorted([(start,end,end-start,front+start+end-start) for start,end in a],key=lambda x:x[3]))

# for i in range(len(ary)):
#     temp_start=ary.popleft()[1] #가중치가 가장 낮은 튜플의 end가 현재 리스트의 start기준이 되어야함
#     print(temp_start)
#     count+=1
#     # print(ary)
#     '''
#         수정해야함...
#     '''
#     ary=deque([i for i in ary if i[0]>=temp_start]) # 여기서 full 순회를 돌리는게 문제인데...
#     if len(ary)==0:
#         break
# print(count)

'''
    누군가의 풀이... 흠...
'''

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))
print(time)
cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)