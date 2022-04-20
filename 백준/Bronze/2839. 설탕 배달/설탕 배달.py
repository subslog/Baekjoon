# 다이나믹 프로그래밍
# 탐욕 알고리즘

N = int(input())

five = N // 5       # 5kg을 최대로 시작
grid = []

# 5kg이 0될 때까지 하나씩 줄이며 반복
for i in range(five, -1, -1):

    # 3kg 개수
    three = (N - i * 5) // 3
    # 설탕 봉지 개수
    origin = i * 5 + three * 3
    # 배달할 설탕과 설탕 봉지 개수가 같으면
    if N == origin:
        # 봉지의 개수를 리스트에 추가
        grid.append(i + three)

# 리스트에 봉지가 있으면 
if len(grid):
    # 제일 적은 봉지 출력
    print(min(grid))
# 봉지가 없으면 -1 출력
else:
    print(-1)