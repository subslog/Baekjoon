def seq(max: int):
    '''셀프 넘버를 찾는 함수'''

    # 1 ~ max - 1 까지의 range
    max_rang = range(1, max)

    # n과 n의 각 자릿수를 더한 결과 리스트
    self_no = [i + sum(map(int, str(i))) for i in max_rang]
    
    print(*sorted(set(max_rang) - set(self_no)))

seq(10000)