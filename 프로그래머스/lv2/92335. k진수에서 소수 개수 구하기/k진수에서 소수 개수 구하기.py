import re

def solution(n, k):
    answer = 0
    
    # k진수로 변환(나눈 몫이 0이면 종료)
    change = ''
    while n != 0:
        # 나머지값
        change += str(n % k)
        # 몫
        n //= k
    # k진수 뒤집기
    change = change[::-1]
    # 0을 기준으로 숫자 분리
    num_list = map(int, re.findall('[1-9]+', change))

    # 모든 수를 소수인지 검사
    for num in num_list:
        if num <= 1: continue
        # num의 제곱근까지 검사
        for i in range(2, int(num ** 0.5) + 1):
            # 나누어 떨어지면 소수가 아니다.
            if num % i == 0:
                break
        else:
            # 소수면 갯수 +1
            answer += 1
    
    return answer