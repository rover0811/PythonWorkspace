# 전역 변수에 접근하는 다른 방법들

var=99

def local():
    var=0

def glob1():
    global var
    var+=1

def glob2():
    var=0
    import clojure
    clojure.var+=1

def glob3():
    var=0
    import sys
    glob=sys.modules['clojure']
    glob.var+=1

def test():
    print(var) # 99
    local();glob1();glob2();glob3() #glob1에서 100이됨, #glob2에서 101됨, # glob3에서 102됨
    print(var)

# test()

#범위와 중첩함수

x=99

def f1():
    x=88
    def f2():
        print(x)
    f2()

# 이 f2는 바깥쪽 함수 f1이 실행되는 동안에만 존재하는 임시함수다..
# f1()

def f1():
    x=88
    def f2():
        print(x)
    return f2

action=f1() #여기서 action이 가지고 있는 것은 f2라는 함수
# action() #f2가 x값을 기억하고 있다는 것..!

#팩토리 함수: 클로저

def maker(N):
    def action(X):
        return X**N
    return action

a=maker(4) #a라고 하는 action 함수 객체는 N에 4가 들어왔다는 사실을 기억하고 있다...
#print(a(2)) 

def maker(N):
    return lambda x:x**N

#print(maker(4)(2)) # 이게 되네... maker(4)는 lambda x:x**4 그리고 거기서 x값에 2를 대입한것..

# 클로저 vs 클래스, 라운드 1

#그렇지만 여전히 클로저 함수는 상태 정보 저장만을 목표로 할 때, 보다 가볍고 실행 가능한 대안이 될 수 있다.
# 클로저 함수는 호출될 때마다 지역범위의 스토리지가 생성되고, 이 안에 그 중첩함수가 필요로 하는 데이터가 저장됨.

# nonlocal이 나오면서 더 강력한 대안이 됨

# 기본 인수로 외부 범위 상태 정보 유지하기

#반면에, 클로저의 중첩함수는 람다 함수와 마찬가지로 파이썬 코드에서는 매우 일반적으로 사용됨.

#중첩된 범위, 기본 인수, 람다 함수

#lambda는 def문 처럼 나중에 호출될 새로운 함수를 생성하는 표현식이다. lambda는 표현식이므로 리스트나 딕셔너리 리터럴처럼 def가 사용될 수 없는 곳에서도 사용할 수 있다..


# def func():
#     x=4
#     return lambda n:x**n

# print(func()(4))

# def makeActions():
#     acts=[]
#     for i in range(5):
#         acts.append(lambda x:i**x)
#     return acts

# acts=makeActions()

# print(acts[0](2))
# print(acts[1](2))

# def out():
#     a=3
#     def inner():
#         nonlocal a
#         a=5
#         return a
#     return inner

# a=out()()

# print(a)

'''
    얕은 복사 실험
'''
# element=[1,2,3]

# outer=[element]

# def is_deepcopy(locally_named_list):
#     sliced_copied_list=locally_named_list[:]
#     if sliced_copied_list[0] is element:
#         print("Yes")
#         sliced_copied_list[0].append(1)
#     else:
#         print("No")
    
#     method_copy_list=locally_named_list
    
    


# print(outer)
# is_deepcopy(outer)
# print(outer)


'''
    튜플에 리스트
'''
# a=([1,2,3,4,5],[2,3,4,5])

# print(a)
# print(type(a))

# b=[1,2,3,4],

# print(b)
# print(type(b))

# b=tuple([1,2,3,4])

# print(b)
# print(type(b))

# b=([1,2,3,4])

# print(b)
# print(type(b))

# a=[1,2,3]

# def func(b):
#     b.append(4)
#     print(id(b))
#     print(id(a))
#     print(local())
#     print(globals())


# func(a)

def decorator1(func):
    def wrapper(x):
        print("Decorator 1 before function") 
        result = func(x)
        print(f"decorator1 result: {result}")
        print("Decorator 1 after function")
        return result

    return wrapper


def decorator2(func):
    def wrapper(x):
        print("Decorator 2 before function")
        result = func(x)
        print(f"decorator2 result: {result}")
        print("Decorator 2 after function")
        return result

    return wrapper


@decorator1
@decorator2
def my_func(x):
    return x + 1


# decorator1(decorator2(my_func))(100) 동등
my_func(100)





    





