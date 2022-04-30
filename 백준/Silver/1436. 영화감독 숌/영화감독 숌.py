import re

N = int(input())

i = 1
num = 666

while i < N:
    num += 1
    if re.search('6{3,}', str(num)):
        i += 1

print(num)