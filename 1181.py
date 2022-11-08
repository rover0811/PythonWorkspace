import sys
input=sys.stdin.readline
a=[]
for i in range(int(input())):
    a.append(input().rstrip())

for i in sorted(a,key=len):
    print(i)