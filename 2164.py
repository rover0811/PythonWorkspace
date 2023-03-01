from collections import deque
import sys
card=deque(range(1,int(sys.stdin.readline())+1))


while(card):
    if(len(card)==1):
        break
    card.popleft()
    card.append(card.popleft())
    # print(card)
print(card.pop())