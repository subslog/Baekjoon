x, y, w, h = map(int, input().split())

right = w - x
left = x
top = h - y
down = y

print(min(right, left, top, down))