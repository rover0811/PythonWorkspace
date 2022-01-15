
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
print(countdown(5))

#선택정렬

def findSmallest(arr):
	smallest=arr[0]						#가장 작은 정수를 저장
	smallest_index=0					#가장 작은 정수의 인덱스를 저장
	for i in range(1,len(arr)):			# 1부터 배열의 크기만큼 진행한다
		if arr[i]<smallest:				#만약 배열의 한놈이 smallest(첫번째 놈)보다 작을 경우
			smallest=arr[i]				#그놈이 smallest가 된다
			smallest_index=i			#당연히 smallest의 인덱스도 변경 되기 마련
	return smallest_index				#그리고 smallest의 인덱스를 뱉어내기

def selectionSort(arr):					#자 이제 드가자
	newArr=[]							#새로운 배열의 공간을 만들어주고
	for i in range(len(arr)):			#배열의 길이만큼 반복한다 무엇을?
		smallest=findSmallest(arr)		#제일 작은 놈은 findSmallest가 뱉어낸 놈	
		newArr.append(arr.pop(smallest))#새로운 빈 배열에 하나씩 smallest들을 하나씩 넣어주기
	return newArr

print(selectionSort([5,3,6,2,10]))

#append와 pop의 차이는 뭐지?
#append는 리스트 끝에 박아넣기
#pop은 리스트에서 하나씩 없애면서 반환을 해줌 그러니 2개 이상의 리스트가 필요하겠군..
	
