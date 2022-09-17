import sys
from collections import Counter

# 초기값 입력
N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]
# (요소, 개수) 튜플 변환
num_cnt = sorted(Counter(nums).most_common(), key=lambda x: (-x[1], x[0]))

print(num_cnt[0][0])