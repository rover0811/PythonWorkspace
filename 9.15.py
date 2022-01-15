print("%d"%123)
print("%5d"%123)
print("%05d"%123)

print("%f"%123.45)
print("%7.1f"%123.45)
print("%7.3f"%123.45)

print("%s"%"python")
print("%10s"%'python')

print("%d %5d %05d"%(123,123,123))
print("{0:d} {1:5d} {2:05d}".format(123,123,123))

print("\n줄바꿈\n연습")
print("\t탭키연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과1")
print("\\\\\ 역슬래쉬 세개 출력")
print(r"\n \t \" \\를 그대로 출력")

a=int(input("첫번째 숫자:"))
b=int(input("두번째 숫자:"))

result=a+b
print(a,"+",b,"=",result)

result=a-b
print(a,"-",b,"=",result)

result=a*b
print(a,"*",b,"=",result)

result=a/b
print(a,"/",b,"=",result)

print(0b10010011)

print(int('10010011',2))

print(int('93',16))

sel=int(input("입력진수 결정(16/10/8/2): "))
num=input("값입력: ")

if sel==16:
    num10=int(num,16)
elif sel==10:
    num10=int(num,10)
elif sel==8:
    num10=int(num,8)
elif sel==2:
    num10=int(num,2)       

print("16진수 ==>",hex(num10))    
print("10진수 ==>",num10)    
print("8진수 ==>",oct(num10))    
print("2진수 ==>",bin(num10))    

a=0xFF
b=0o77
c=0b1111

print(a,b,c)

a=3.14
b=3.14e5
print(a,b)

a=10; b=20
print(a+b,a-b,a*b,a/b)

a,b=9,2
print(a**b,a%b,a//b)

a=(100==100)
b=(10>100)
print(a,b)

money=int(input("교환할 돈은 얼마? "))
c500=money//500
money %=500
c100=money//100
money%=100
c50=money//50
money%=50
c10=money//10
money%=10

print("\n오백원짜리 ==>%d개"%c500)
print("\n백원짜리 ==>%d개"%c100)
print("\n오십원짜리 ==>%d개"%c50)
print("\n십원짜리 ==>%d개"%c10)
print("\n바꾸지 못한 잔돈 ==>%d개\n"%money)

a=123456789
print(a)
print(2**100)

a=0x1a
print(a)

a=0b1101
print(a)

print(hex(26))
print(oct(26))
print(bin(26))

a=9.64e12
print(a)

a=1+2j
b=3+4j

print(a+b)

a="korea 서울 1234"
print(a)

a='i say "Help" to you'

a="i say \"Help\" to you'"
print(a)

a="first\tsecond"

print(a)

a="first\nsecond"

print(a)

a="first\\second"
print(a)

a="old\nnew"
print(a)

s='''강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네
길은 외주릭 남도 삼백리 술 익는 마을마다 타는 저녁놀
구름에 달 가듯이 가는 나그네'''
print(s)

s="강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네\
길은 외주릭 남도 삼백리 술 익는 마을마다 타는 저녁놀\
구름에 달 가듯이 가는 나그네"
print(s)

totalsec=365*24*\
    60*60
print(totalsec)

s="Korea" "Japan" "2002"
print(s)
s="Korea Japan 2002"
print(s)
s=("Korea"
"Japan"
"2002")
print(s)

print(ord("A"))
print((98))
print(98)

for c in range(ord("A"),ord("Z")+1):
    print(chr(c),end= " ")

a=5
b=a==5
print(b)

a=5
if a==5:
    print("a는 5")

a=None
print(a)

member=['손오공','저팔계','사오정','삼장법사']
for m in member:
    print(m, "출동")




