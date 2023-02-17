import random;

print("몇 자리 난수를 원하십니까?")
HowManyLength=int(input())

print("몇번?")
N=int(input())
for i in range(0,N,1):
    print(random.randint(10**(HowManyLength-1),10**(HowManyLength)))
