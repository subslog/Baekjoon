import sys

N = int(input())
users = {}      # 사용자 덩치를 저장할 딕셔너리

# 사용자 덩치 입력
for i in range(N):
    users[i] = {'body': list(map(int, sys.stdin.readline().split())), 'rank': 1}

# 브루스 포스
for i in range(N):
    # 다른 사용자와 모두 비교
    for j in range(N):
        # 같은 사용자는 다음 반복으로
        if i == j:
            continue
        # 몸무게와 키가 둘 다 작으면 등수 +1
        elif users[i]['body'][0] < users[j]['body'][0] and users[i]['body'][1] < users[j]['body'][1]:
            users[i]['rank'] += 1

print(*[i['rank'] for i in users.values()])