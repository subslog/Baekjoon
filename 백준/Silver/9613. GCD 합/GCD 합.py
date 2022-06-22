def euclidean(a: int, b: int) -> int:
    """유클리드 호제법"""

    if b == 0:
        return a
    
    return euclidean(b, a % b)

import sys

t = int(input())

for _ in range(t):
    
    answer= 0
    num_list = list(map(int, sys.stdin.readline().split()))[1:]

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            answer += euclidean(num_list[i], num_list[j])

    print(answer)