cut_position = input()

cnt = 0     # 자를 때 추가할 파이프 수
answer = 0  # 결과 저장

for pipe in cut_position:
    if pipe == "(":
        cnt += 1            # 파이프 수 +1
        laser = True        # ) 나오면 레이저 체크용
    elif pipe == ")":
        if laser:           # 레이저로 절단
            cnt -= 1        # 파이프 수에서 레이저 ( -1
            answer += cnt   # 파이프 cnt 만큼 추가
            laser = False   # ( 나올 때까지 레이저는 안나온다.
        else:               # 파이프 끝
            cnt -= 1        # 파이프 수 -1
            answer += 1     # 파이프 1만큼 추가

print(answer)