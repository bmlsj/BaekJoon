# 최대값

num = []

for i in range(9):
    num.append(int(input()))

# print(max(num))
# print(num.index(max(num))+1)


max = num[0]

for i in range(1, 9):
    if max < num[i]:
        max = num[i]

print(max)
print(num.index(max)+1)