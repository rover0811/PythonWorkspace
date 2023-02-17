N = int(input())
a = []
count = 0

for i in range(N):
    a.append(list(map(int, input().split())))
    a[i].append(a[i][1]-a[i][0])
    a[i].append(a[i][2]+a[i][0])

while True:
    wantKnow = min(a, key=lambda x: x[3])
    a = [a[i] for i in range(len(a)) if a[i][0] >= wantKnow[1]]
    count += 1
    for i in range(len(a)):
        a[i][3] = a[i][3] - wantKnow[3]
    if not a:
        break
print(count)
