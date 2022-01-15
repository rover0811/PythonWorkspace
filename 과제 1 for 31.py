print("PASS or FAIL program")
q= int(input("퀴즈 점수는 몇점입니까? "))
m= int(input("중간 고사 점수는 몇점입니까? "))
f= int(input("기말고사 점수는 몇점입니까? "))
c= 0.2*q + 0.3*m+ 0.5*f 

if c>=70:
    print("당신의 점수는 %d점입니다. 70점 이상이므로 PASS입니다." %c)
else:
    print("당신의 최종 점수는 %d점입니다. 70점 미만이므로 FAIL입니다." %c)


print("===당신은 건강하십니까?===")
h=float(input("당신의 키는 몇 cm입니까?" ))
kg=float(input("당신의 몸무게는 몇 kg입니까?" ))
standard=(h-100)*0.9
ratio=kg/standard
if ratio<0.85:
    print("당신은 저체중입니다. 제 때에 많이 먹고 운동도 하세요.")
elif 0.85<= ratio < 1.15:
    print("당신은 정상 몸무게입니다. 지금 체중을 잘 유지하세요.")
elif 1.15<= ratio <1.3:
    print("당신은 과체중입니다. 약간 살이 쪘네요. 주 2일은 운동하세요.")
elif 1.3<= ratio :
    print("당신은 비만입니다. 식사량을 줄이고 주 3일 이상 운동하세요.")