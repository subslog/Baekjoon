# 초기값 입력
N, M, K = map(int, input().split())

# 현재 만들 수 있는 팀 수
girl = N // 2
man = M
team_cnt = min(girl, man)
# 현재 여유 있는 학생 수
other = (N - team_cnt * 2) + (M - team_cnt)
# 여유 있는 학생들을 인턴쉽에 보낸다.
internship = other - K
# 인턴쉽에 보낼 학생이 부족하면 팀 구성에서 뺀다.
if internship < 0:
    team_cnt += -((abs(internship) - 1) // 3 + 1)

print(team_cnt)