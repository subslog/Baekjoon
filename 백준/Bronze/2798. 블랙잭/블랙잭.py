import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

combination = list(itertools.combinations(cards, 3))
temp = M

for i in combination:
    com_sum = sum(i)
    if M - com_sum >= 0 and M - com_sum < temp:
        temp = M - com_sum
        result = com_sum

print(result)