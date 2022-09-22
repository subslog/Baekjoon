def open_check(key: list, key_position: list, lock: list, lock_position: list) -> bool:
    """자물쇠 오픈 체크 함수"""
    key_size = len(key)
    lock_size = len(lock)
    for i in range(lock_size - key_size + 1):
        for j in range(lock_size - key_size + 1):
            for k in key_position:
                x, y = k
                # key의 돌기와 자물쇠의 돌기가 만나면 자물쇠 오픈 불가
                if lock[i + x][j + y] == 1:
                    break
            # key의 돌기가 자물소의 돌기와 만나지 않으면 열리는지 확인
            else:
                for l in lock_position:
                    x, y = l
                    # key의 돌기와 자물소의 홈이 만나지 않으면 오픈 불가
                    if x - i < 0 or x - i >= key_size or y - j < 0 or y - j >= key_size or key[x - i][y - j] != 1:
                        break
                # key의 돌기와 자물소의 홈이 만나면 오픈
                else:
                    return True
    return False

def arr_rotate(arr: list):
    """배열을 시계 방향으로 90도 회전하고, key의 돌기를 찾는 함수"""
    arr_size = len(arr)
    rotate = [[arr[j][i] for j in range(arr_size - 1, -1, -1)]for i in range(arr_size)]
    key_position = [(i, j) for i in range(arr_size) for j in range(arr_size) if rotate[i][j] == 1]

    return rotate, key_position

def solution(key, lock):
    # key의 돌기 위치를 찾는다.
    key_size = len(key)
    key_position = [(i, j) for i in range(key_size) for j in range(key_size) if key[i][j] == 1]
    # 자물쇠 크기를 key의 크기 - 1 만큼 상, 하, 좌, 우로 크기를 늘린다.
    lock_size = len(lock)
    for i in range(lock_size):
        lock[i] = [-1] * (key_size - 1) + lock[i] + [-1] * (key_size - 1)
    for _ in range(key_size - 1):
        lock.insert(0, [-1] * (lock_size + (key_size - 1) * 2))
        lock.append([-1] * (lock_size + (key_size - 1) * 2))
    # 자물쇠의 홈 위치를 찾는다.
    lock_size += key_size - 1
    lock_position = [(i, j) for i in range(lock_size) for j in range(lock_size) if lock[i][j] == 0]

    # 자물쇠 열 수 있는지 확인
    for _ in range(4):
        # 열 수 있으면 True 반환
        if open_check(key, key_position, lock, lock_position):
            return True
        # 시계 방향으로 90도 회전
        key, key_position = arr_rotate(key)

    return False