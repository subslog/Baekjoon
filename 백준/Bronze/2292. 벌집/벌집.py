N = int(input())

room = 1
multiple = 0

while True:
    if N <= room:
        break
    multiple += 6
    room += multiple

print(multiple // 6 + 1)