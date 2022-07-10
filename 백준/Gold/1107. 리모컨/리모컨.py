def button_check(num: int) -> bool:
    """고장난 버튼 확인 함수"""
    len = 0     # 버튼 누르는 횟수
    # 숫자가 0일 경우
    if num == 0:
        if button[0]:
            return 0
        else:
            return 1

    while num > 0:
        # 고장난 버튼이 있으면 False 반환
        if button[num % 10]:
            return 0
        num //= 10
        len += 1

    return len

N = int(input())        # 목표 채널
M = int(input())        # 고장난 버튼 수

button = [False] * 10   # False면 정상 버튼
# 고장난 버튼 처리
if M:
    broken = map(int, input().split())
    for i in broken:
        button[i] = True

answer = [abs(N - 100)] # 100에서 직접 하나씩 이동
num_small = 1000000     # N보다 작은 채널
num_big = 1000000       # N보다 큰 채널

# N보다 작은 채널 확인
for i in range(N, -1, -1):
    len = button_check(i)
    if len:
        answer.append(abs(N - i) + len)
        break
# N보다 큰 채널 확인
for i in range(N, 1000001):
    len = button_check(i)
    if len:
        answer.append(abs(N - i) + len)
        break

print(min(answer))