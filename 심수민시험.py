
i=0
a=[20,30,40,50]
for i in range(0,len(a)-1):
    b=[]
    b.append(abs(a[i]-a[i+1]))
print(b)