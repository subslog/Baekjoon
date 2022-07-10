import sys

nine = []

# 9명 키 저장
for _ in range(9):
    stature = int(input())
    nine.append(stature)

nine.sort()             # 키 오름차순 정렬
nine_sum = sum(nine)    # 9명 키의 합

for i in range(9):
    for j in range(i + 1, 9):
        # 두 명의 키를 뺏을 때 100이면
        if nine_sum - nine[i] - nine[j] == 100:
            # 나머지 7명의 키 출력
            for z in range(9):
                if z == i or z == j: continue
                
                print(nine[z])
            # 종료
            sys.exit(0)