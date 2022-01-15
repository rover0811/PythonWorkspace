# a,b=(map(int,input().split()))
# realtime=60*a+b
# alarmtime=realtime-45
# diplaysi=alarmtime//60
# if diplaysi<0:
#     diplaysi=diplaysi+24
# diplaybun=alarmtime%60
# print(diplaysi,diplaybun)


# n=int(input())
# for i in range(1,10):
#     print("%d * %d = %d"%(n,i,n*i))
#     i+=1

# n=int(input())
# for i in range(1,n+1,1):
#     a,b=map(int,input().split())
#     print(a+b)
#     i+=1

# n=int(input())
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# print(sum)

# n=int(input())
# for i in range(n,0,-1):
#     print(i)
#     i+=1

# n=int(input())
# for i in range(1,n+1,1):
#     a,b=map(int,input().split())
#     print("Case #%d: %d + %d = %d"%(i,a,b,a+b))

# n=int(input())

# for i in range(1,n+1,1):
#     print(" "*(n-1)+"*"*i)
#     n-=1

# while 1:
#     a,b=map(int,input().split())
#     if (a==0)and (b==0):
#         break
#     else:
#         print(a+b)

# while 1:
#     try:
#         a,b=map(int,input().split())
#     except:
#         break
#     print(a+b)


# import time
# a=int(input())
# ten=a/10
# one=a%10
# newone=ten+one
# newten=10*one
# while a==newten+newone:
#     if a<10:
#         a=10*a
#         ten=a/10
#         one=a%10
#         newone=ten+one
#         newten=10*one
#         a=newten+newone
#     else:
#         a=newten+newone

#     print(newten+newone)

    
        

# import time
# 입력받은수=int(input())
# 기존수의십의자리=입력받은수//10
# 기존수의일의자리=입력받은수%10
# while 입력받은수==새로운수:
#     if 입력받은수<10:
#         새로운수=기존수의일의자리*10
#         print(새로운수)
#         time.sleep(1)
#     else:
#         새로운수의십의자리수=기존수의일의자리
#         새로운수의일의자리수=기존수의십의자리+기존수의일의자리
#         새로운수=새로운수의십의자리수*10+새로운수의일의자리수
#         print(새로운수)
#         time.sleep(1)
# import time

# given=int(input())
# giventen=given//10
# givenone=given%10
# newnumber=given
# i=0
# if given>=10:
#     given=10*givenone+((giventen+givenone)%10)
#     giventen=newnumber//10
#     givenone=newnumber%10

# else:
#     newnumber=given*10
#     giventen=newnumber//10
#     givenone=newnumber%10

# while newnumber!=given:
#     if newnumber>=10:
#         newnumber=10*givenone+((giventen+givenone)%10)
#         giventen=newnumber//10
#         givenone=newnumber%10
#         print(newnumber)
#         newnumber=10*givenone+((giventen+givenone)%10)
#         i+=1
#         time.sleep(1)

#     else:
#         newnumber=given*10
#         giventen=newnumber//10
#         givenone=newnumber%10
#         print(newnumber)
#         i+=1
#         time.sleep(1)
# print(i)


# for i in range(0,len(str)-1,1):
#     for k in range(0-speed,len(str)-speed,1):
#         print(str[k],end="")
#         time.sleep(0.3)
#     if 2*speed<len(str):
#         speed+=speed
#     else:
#         speed-=speed
#     print()

# print(str[speed+k])

# for i in range(0,):
#     for k in range(0-speed,len(str)-speed,1):
#         a.append(str[k])
#         x="".join(a)
        
#         time.sleep(0.3)
#     print(x)
#     x=0
#     if 2*speed<len(str):
#         speed+=speed
#     else:
#         speed-=speed
#     if x==originalstr:
#         break
#     print()


# str="012345"
# originalstr=str
# speed=2
# k=0

# import time
# while 1:
#     k=(k+speed)%len(str)
#     s=str[-k:]+str[:-k]
#     print(s)
#     time.sleep(0.7)
 
    
#     if s==originalstr:
#         break

# n=int(input())
# f=int(input())
# i=1

# while ((n+i)%f==0):
#     i+=1
# print("%02d"%(i+1))

# print(int(input(),16)) #16진수 입력받아 10진수로 변환 int(입력받은수, 진수종류)

# hard, cost, price=map(int,input().split())
# d=0
# while price*d<=hard+cost*d:
#     d+=1
#     if price<=cost:
#         d=-1
#         break
# print(d)

# if price<=cost:
#     print(-1)
# def eco(x):
#     y=hard+cost*x-price*x
#     return y
# print(eco(x))


# 
# a=int(input())
# b=0
# while a>15:
#     a-=15
#     b+=1
# if a%15==1:
#     print(-1)
# if a%15==2:
#     print(-1)
# if a%15==4:
#     print(-1)
# if a%15==7:
#     print(-1)
# elif a%15==3:
#     print(1+3*b)
# elif a%15==5:
#     print(1+3*b)
# elif a%15==6:
#     print(2+3*b)
# elif a%15==8:
#     print(2+3*b)
# elif a%15==9:
#     print(3+3*b)
# elif a%15==10:
#     print(2+3*b)
# elif a%15==11:
#     print(3+3*b)
# elif a%15==12:
#     print(3+3*b)
# elif a%15==13:
#     print(3+3*b)
# elif a%15==14:
#     print(4+3*b)
# elif a%15==0:
#     print(3+3*b)

x=int(input())
a=64
b=0
while x<a:
    a=0.5*a
    b+=a
    if b>x:










