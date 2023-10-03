a = input() # ABRACADABRA
b = input() # ECADADABRBCRDARA


dp = [[0] * (len(b) + 2) for _ in range(len(a) + 2)]
max = 0 
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dp[j+1][i+1] = dp[j][i] + 1
            if dp[j+1][i+1] > max:
                max = dp[j+1][i+1]

# print(*dp, sep='\n')

print(max)

      
    