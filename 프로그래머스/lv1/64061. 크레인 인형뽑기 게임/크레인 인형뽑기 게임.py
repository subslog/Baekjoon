def solution(board, moves):
    answer = 0
    # 뽑은 인형을 담을 리스트
    basket = []
    # 인형을 뽑는다.
    for move in moves:
        # 인형이 나올 때까지 크레인을 내린다.
        for depth in range(len(board)):
            # 인형이 나오면 뽑는다.
            if 0 < board[depth][move - 1]:
                basket.append(board[depth][move - 1])
                board[depth][move - 1] = 0
                # 인형이 2개 이상이고, 같은 인형이 연속되면 터트린다.
                if 2 <= len(basket) and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                # 다음 크레인 위치로 이동
                break
        
    return answer