def solution(n, arr1, arr2):
    answer = []
    # 지도1과 지도2를 or 연산하여 결과에 따라 저장
    for i in range(n):
        # or 연산 후 0으로 자리수 채우기
        result = bin(arr1[i] | arr2[i]).lstrip('0b').rjust(n, '0').replace('1', '#').replace('0', ' ')
        answer.append(result)
        
    return answer