# 더하기 싸이클

num = int(input())
check = num
new_num = 0
cycle = 0

while True:
    sum = (num // 10) + (num % 10)  # 2 + 6 / sum = 8
    new_num = (num % 10) * 10 + (sum % 10)  # 68
    cycle += 1
    num = new_num
    if new_num == check:
        break

print(cycle)

"""
a, b, c = -1, -1, -1
cycle = 0

a = int(input())
b = a

while c != a:
    c = (b % 10) * 10 + (((b // 10) + (b % 10)) % 10)
    cycle += 1
    b = c

print(cycle)
"""