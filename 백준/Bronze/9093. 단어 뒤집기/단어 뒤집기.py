import sys

N = int(input())

for _ in range(N):
    string = sys.stdin.readline()[::-1].split()
    
    string.reverse()
    
    print(" ".join(string))