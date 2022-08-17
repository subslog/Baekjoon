def solution(s):
    answer = []
    s_list = [i.split(',') for i in s[2:-2].split('},{')]   # 특수 문제 제거
    s_list.sort(key=lambda x:len(x))                        # 길이 순으로 오름차순 정렬
    # 차집합 연산으로 튜플을 구한다.
    for i in s_list:
        temp = set(i) - set(answer)
        answer.append(list(temp)[0])
        
    return list(map(int, answer))