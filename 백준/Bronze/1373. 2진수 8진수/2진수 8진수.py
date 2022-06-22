def octal(num: str) -> str:
    """2진수 -> 8진수 변환"""

    exponentiation = 1  # 거듭제곱
    oct = 0             # 8진수

    for n in num:
        oct += int(n) * exponentiation
        exponentiation *= 2
    
    return str(oct)

num = input()[::-1]
answer = ""

for i in range(0, len(num), 3):
    answer += octal(num[i:i + 3])

print(answer[::-1])