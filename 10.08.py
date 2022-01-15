a,b=map(int,input().split())


c=list(input().split(" "))
print(c)

for i in range(a):
    if int(c[i])<b:
        c.remove(c[i])
print(c)