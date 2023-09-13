# 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

abs_heap = []

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        if len(abs_heap):
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(n), n))



# answer = [-1,
#           1,
#           0,
#           - 1,
#           - 1,
#           1,
#           1,
#           - 2,
#           2,
#           0]

# if result == answer:
#     print("정답입니다.")