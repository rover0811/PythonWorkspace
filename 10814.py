'''
    이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
'''
# import sys
# N=int(sys.stdin.readline())

# a=[]
# for i in range(N):
#     age,name=sys.stdin.readline().split()
#     a.append((int(age),name,i))
# a=sorted(a,key=lambda x:(x[0],x[2]))


# for i in a:
#     print(i[0],i[1])



## 틀림
# [print(k[0],k[1]) for k in sorted([(*input().split(),i) for i in range(int(input()))],key=lambda x:(x[0],x[2]))]

