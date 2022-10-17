# 초기값 입력
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 내림차순, B는 오름차순 정렬
A.sort()
B.sort(reverse=True)

# A 최소값, B 최대값부터 곱하면 최소값이다.
answer = 0
for i in range(N):
    answer += A[i] * B[i]

print(answer)