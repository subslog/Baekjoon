def solution(record):
    commend = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    # id를 키로 사용자 닉네임 저장
    nick = {}
    # 채팅방 히스토리
    history = []
    # 메시지 기록
    for r in record:
        c, *id = r.split()
        # id 키가 없으면 사전에 등록
        if not id[0] in nick: nick[id[0]] = ''
        # 엔터 : 닉네임 갱신, 입장 기록
        if c == 'Enter':
            nick[id[0]] = id[1]
            history.append((id[0], commend[c]))
        # 나가기 : 퇴장 기록
        elif c == 'Leave':
            history.append((id[0], commend[c]))
        # 변경 : 닉네임 갱신
        elif c == 'Change':
            nick[id[0]] = id[1]
    # 메시지 가공
    answer = [nick[h[0]] + h[1] for h in history]

    return answer