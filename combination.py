

def nc2(itterable):
    for i in range(len(itterable)-1):
        for k in range(i+1,len(itterable)):
            print(itterable[i],itterable[k])


nc2([1,2,3,4,5,6])