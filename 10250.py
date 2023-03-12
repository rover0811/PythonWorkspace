import sys
input=sys.stdin.readline

T=int(input())
H,W,N=map(int,input().split())

호수=N//H
층수=N%H

#print(호수,층수)

# print(층수,호수+1)
print("{}{:02}".format(층수,호수+1))

