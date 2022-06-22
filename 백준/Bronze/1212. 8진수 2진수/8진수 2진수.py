binary = ["000", "001", "010", "011", "100", "101", "110", "111"]

num = input()
start = True    # 맨 앞 숫자 확인용
answer = ""     # 정답

if num == "0":
    answer = "0"

for n in num:
    n = int(n)
    if start and n < 4:
        if n == 1:
            answer += "1"
        elif n == 2:
            answer += "10"
        elif n == 3:
            answer += "11"
        start = False
    else:
        answer += binary[n]
        start = False

print(answer)