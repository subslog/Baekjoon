def multiple_set(s: str) -> list:
    m_s = []
    for i in range(len(s) - 1):
        # 알파벳이면 대문자로 변환해 push
        if s[i:i+2].isalpha(): m_s.append(s[i:i+2].upper())
    
    return m_s

def solution(str1, str2):
    # 다중집합 변환
    set1 = multiple_set(str1)
    set2 = multiple_set(str2)
    # 두 집합 모두 공집합이면 65536 반환
    if not set1 and not set2: return 65536

    intersection = 0    # 교집합 원소 수
    union = 0           # 합집합 원소 수
    # 교집합, 합집합 원소 카운트
    for s in set(set1 + set2):
        # 원소 수 카운트
        set1_cnt = set1.count(s)
        set2_cnt = set2.count(s)
        # 교집합은 작은 값, 합집합은 큰 값 추가
        intersection += min(set1_cnt, set2_cnt)
        union += max(set1_cnt, set2_cnt)
    
    # 정답
    answer = int(intersection / union * 65536)
    
    return answer