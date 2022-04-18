N = int(input())

room = 1
multiple = 0

while N > room:
    multiple += 6
    room += multiple

print(multiple // 6 + 1)