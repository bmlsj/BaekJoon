# 숫자의 개수

a = []
for i in range(3):
    a.append(int(input()))

result = a[0] * a[1] * a[2]

# 문자로 인식해서 리스트에 넣고 비교하기
result_list = [int(i) for i in str(result)]

count = []
for i in range(10):
    if result_list.count(i) == 0:
        count.insert(i, 0)
    else:
        count.insert(i, result_list.count(i))
    print(count[i])

