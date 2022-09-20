def solution(files):
    answer = []
    # 파일명 파싱
    parsing = []
    for idx, file in enumerate(files):
        start = 0   # 숫자 처음 나온 위치
        end = 0     # 숫자 두 번째 나온 위치
        for i in range(len(file)):
            # 첫 번째 숫자 인덱스 저장
            if file[i].isdigit():
                start = i
                end = i + 1
                # 두 번째 숫자 인덱스 젖장
                for j in range(i + 1, len(file)):
                    if file[j].isdigit():
                        end = j + 1
                    else:
                        break
                break 
        # 튜플로 HEAD, NUMBER, index, TAIL 순으로 저장
        parsing.append((file[:start], file[start:end], idx, file[end:]))
    # 오름차순 정렬
    parsing.sort(key=lambda x: (x[0].upper(), int(x[1]), x[2]))
    # 정답 저장
    for p in parsing:
        answer.append(p[0] + p[1] + p[3])

    return answer