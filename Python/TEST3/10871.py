# X보다 작은 수

N, X = map(int, input().split())
min = list(map(int, input().split()))

for i in range(N):
    if min[i] < X:
        print(min[i], end=' ')
    else:
        continue
