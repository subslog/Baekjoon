# M과 K로 가능한 N의 최소 길이 : N >= M + K - 1
# N=4, M=3, K=2 일 때 1, 2, 4, 3 과 같이 계속 증가, 계속 감속하는 수열이 하나의 요소를 공유할 수 있다.
# 그렇기 때문에 N은 최소 M + K - 1을 만족해야 된다.
# N의 최대 길이 : N <= MK
# 1~N까지 M 개의 그룹으로 나눈다. (각 그룹을 reverse하면 각 그룹의 요소가 증가하는 부분 수열이 된다.)
# 적어도 1개의 그룹에는 K 개의 요소가 있어야 한다.
# 나머지 그룹은 K보다 작거나 같아야 한다.
# 예시(N=13, M=5, K=4)
# 수열 : 1 2 3 4 5 6 7 8 9 10 11 12 13
# 수열을 M 개의 그룹으로 나눈다.(하나의 그룹에는 K 개의 요소가 있어야 한다.)
# 수열 : [1, 2, 3, 4], [5, 6], [7, 8], [9, 10], [11, 12, 13]
# 각 그룹을 reverse 한다.
# 수열 : [4, 3, 2, 1], [6, 5], [8, 7], [10, 9], [13, 12, 11]
# 각 그룹에서 숫자를 하나씩 뽑으면 증가하는 부분 수열의 길이 M을 만족한다.
# 첫 번째 그룹에서 감소하는 부분 수열의 길이 K를 만족한다.

# 초기값 입력
N, M, K = map(int, input().split())

if M + K - 1 <= N <= M * K:
    answer = [i for i in range(1, N + 1)]   # 1~N까지 수열 생성
    group_line = [0, K]                     # 각 그룹의 범위를 저장(K 개를 먼저 선택)
    N -= K                                  # N에서 K 개를 뺀다.
    M -= 1                                  # 그룹을 1 개 뺀다.
    group_cnt = 0 if M == 0 else N // M     # 나머지 그룹에 들어가는 개수
    remainder = 0 if M == 0 else N % M      # 나머지 그룹에 1 개씩 넣어줄 나머지 값
    # 그룹 생성
    for i in range(M):
        # 마지막 범위에서 그룹의 수만큼 추가하여 범위 추가
        group_line.append(group_line[-1] + group_cnt)
        # 나머지 값이 있으면 +1 해주고 나머지 값을 1 감소한다.
        if remainder > 0:
            group_line[-1] += 1
            remainder -= 1
    # 그룹의 범위만큼 reverse 수행
    for i in range(len(group_line) - 1):
        start, end = group_line[i], group_line[i + 1]
        answer[start:end] = reversed(answer[start:end])

    print(*answer)
else:
    print(-1)