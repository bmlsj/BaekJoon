# 빠른 A+B
# sys.stdin.readline 사용
# - 반복문으로 여러줄을 입력 받아야 할때 input()은 시간초과

import sys

num = int(input())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    sum = a+b
    print(sum)

