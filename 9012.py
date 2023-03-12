from sys import stdin

T=int(stdin.readline())

a=[]
for i in range(T):
    a.append(input())
# print(len(a))
newidx=0
for i in a:
    new=i
    while ("()" in new):
        newidx=new.find("()")
        if newidx==-1:
            break
        else:
            new=new[:newidx]+new[newidx+2:]
    if (len(new)>0):
        print("NO")        
    else:
        print("YES")

        
    # if i in "()":
    #     print("NO")
    # else:
    #     new=i
    #     newidx=new.find("()")
    #     new=new[:newidx]+new[newidx+2:]
        
# for i in a:
#     left=list()
#     right=list()
#     # for newidx,k in enumerate(i):
#     #     if newidx==0 and k=="(":
#     #         left.append("(")
#     #         continue
#     #     elif newidx==0 and k==")":
#     #         print("NO")
#     #         break
#     #     if k=="(":
#     #         left.append(k)
#     #     elif k==")":
#     #         right.append(k)
#     # else:
#     #     continue

    
#     while(len(left)>0 and len(right)>0):
#         left.pop()
#         right.pop()
#     if (len(left)==0 and len(right)==0):
#         print("YES")
#     else:
#         print("NO")

    

# print(left,right)

