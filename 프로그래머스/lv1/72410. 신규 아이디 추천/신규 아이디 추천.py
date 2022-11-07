import re

def solution(new_id):
    answer = new_id
    # 1단계 : 소문자 변환
    answer = answer.lower()
    # 2단계 : 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모든 문자 제거
    answer = re.sub('[^a-z0-9-_\.]', '', answer)
    # 3단계 : . 2개 이상을 1개로 변경
    answer = re.sub('\.{2,}', '.', answer)
    # 4단계 : 양쪽에 . 제거
    answer = answer.strip('.')
    # 5단계 : 빈 문자열이면 a 대입
    if len(answer) == 0: answer = 'a'
    # 6단계 : 15개 까지 문자만 저장(. 있으면 제거)
    answer = answer[:15].rstrip('.')
    # 7단계 : 2개 이하면 길이가 3이 될 때까지 마지막 문자 연결
    answer = answer.ljust(3, answer[-1])

    return answer