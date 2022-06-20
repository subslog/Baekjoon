import collections

answer = []                 # 정답 저장 리스트
deq = collections.deque()   # 문자열 저장 덱

deq += input()              # 문자열 덱에 저장

# 덱 요소가 없어질 때까지 반복
while deq:
    # 문자열 추가
    answer.append("".join(deq))
    # 문자열 왼쪽 1개 문자 제거
    deq.popleft()

# 오름차순 정렬
print("\n".join(sorted(answer)))