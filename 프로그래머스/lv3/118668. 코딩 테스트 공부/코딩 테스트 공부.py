INF = int(1e9)

def solution(alp, cop, problems):
    # 목표 알고력, 코딩력
    target_alp, target_cop = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        target_alp = max(target_alp, alp_req)
        target_cop = max(target_cop, cop_req)
    # 목표값보다 초기값이 더 높을 경우 예외 처리
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    # dp 테이블
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    # dp 초기값
    dp[alp][cop] = 0
    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            if i + 1 < target_alp:
                # 알고리즘 공부
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 < target_cop:
                # 코딩 공부
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
                # 풀 수 있는 문제를 문다
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    # 문제를 풀어서 알고력, 코딩력이 목표치를 넘어가지 않도록 한다.
                    n_alp = min(target_alp, i + alp_rwd)
                    n_cop = min(target_cop, j + cop_rwd)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[i][j] + cost)

    return dp[target_alp][target_cop]