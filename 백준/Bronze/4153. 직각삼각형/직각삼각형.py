while True:
    line = list(map(int, input().split()))

    if sum(line) == 0:
        break

    diagonal = max(line)
    line.remove(diagonal)

    if (line[0] ** 2 + line[1] ** 2) ** 0.5 == diagonal:
        print('right')
    else:
        print('wrong')