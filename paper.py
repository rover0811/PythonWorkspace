# import itertools

# arr = [1, 2]
# nCr = itertools.permutations(arr, 2)
# print(list(nCr))



# N=int(input())
# a=[]
# for i in range(1,N+1):
#     a.append("*"*(2*i-1))
# asterisk='*'
# t=0
# width=0
# for i in range(N):
#     print("{0:{width}}".format("*"*(2*i-1),width=i))

# a.reverse()

# for i in range(N):
#     print(a[i])

def asterisk(num:int):
    return "*"*(2*num-1)
width=1
# print(asterisk(3))
for num in range(1,10,2): 
    width=num
    print('{0:^{width}s}'.format(asterisk(num),width=width))




