N, M = map(int, input().split())

# 종이 수
paper = [list(map(int, input().split())) for _ in range(N)]
# 정답 리스트
answer = []

# 테트로미노 경우의 수
tetromino = [
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [0, 2], [0, 3]],
    [[0, 1], [1, 0], [1, 1]],
    [[0, 1], [0, 2], [1, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [1, -2]],
    [[1, 0], [2, 0], [2, 1]],
    [[1, 0], [1, 1], [1, 2]],
    [[0, 1], [1, 0], [2, 0]],
    [[0, 1], [0, 2], [1, 2]],
    [[1, 0], [2, 0], [2, -1]],
    [[0, 1], [-1, 1], [-1, 2]],
    [[1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 1], [1, 2]],
    [[1, 0], [1, -1], [2, -1]],
    [[1, 0], [1, -1], [2, 0]],
    [[1, 0], [1, -1], [1, 1]],
    [[1, 0], [2, 0], [1, 1]],
    [[0, 1], [0, 2], [1, 1]]
]

# 모든 경우의 수 반복
for i in range(N):
    for j in range(M):
        # paper[i][j]를 기준으로 테트로미노 놓을 수 있으면 answer에 추가
        for tet in tetromino:
            sum = paper[i][j]
            for point in range(3):
                x = i + tet[point][0]
                y = j + tet[point][1]
                if 0 <= x < N and 0 <= y < M: 
                    sum += paper[x][y]
                else:
                    break
            else:
                answer.append(sum)

print(max(answer))