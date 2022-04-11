dial = [['C', 3], ['F', 4], ['I', 5], ['L', 6], ['O', 7], ['S', 8], ['V', 9], ['Z', 10]]

word = input()

time = 0

for i in word:
    for j in dial:
        if i <= j[0]:
            time += j[1]
            break

print(time)