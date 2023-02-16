'''
    번호: 1978번
    정답
'''

N=int(input())

a=list(map(int,input().split()))   
b=[] 

def isPrime(input:int):
    if input==1:
        return False
    for i in range(2,int(input/2)+1):
        if input%i==0:
            break
    else:
        return True
    return False

for i in a:
    b.append(isPrime(i))

print(b.count(True))

# for i in a:
#     if(i==1):
#         continue
#     elif(i%2==0):
#         if(i==2):
#             b.append(i)
#         else:
#             continue
#     elif(i%3==0):
#         if(i==3):
#             b.append(i)
#         else:
#             continue
#     elif(i%5==0):
#         if(i==5):
#             b.append(i)
#         else:
#             continue
#     elif(i%7==0):
#         if(i==7):
#             b.append(i)
#         else:
#             continue
#     else:
#         b.append(i)

