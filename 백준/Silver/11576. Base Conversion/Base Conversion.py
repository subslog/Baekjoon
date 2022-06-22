A, B = map(int, input().split())
N = int(input())
num = map(int, input().split())

dec = 0             # 10진수
squared = N - 1     # 제곱
answer = []         # 정답

# 10진수 변환
for i in num:
    dec += i * (A ** squared)
    squared -= 1

# B진수 변환
while dec > 0:
    answer.append(dec % B)  # 나머지
    dec = dec // B          # 몫

print(*answer[::-1])