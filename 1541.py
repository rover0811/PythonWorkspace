from sys import stdin
import re
line = stdin.readline().rstrip()

# 정규표현식으로 숫자만 추출
# 그러면 연산은 어떻게 하게? -> 숫자만 추출한 리스트를 만들어서 연산
# 연산자는 어디로 가는데?
# 연산자는 숫자 리스트보다 1개 적음

# 숫자만 추출
num_list = re.findall('\d+', line)

# 연산자만 추출
op_list = re.findall('[+|-]', line)

# 연산자가 없으면 그냥 출력
if len(op_list) == 0:
    print(num_list[0])
else:
    # 연산자가 있으면 연산
    # 괄호를 쳐서 연산자 우선순위를 바꿔줌

    