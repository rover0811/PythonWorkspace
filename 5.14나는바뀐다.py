# 02-2 문자열 자료형


# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date=a[:8] #파이썬의 숫자 세기는 0부터! [0:8]이면 0~7까지라는 사실!!!
#그리고 슬라이싱할 때의 문법 재료[시작:끝에서 하나 더 간것] 시작이 0일때 생략 o, 진짜 끝까지면 생략 o
#헷갈리기 쉽지만 수학에서의 +1이 아니라 진행방향에서 하나 더간것을 의미 0~8까지 뽑아내고 싶으면 [0:9] 0부터 -8까지
# 뽑아내길 원하면, [0:-9]
print(date)
weather=a[8:]
print(weather)

c=a[:] #둘다 생략시 모두 뽑아낸다
print(c)

b = "Life is too short, You need Python"
#    0123456789012345678901234567890123
#                            0987654321 여기서는 음수
d=b[:-5] #그러니 음수일때 -7까지면 -8까지 표현해주는 것 끝-1까지 표현해주는 것!
print(d)

# ["Pithon"이라는 문자열을 "Python"으로 바꾸려면?]

a = "Pithon"

print(a[:1]+"y"+a[2:]) #문자열끼리 합치기!!

# 문자열 포매팅

# %d => 정수 
# %s => 문자열
# %f => 실수
# %% =>%문자 자체





성=input("당신의 성은 무엇입니까?")
이름=input("당신의 이름은 무엇입니까?")
풀네임=성+이름
print("안녕하십니까 %s 고객님"%풀네임) #문자열 string => %s

잔고=input("당신의 잔고는 몇 원입니까?")
print("%s님의 잔고는 %s원입니다"%(풀네임,잔고))
# 
