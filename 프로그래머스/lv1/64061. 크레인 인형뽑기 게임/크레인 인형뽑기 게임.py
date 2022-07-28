def solution(board, moves):
    answer = 0
    basket = []

    # 인형 뽑기
    for move in moves:
        # move - 1 열에서 반복
        for i in range(len(board)):
            # 인형이 있으면
            if board[i][move - 1] != 0:
                # 바구니에 담기
                basket.append(board[i][move - 1])
                # 인형 제거
                board[i][move - 1] = 0
                # 바구니에 똑같은 인형이 있으면 점수 +2
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                # 다음 뽑기 진행
                break
    
    return answer