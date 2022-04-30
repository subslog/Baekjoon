def decompose(N):
    # 생성자의 최대 자릿수
    gener= 9 * len(str(N))

    # N이 gener보다 작아 음수가 되는 케이스 처리
    if N > gener:        
        result = N - gener
    else:
        result = 0

    # N - result ~ N 사이에 생성자가 있다.
    while result < N:
        # 생성자의 각 자리수를 담을 리스트
        num_list =[]
        # 생성자 리스트 생성
        for i in str(result):
            num_list += [int(i)]
        # 생성자와 각 자리수의 합이 N과 같으면 생성자다.
        if N == result + sum(num_list):
            return result
        # 생성자가 아니므로 +1
        result += 1
    # 생성자가 없으면 0 반환
    else:
        return 0
    
print(decompose(int(input())))