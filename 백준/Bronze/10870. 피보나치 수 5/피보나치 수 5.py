def fibonacci(num):
    
    if num >= 2:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    elif num == 1:
        result = 1
    else:
        result = 0

    return result

print(fibonacci(int(input())))