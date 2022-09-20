from collections import deque

def solution(msg):
    answer = []
    # 단어 큐에 저장
    queue = deque(list(msg))
    # 사전 초기화
    dictionary = dict()
    for i in range(1, 27):
        dictionary[chr(i + 64)] = i
    # 색인 번호
    index = 27
    # LZW 압축
    while True:
        # 현재 문자
        word = queue.popleft()
        # 다음 문자 검사
        cnt = 0
        for i in range(len(queue)):
            # 딕셔너리에 없는 문자면 색인 번호 추가 및 사전 등록
            if not word + queue[i] in dictionary:
                answer.append(dictionary[word])
                dictionary[word + queue[i]] = index
                index += 1
                break
            # 딕셔너리에 있는 문자면 문자 연결
            else:
                word += queue[i]
            cnt += 1
        # i 만큼 문자 pop
        for _ in range(cnt):
            queue.popleft()
        # 큐가 비었으면 종료
        if not queue:
            break
    # 남은 문자 색인 번호 추가
    answer.append(dictionary[word])
        
    return answer