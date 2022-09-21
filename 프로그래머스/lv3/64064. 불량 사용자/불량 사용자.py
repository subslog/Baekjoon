from itertools import combinations, permutations
import re

def solution(user_id, banned_id):
    answer = 0
    # 불량 사용자 수
    banned_len = len(banned_id)
    # 정규표현식 *을 모든 알파벳으로 비교하기 위해 치환
    for i in range(banned_len):
        banned_id[i] = banned_id[i].replace('*', '[a-z0-9]')
    # 비교할 수 있는 모든 사용자 조합
    user_combi = list(combinations(user_id, banned_len))
    # 모든 사용자 조합에서 제재 아이디를 찾기 위한 순열
    banned_per = list(permutations(banned_id, banned_len))
    # 제재 아이디 목록 경우의 수 구하기
    for user in user_combi:
        for banned in banned_per:
            for i in range(banned_len):
                # 불일치 경우가 있으면 현재 검사 종료
                if not re.match('^' + banned[i] + '$', user[i]):
                    break
            # 일치하는 경우가 나오면 경우의 수를 증가하고, 해당 사용자 조합의 검사 종료
            else:
                answer += 1
                break
                
    return answer