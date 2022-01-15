
def binary_search(list,item):#이진탐색
	low=0
	high=len(list)-1
	
	while low<=high:
		mid=(low+high)//2
		guess=list[mid]
		if guess==item:
			return mid
		if guess>item:
			high=mid-1
		else:
			low=mid+1
	return None

#재귀
my_list=[1,3,5,7,9,11]
print(binary_search(my_list,1))
print(binary_search(my_list,4))
import time
def countdown(i):
    print(i)
    time.sleep(0.1)
    if i<=1:
        return
    else:
        countdown(i-1)
print(countdown(100))

#선택정렬
def findSmallest(arr):
	smallest=arr[0]#가장 작은 정수를 저장
	smallest=index=0#
