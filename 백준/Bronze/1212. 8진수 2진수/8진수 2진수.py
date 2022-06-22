def binary(num: str) -> str:
    """8진수 -> 2진수 변환"""

    num = int(num)
    binary = ""

    while num > 1:
        binary += str(num % 2)  # 2로 나눈 나머지
        num = num // 2          # 2로 나눈 몫
    
    binary += str(num)

    return binary[::-1].rjust(3, "0")

num = input()
answer = ""

for i in num:
    answer += binary(i)

if answer == "000":
    print(0)
else:
    print(answer.lstrip("0"))