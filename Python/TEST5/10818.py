# 최소, 최대

# 내장 함수 사용
"""
num = int(input())
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list))
"""

# 내장 함수 사용x
num = int(input())
num_list = list(map(int, input().split()))
min = num_list[0]
max = num_list[0]

for i in num_list[1:]:

    if i > max:
        max = i;

    elif i < min:
        min = i


print(min, max)