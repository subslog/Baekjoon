def subsequence(index: int, sum):
    """부분 수열의 합이 S와 같은 경우의 수를 구하는 함수"""
    global ans
    # 재귀 종료 조건 : 수열의 마지막 인덱스까지 재귀 완료
    if index == N:
        # 정답 조건 : 부분 수열의 합이 S와 같으면 카운트
        if sum == S:
            ans += 1
        return
    # 선택하는 경우
    subsequence(index + 1, sum + arr[index])
    # 선택하지 않는 경우
    subsequence(index + 1, sum)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
subsequence(0, 0)
if S == 0: ans -= 1

print(ans)