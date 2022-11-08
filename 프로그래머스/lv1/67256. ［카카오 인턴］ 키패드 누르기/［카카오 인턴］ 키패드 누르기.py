def solution(numbers, hand):
    answer = ''
    
    # 숫자에 따라 누를 손가락
    touch_hand = {1:'left', 4:'left', 7:'left', 3:'right', 6:'right', 9:'right'}
    # 키패드 좌표
    keypad = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    # 엄지손가락 위치
    hand_position = {'left':(3, 0), 'right':(3, 2)}
    
    # 숫자를 누른다.
    for number in numbers:
        # 숫자가 1, 3, 4, 6, 7, 9이면 그에 맞는 손으로 누른다.
        if number in touch_hand:
            answer += touch_hand[number][0].upper()
            hand_position[touch_hand[number]] = keypad[number]
        # 숫자가 2, 5, 8, 0이면
        else:
            # 왼손과 키패드의 맨하튼 거리
            left_dist = abs(hand_position['left'][0] - keypad[number][0]) + abs(hand_position['left'][1] - keypad[number][1])
            # 오른손과 키패드의 맨하튼 거리
            right_dist = abs(hand_position['right'][0] - keypad[number][0]) + abs(hand_position['right'][1] - keypad[number][1])
            # 왼손이 더 가까우면 왼손으로 누른다.
            if left_dist < right_dist:
                answer += 'L'
                # 왼손 위치 변경
                hand_position['left'] = keypad[number]
            # 오른손이 더 가까우면 오른손으로 누른다.
            elif left_dist > right_dist:
                answer += 'R'
                # 오른손 위치 변경
                hand_position['right'] = keypad[number]
            # 같으면 본인 손잡이로 누른다.
            else:
                answer += hand[0].upper()
                # 손 위치 변경
                hand_position[hand] = keypad[number]
        
    return answer