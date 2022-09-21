
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
def solution(gems):
    answer = [1, len(gems)]
    # 보석을 키로 딕셔너리 생성
    gems_dict = dict()
    for gem in gems:
        if not gem in gems_dict:
            gems_dict[gem] = 0
    # 보석 개수
    gem_cnt = len(gems_dict)
    # 모든 보석을 확인
    start, end = 0, 0
    cnt = 0             # 수집된 보석 수
    result = len(gems)  # 구간 길이
    for gem in gems:
        # 처음으로 포함되는 보석이면 수집된 보석 수 증가
        if gems_dict[gem] == 0:
            cnt += 1
        # 보석을 추가하고 end를 증가한다.
        gems_dict[gem] += 1
        end += 1
        # start 위치의 보석이 2개 이상 포함되어 있으면 시작 위치를 증가한다.
        for i in range(start, end):
            if gems_dict[gems[start]] > 1:
                gems_dict[gems[start]] -= 1
                start += 1
            else:
                break
        # 모든 보석이 수집되고, 최소 구간이면 구간 갱신
        if cnt == gem_cnt and end - start < result:
            result = end - start
            answer = [start + 1, end]

    return answer