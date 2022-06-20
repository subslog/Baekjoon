while True:
    # 정답 저장 리스트(소문자, 대문자, 숫자, 공백)
    answer = [0] * 4

    try:
        string = input()
        # 문자열 분
        for s in string:
            # 아스키 코드 변환
            ascii = ord(s)
            # 소문자 카운트
            if 97 <= ascii <= 122:
                answer[0] += 1
            # 대문자 카운트
            elif 65 <= ascii <= 90:
                answer[1] += 1
            # 숫자 카운트
            elif 48 <= ascii <= 57:
                answer[2] += 1
            # 공백 카운트
            elif ascii == 32:
                answer[3] += 1
        
        print(*answer)

    except:
        break