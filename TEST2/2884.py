# 알람 시계
# - 45분 일찍 알람 설정하기

hour, min = input().split()
hour = int(hour)
min = int(min)

if hour == 0:
    if min >= 45:
        min -= 45
        print(hour, min)

    else:  # min < 45
        hour += 23
        min = (60 - (45 - min))
        print(hour, min)

else:
    if min >= 45:
        min -= 45
        print(hour, min)

    else:  # min < 45
        hour -= 1
        min = (60 - (45 - min))
        print(hour, min)
