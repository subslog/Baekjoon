def subsequence(index: int, sum: int):
    """부분 수열의 합을 구하는 함수"""
    # 종료 조건 : 마지막 인덱스까지 재귀 완료
    if index == N:
        # 부분 수열의 합 True 처리
        check[sum] = True
        return

    # 선택하는 경우
    subsequence(index + 1, sum + S[index])
    # 선택하지 않는 경우
    subsequence(index + 1, sum)

N = int(input())
S = list(map(int, input().split()))
check = [True] + [False] * (sum(S) + 1) # 부분 수열의 합 체크용
subsequence(0, 0)
# 첫 번째로 반환되는 인덱스가 부분 수열의 합으로 나올 수 없느 가장 작은 자연수
ans = check.index(False)
print(ans)