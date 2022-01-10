# 오른쪽 정렬 별 찍기

n = int(input())

for i in range(1, 1 + n):
    print("%{}s".format(n) % ("*" * i))
