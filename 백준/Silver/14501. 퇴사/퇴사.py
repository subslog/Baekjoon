def working(day, sum):
    """최대 금액을 반환하는 함수"""
    if day == N:
        answer.append(sum)
        return
    if day > N:
        return

    working(day + T_P[day][0], sum + T_P[day][1])
    working(day + 1, sum)

N = int(input())
T_P = [list(map(int, input().split())) for _ in range(N)]
answer = []

working(0, 0)
print(max(answer))