X = int(input())

an = 1     # 수열 an
b = 2     # 증가 값

# 입력값이 수열 an보다 작거나 같을 때까지 반복
while X > an:
    an += b    # 계차수열만큼 증가
    b += 1    # 계차수열(+1)

sub = an - X   # 수열 an - 입력값
n = b - 1     # n 번째

# n이 홀수
if n % 2 == 1:
    print(f'{1 + sub}/{n - sub}')
# 짝수
else:
    print(f'{n - sub}/{1 + sub}')