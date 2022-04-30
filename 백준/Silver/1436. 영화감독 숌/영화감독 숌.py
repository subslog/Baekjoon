N = int(input())

i = 1
num = 666

while i < N:
    num += 1
    if str(num).find('666') >= 0:
        i += 1

print(num)