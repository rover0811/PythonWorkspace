print("Error is %d%%." % 98) #포매팅코드 %에서 실제 퍼센트(%)를 쓰고 싶을 때는 %%로
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

# %s는 거의 만능 왜와이? 그냥 다 문자열로 바꿈

print("%10s" % "hi")

print("%10sjane." % 'hi') #"%10s" % 는 공백 10자리 만들고 우정렬

print("%-10sjane." % 'hi')

print("%0.4f" % 3.42134234) #4번째 자리까지 소수점 살리기

print("%10.4f" % 3.42134234) #