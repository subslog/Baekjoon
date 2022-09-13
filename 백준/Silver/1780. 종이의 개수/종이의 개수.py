import sys

def paper_cut(arr: list, lenth: int):
    """-1, 0, 1 종이의 수를 카운트 하는 함수"""
    # 함수를 이용해 종이의 숫자 확인
    paper_check = set()
    for i in range(lenth):
        for j in range(lenth):
            paper_check.add(arr[i][j])
    # 길이가 1이면 하나의 숫자로만 이루어진 종이다.
    if len(paper_check) == 1:
        answer[list(paper_check)[0]] += 1
        return
    # 하나의 숫자로 이루어진 종이가 아니면 9등분 한다.
    cut_lenth = lenth // 3
    for i in range(0, lenth, cut_lenth):
        for j in range(0, lenth, cut_lenth):
            temp = []
            # 1/3 행렬 생성하여 재귀
            for row in range(i, i + cut_lenth):
                temp.append(arr[row][j:j + cut_lenth])
            paper_cut(temp, cut_lenth)

# 초기값 입력
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 정답 저장용 사전
answer = {-1:0, 0:0, 1:0}

paper_cut(paper, N)
for i in answer:
    print(answer[i])