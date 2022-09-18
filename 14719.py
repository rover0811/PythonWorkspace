# H, W = map(int, input().split())
# arr = list(map(int, input().split()))
# water=0
# temp=0
# for i in range(H):        #4번 반복 높이만큼
#     for i in range(len(arr)):
#         if arr[i]==1:
#             for t in range(i+1,len(arr)):
#                 if arr[t]==0:
#                     temp+=1
#                 else:
#                     water+=temp
#                     temp=0
#                     i=t
#                     break
#     for j in range(W):
#         if arr[j]>0:
#             arr[j]-=1

# print(water)

H, W = map(int, input().split())
arr = list(map(int, input().split()))

temp=0
water=0
for t in range(H):
    for i in range(W):
        if arr[i]==1:
            for k in range(i+1,W):
                if arr[k]==0:
                    temp+=1
                else:
                    water+=temp
                    temp=0
                    i=t
                    break
    for j in range(W):
        if arr[j]>0:
            arr[j]-=1

print(water)
            
            


    

