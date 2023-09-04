from sys import stdin
# 좌표 압축
n = int(stdin.readline())
point_list = list(map(int,stdin.readline().split()))

sorted_point_list = sorted(list(set(point_list))) # 중복 제거 후 정렬

point_dict = {sorted_point_list[i]:i for i in range(len(sorted_point_list))} # 좌표 압축 딕셔너리

print(*[point_dict[i] for i in point_list])
