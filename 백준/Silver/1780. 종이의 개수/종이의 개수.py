import sys

def paper_cut(x: int, y: int, lenth: int):
    """x, y에서 lenth만큼 종이를 확인"""
    # 함수를 이용해 종이의 숫자 확인
    paper_check = set()
    for i in range(x, x + lenth):
        for j in range(y, y + lenth):
            paper_check.add(paper[i][j])
    # 길이가 1이면 하나의 숫자로만 이루어진 종이다.
    if len(paper_check) == 1:
        answer[list(paper_check)[0]] += 1
        return
    # 하나의 숫자로 이루어진 종이가 아니면 9등분 한다.
    cut_lenth = lenth // 3
    for i in range(x, x + lenth, cut_lenth):
        for j in range(y, y + lenth, cut_lenth):
            paper_cut(i, j, cut_lenth)

# 초기값 입력
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 정답 저장용 사전
answer = {-1:0, 0:0, 1:0}

paper_cut(0, 0, N)
for i in answer:
    print(answer[i])