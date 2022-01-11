# A + B - 4
# 입력이 끝날 때까지 A+B를 출력하는 문제
# EOF
# 왜 EOF를 해주어야 하는가?
# 코드 동작 과정에서 오류를 컨트롤 해주기 위해 사용

# 풀이1
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 풀이2
# sys.stdin을 사용 -> ctrl+Z를 누르면 입력 종료된다
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
