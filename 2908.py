A,B=map(str, input().split())
A=A[::-1]
B=B[::-1]
if A>B:
    print(int(A))
else:
    print(int(B))