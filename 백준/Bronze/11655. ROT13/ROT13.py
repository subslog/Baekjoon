S = input()

answer = ""

for i in S:
    # 아스키 코드 변환
    ascii = ord(i)
    # 대문자 변환
    if 65 <= ascii <= 77:
        answer += chr(ascii + 13)
    # 대문자 변환(13 더해서 아스키 코드가 90 초과)
    elif 78 <= ascii <= 90:
        answer += chr(ascii - 13)
    # 소문자 변환
    elif 97 <= ascii <= 109:
        answer += chr(ascii + 13)
    # 소문자 변환(13 더해서 아스키 코드가 122 초과)
    elif 110 <= ascii <= 122:
        answer += chr(ascii - 13)
    else:
        answer += i

print(answer)