# 초기값 입력
S = input()
T = list(input())

def string_check(s: str, lenth: int):
    """T가 S가 될 수 있는지 판단하는 함수"""
    # 길이가 같아지면 같은지 판단
    if len(S) == lenth:
        if S == ''.join(s):
            print(1)
            exit()
        return
    # 맨 오른쪽 인덱스의 문자가 A면 A 제거
    if s[-1] == 'A':
        string_check(s[:-1], lenth - 1)
    # 맨 왼쪽 인덱스의 문자가 B면 반전 후에 B 제거
    if s[0] == 'B':
        string_check(s[::-1][:-1], lenth - 1)

string_check(T, len(T))
print(0)