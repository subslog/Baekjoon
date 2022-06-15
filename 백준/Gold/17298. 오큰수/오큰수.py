N = int(input())

seq_list = list(map(int, input().split()))  # 수열
answer = [-1] * len(seq_list)               # 정답 리스트
stack = [0]                                 # 오큰수를 찾지 못한 인덱스

for seq_idx in range(1, len(seq_list)):
    # stack 인덱스가 있고, 수열의 인덱스 값보다 현재 인덱스의 값이 크면
    while len(stack) and seq_list[stack[-1]] < seq_list[seq_idx]:
        # 정답 리스트의 인덱스에서 오큰수로 업데이트
        answer[stack[-1]] = seq_list[seq_idx]
        # stack top 제거
        stack.pop()
    # 다음 반복 때 오큰수를 찾을 인덱스 stack에 추가
    stack.append(seq_idx)

for i in answer:
    print(i, end=" ")