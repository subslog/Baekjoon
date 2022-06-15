import collections

N, K = map(int, input().split())

seq_queue = collections.deque(map(str, range(1, N + 1)))
move = K - 1
answer = []

while seq_queue:
    seq_queue.rotate(-move)
    answer.append(seq_queue.popleft())

print(f"<{', '.join(answer)}>")