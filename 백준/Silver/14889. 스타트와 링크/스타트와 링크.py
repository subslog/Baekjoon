def team_match(idx, start):
    """두 팀의 능력치가 최소인 값을 반환하는 함수"""
    # 팀 인원이 맞으면 팀 능력치 계산 후 재귀 종료
    if idx == N // 2:
        team_l = list(set(team_all) - set(team_s))  # link 팀 멤버
        sum_s = sum_l = 0                           # 각 팀 능력치
        # start, link 팀의 능력치 계산
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                sum_s += S[team_s[i]][team_s[j]] + S[team_s[j]][team_s[i]]
                sum_l += S[team_l[i]][team_l[j]] + S[team_l[j]][team_l[i]]
        # 정답 리스트에 추가
        answer.append(abs(sum_s - sum_l))
        return

    for i in range(start, N):
        team_s[idx] = i             # 팀원 뽑기
        team_match(idx + 1, i + 1)  # 다음 팀원 뽑기

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
team_all = list(range(N))
team_s = [0] * (N // 2)
answer = []

team_match(0, 0)
print(min(answer))