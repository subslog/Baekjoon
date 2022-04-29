def fac(num):
    
    if num >= 2:
        result = num * fac(num - 1)
    else:
        result = 1

    return result

print(fac(int(input())))