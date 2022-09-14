def Z(num: int, x: int, y: int):
    """r, c의 순서를 반환하는 함수"""
    # x, y를 찾으면 반환
    if num == 1:
        return 2 * x + y

    # x, y 위치에 따라 제2사분면으로 만들기 위한 값
    quadrant2 = pow(2, num - 1)
    if x < quadrant2:
        # 제2사분면에 있으면 그대로 사용
        if y < quadrant2:
            return Z(num - 1, x, y)
        # 제1사분면에 있으면 y를 감소시켜 제2사분면으로 만든다.(제1사분면의 시작값을 더해준다.)
        else:
            return Z(num - 1, x, y - quadrant2) + pow(2, 2 * num - 2)
    else:
        # 제3사분면에 있으면 x를 감소시켜 제2사분면으로 만든다.(제3사분면의 시작값을 더해준다.)
        if y < quadrant2:
            return Z(num - 1, x - quadrant2, y) + pow(2, 2 * num - 2) * 2
        # 제4사분면에 있으면 x, y를 감소시켜 제2사분면으로 만든다.(제4사분면의 시작값을 더해준다.)
        else:
            return Z(num - 1, x - quadrant2, y - quadrant2) + pow(2, 2 * num - 2) * 3

# 초기값 입력
N, r, c = map(int, input().split())

print(Z(N, r, c))