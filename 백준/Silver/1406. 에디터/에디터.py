import sys

# 커서를 기준으로 스택을 왼쪽, 오른쪽으로 나눈다.
string_left = list(input())
string_right = []
N = int(input())

for _ in range(N):
    commend = sys.stdin.readline().split()

    # L이면 왼쪽 스택에서 오른쪽 스택으로 pop
    if commend[0] == "L" and len(string_left) > 0:
        string_right.append(string_left.pop())
    # D이면 오른쪽 스택에서 왼쪽 스택으로 pop
    elif commend[0] == "D" and len(string_right) > 0:
        string_left.append(string_right.pop())
    # B면 왼쪽 스택에서 마지막 요소 삭제
    elif commend[0] == "B" and len(string_left) > 0:
        string_left.pop()
    # P면 왼쪽 스택의 마지막 요소에 추가
    elif commend[0] == "P":
        string_left.append(commend[1])

string_right.reverse()
print("".join(string_left + string_right))