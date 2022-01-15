# a=[]
# for i in range(1,10,1):
#     a.append(int(input()))
# print(max(a))
# print(a.index(max(a))+1)

# a=int(input())
# b=int(input())
# c=int(input())

# cal=list(str(a*b*c))
# for i in range(10):
#     print(cal.count(str(i)))
# a=[]
# for i in range(10):
#     a.append(int(input())%42)
# a=set(a)
# print(len(a))

# n=int(input())
# a=list(map(int,input().split()))   #왜 a=[] a.append(map(int,input().split()))은 안될까??

# newlist=[]

# for score in a:
#     newlist.append(score/max(a)*100)  


# n=int(input()) #케이스 개수
# for i in range(n):
#     a=list(input())
# print(a)


a = 2
b = -3
c = 5
d = -7
e = 11

c += 1 + 2
b += c
a += b
print(a,b,c)
