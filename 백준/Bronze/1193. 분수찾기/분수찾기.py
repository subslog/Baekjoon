X = int(input())

an = 1     # 수열 an
b = 1     # 증가 값

# 입력값이 수열 an보다 작거나 같을 때까지 반복
while X > an:
    b += 1    # 계차수열(+1)
    an += b    # 계차수열만큼 증가

sub = an - X   # 수열 an - 입력값

# b가 홀수
if b % 2 == 1:
    print(f'{1 + sub}/{b - sub}')
# 짝수
else:
    print(f'{b - sub}/{1 + sub}')