import sys

# 초기값 입력
N = int(input())
num_list = []
minus_list = []
one_count = 0
zero = True
# 각 조건에 만족하는 숫자 처리
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        num_list.append(num)
    elif num == 1:
        one_count += 1
    elif num == 0:
        zero = False
    else:
        minus_list.append(num)
# 양수는 내림차순, 음수는 오름차순 정렬
num_list.sort(reverse=True)
minus_list.sort()

# 최대값을 구하는 연산 수행
# 높은 수끼리 곱하여 더한다.(음수)
minus_num = 0
for i in range(1, len(minus_list), 2):
    minus_num += minus_list[i - 1] * minus_list[i]
# 0이 없고, 수의 개수가 홀수면 마지막 요소를 더한다.
if zero and len(minus_list) % 2 == 1:
    minus_num += minus_list[-1]
# 높은 수끼리 곱하여 더한다.(양수)
cal_num = 0
for i in range(1, len(num_list), 2):
    cal_num += num_list[i - 1] * num_list[i]
# 수의 개수가 홀수면 마지막 요소를 더한다.
if len(num_list) % 2 == 1:
    cal_num += num_list[-1]

# 정답 계산
answer = cal_num + minus_num + one_count
print(answer)