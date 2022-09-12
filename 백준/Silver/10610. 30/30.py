# 초기값 입력 및 내림차순 정렬
N = list(input())
N.sort(reverse=True)

# int 형으로 변환 후 30의 배수 검사
num = int(''.join(N))
if num % 30 == 0:
    print(num)
else:
    print(-1)