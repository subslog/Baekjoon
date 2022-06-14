import sys

N = int(input())

for _ in range(N):
    ps = sys.stdin.readline().strip('\n')
    
    cnt = 0

    for s in ps:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            print("NO")
            break
    else:
        if cnt == 0:
            print("YES")
        else:
            print("NO")