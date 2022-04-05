def seq(max: int):
    '''n과 n의 각 자릿수를 더하는 함수'''
    
    # 셀프 넘버를 찾기 위한 리스트
    self_no = list(range(1, max))
    
    for i in range(1, max):
        seq_no = i  # 더한 결과값

        # 각 자릿수를 더한다.
        for j in str(i):
            seq_no += int(j)

        # 더한 결과값이 있으면 리스트에서 제거
        if seq_no in self_no:
            self_no.remove(seq_no)
            
    for no in self_no:
        print(no)

seq(10000)