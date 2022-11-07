def solution(s):
    answer = s
    # 영단어에 매핑되는 숫자
    numbers = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    # 영단어에 매핑되는 숫자로 변경
    for number in numbers:
        answer = answer.replace(number, numbers[number])
        
    return int(answer)