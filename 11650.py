N=int(input())
a=[]
for i in range(N):
    a.append(tuple(map(int,input().split())))
for k,p in sorted(a):
    print(k,p)