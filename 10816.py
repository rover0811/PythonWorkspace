N=int(input())

pocketcard=list(map(int,input().split()))
set_pocket=set(pocketcard)

pocketcard={ i:pocketcard.count(i) for i in set_pocket}

# print(pocketcard)

M=int(input())

querycard=list(map(int,input().split()))
keys=pocketcard.keys()
for i in querycard:
    if i in keys:
        print(pocketcard[i],end=" ")
    else:
        print("0",end=" ")

