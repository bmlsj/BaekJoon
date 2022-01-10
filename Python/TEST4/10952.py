# A + B - 5
# 0 0 이 들어올 때까지 A+B 출력

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)