# 초기값 입력
S = input()
T = list(input())

# S -> T로 변경할 경우 2 ** 999 가지 경우의 수가 있어 풀이가 불가능
# T의 마지막 문자를 기준으로 역변환하여 S가 가능한지 확인
while len(T) > len(S):
    # T의 마지막 문자 제거
    temp = T.pop()
    # 마지막 문자가 B면 반전
    if temp == 'B':
        T.reverse()
        
# T의 문자와 S의 문자가 같으면 1, 다으면 0
if ''.join(T) == S:
    print(1)
else:
    print(0)