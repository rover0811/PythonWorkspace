# array=[i*i for i in range(10)]# 리스트 내포 -> 리스트 이름=[표현식 for 반복자 in 반복할 수 있는 것]
# print(array) 

#이터레이터 reversed()의 리턴값은 iterator이다-> 장점: 메모리 절약 기존에 있던 리스트의 인덱스 정보를 가지고 있는건가..?

class Node(object):
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.data=data
class DoubleCircleLinkedList(object):
    def __init__(self):
        