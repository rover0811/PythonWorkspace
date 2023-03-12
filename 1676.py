import math
print([i if i==0 else None for i in str(math.factorial(int(input())))[::-1]])