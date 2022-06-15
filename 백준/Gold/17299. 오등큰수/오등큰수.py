N = int(input())

seq_list = list(map(int, input().split()))  # 수열
answer = ['-1'] * len(seq_list)             # 정답 리스트
stack = [0]                                 # 오등큰수를 찾지 못한 인덱스
seq_cnt = [0] * 1000001                     # 원소 카운트 리스트

# 원소 카운트
for seq in seq_list:
    seq_cnt[seq] += 1

for seq_idx in range(1, len(seq_list)):
    # stack의 top 인덱스의 수열 요소 수보다 현재 요소의 수가 많으면
    while stack and seq_cnt[seq_list[stack[-1]]] < seq_cnt[seq_list[seq_idx]]:
        # 정답 리스트의 인덱스에 현재 요소 업데이트 및 stack top 제거
        answer[stack.pop()] = str(seq_list[seq_idx])
    # 현재 요소의 오등큰수를 찾기 위해 push
    stack.append(seq_idx)

print(" ".join(answer))