def star(num):
    if num == 1:
        return ['*']
    
    stars = star(num // 3)
    result = []

    for i in stars:
        result += [i * 3]
    for i in stars:
        result += [i + ' ' * (num // 3) + i]
    for i in stars:
        result += [i * 3]

    return result

print('\n'.join(star(int(input()))))