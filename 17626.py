import math
N=int(input())
square=frozenset(i**2 for i in range(1,math.floor(math.sqrt(N))+1))


def Lagrangian_sum(N, square_list):
    # square_2_list=set()
    if N in square_list:
        return 1
    # for i in square_list: # 1 4, 9, 16 ,25
    #     sub=N+i
    #     square_2_list.add(sub)
    #square_2_list={sum(a) for a in set(itertools.combinations(square_list,2))} # 이 자리 수정
    square_2_list=nc2(square_list)
    # print(square_2_list)
    if N in square_2_list:
        return 2
    for s in square_list:
        for t in square_2_list:
            if s+t==N:
                return 3
    return 4
    

def nc2(itterable):
    nc2_set=set()
    itterable=list(itterable)
    for i in range(len(itterable)):
        for k in range(len(itterable)):
            # print(itterable[i],itterable[k]) # nC2 구현
            nc2_set.add(itterable[i]+itterable[k])
    return nc2_set
    
print(Lagrangian_sum(N,square))        



# nC2 -> n(n-1)/2






# a^2

# a^2+b^2

# a^2+b^2+c^2

# a^2+b^2+c^2+d^2



