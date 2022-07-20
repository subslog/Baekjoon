def go(index: int) -> list:
    """부등호 관계를 만족하는 수 반환 함수"""
    
    # 부등호 관계를 만족하는 수
    if index == k + 1:
        answer.append("".join(map(str, num_list)))
        return
    # 다음 비교 진행
    for i in range(10):
        if check[i]: continue   # 사용 중이면 반복 건너뛰기
        # 백트랙킹(조건을 만족할 때만 다음 재귀 진행)
        if index == 0 or symbol[index - 1] == "<" and num_list[index - 1] < i or symbol[index - 1] == ">" and num_list[index - 1] > i:
            num_list[index] = i
            check[i] = True
            go(index + 1)
            check[i] = False

k = int(input())
symbol = input().split()    # 부등호 리스트
check = [False] * 10        # 중복 확인
num_list = [0] * (k + 1)    # 부등호 관계 만족하는 수 저장
answer = []                 # 부등호 관계 만족하는 수 리스트
go(0)

print(max(answer))
print(min(answer))