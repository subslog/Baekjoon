x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    other = x3, y3
    if y1 > y2:
        top = [x1, y1]
        down = [x2, y2]
    elif y1 < y2:
        top = [x2, y2]
        down = [x1, y1]
elif x1 == x3:
    other = x2, y2
    if y1 > y3:
        top = [x1, y1]
        down = [x3, y3]
    elif y1 < y3:
        top = [x3, y3]
        down = [x1, y1]
elif x2 == x3:
    other = x1, y1
    if y2 > y3:
        top = [x2, y2]
        down = [x3, y3]
    elif y2 < y3:
        top = [x3, y3]
        down = [x2, y2]

if top[1] == other[1]:
    if top[0] > other[0]:
        result = [other[0], down[1]]
    elif top[0] < other[0]:
        result = [other[0], down[1]]
elif down[1] == other[1]:
    if top[0] > other[0]:
        result = [other[0], top[1]]
    elif top[0] < other[0]:
        result = [other[0], top[1]]

print(*result)