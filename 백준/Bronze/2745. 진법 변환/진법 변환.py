N, B = input().split()

answer = 0              # 10진수
squared = len(N) - 1    # 제곱

# 자리수마다 제곱 -1 하면서 연산
for i in N:
    # 알파벳이면 숫자로 변환해서 계산
    if i.isalpha():
        answer += (ord(i) - 55) * (int(B) ** squared)
    else:
        answer += int(i) * (int(B) ** squared)
    squared -= 1

print(answer)