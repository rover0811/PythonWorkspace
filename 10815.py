import sys
N=int(input())
beforelist = list(map(int, sys.stdin.readline().split()))
M=int(input())
afterlist = list(map(int, sys.stdin.readline().split()))
beforelist.sort()
afterlist.sort()
print(beforelist)
print(afterlist)

for t,j in enumerate(afterlist):
    while(1):
        first=0
        last=N
        mid=N//2
        if afterlist[t]> beforelist[mid]:
            first=mid+1
        elif afterlist[t]< beforelist[mid]:
            last=mid-1
        else:
            return 




