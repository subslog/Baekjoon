import sys

N = int(input())

for _ in range(N):
    string = sys.stdin.readline().split()

    for s in range(len(string)):
        string[s] = string[s][-1::-1]
    
    print(" ".join(string))