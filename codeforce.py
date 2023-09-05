# t = int(stdin.readline())

# # for i in range(t):
# n,m = map(int,stdin.readline().split()) # n이 row의 갯수, m이 column의 갯수
# # carpet = np.array([k[index] for index,k in enumerate([stdin.readline().split() for i in range(n)])])

# carpet = [[] for i in range(m)]

# for i in range(n):
#     input_str = stdin.readline().rstrip()

#     for k in input_str:
#         carpet[i].append(k)


# carpet=np.array(carpet)
# carpet = carpet.transpose()

# counter = 0
# for letter in "vika":
#     for i in range(m):
#         print(carpet[i])
#         if letter in carpet[i]:
#             counter+=1
#             continue

# # if "v" in carpet[0]:
# #     print("Y")

# if counter == 4:
#     print("YES")
