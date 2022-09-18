import sys
n=int(sys.stdin.readline().strip())
a={}

for i in range(n):
    age,name=sys.stdin.readline().split()
    a[name]=age
print(a)











