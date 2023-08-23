# [ for i in range(int(input()),0,-1)]

# 백준 2441번을 푸는 한줄 코드입니다.
a=int(input());[print(' '*(a-i)+'*'*i) for i in range(a,0,-1)]
