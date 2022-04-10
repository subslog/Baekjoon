def a_seq():
    '''한수를 구하는 함수'''
    c = 0   # 한수 카운트

    num = int(input())

    # 입력된 값만큼 반복
    for i in map(str, range(1, num + 1)):
        # 입력된 값의 길이만큼 반복
        for j in range(len(i), 0, -1):
            # 한 자리 또는 두 자리일 경우 한수
            if j in (1, 2):
                c += 1
                break
            # a + (a + 2n) = (a + n) / 2 아니면 한수 x 
            elif int(i[j - 1]) + int(i[j - 3]) != int(i[j - 2]) * 2:
                break
    
    print(c)

a_seq()