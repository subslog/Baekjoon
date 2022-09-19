def time_change(time: str):
    """시간을 분으로 환산하여 반환하는 함수"""
    hour, minute = map(int, time.split(':'))
    
    return hour * 60 + minute

def parking_cal(d_time: int, d_won: int, time: int, won: int, p_time : int):
    """주차 요금을 계산하는 함수"""
    money = d_won       # 기본 요금
    p_time -= d_time    # 기본 시간 빼기
    # 기본 시간을 초과하면 추가 계산
    if p_time > 0:
        money += p_time // time * won
        # 잔여 시간이 있으면 추가 계산
        if p_time % time > 0:
            money += won
    
    return money

def solution(fees, records):
    answer = []
    parking = dict()    # 차량 입차, 출차 체크용 딕셔너리
    
    # 입차, 출차 처리
    for record in records:
        # 시간, 차량 번호, (입차 or 출차)
        time, number, state = record.split()
        number = int(number)
        # 시간을 분으로 환산
        minute = time_change(time)
        # 딕셔너리에 키가 없으면 추가[시간, 누적 시간]
        if not number in parking:
            parking[number] = [0, 0]
        # 입차면 parking 딕셔너리에 시간 추가
        if state == 'IN':
            parking[number][0] = minute
        # 출차면 parking 딕셔너리에서 제거 후 요금 계산
        else:
            parking[number][1] += minute - parking[number][0]
            parking[number][0] = -1
            
    # 차 번호 순으로 오름차순 정렬
    parking = sorted(parking.items())
    
    # 요금 계산
    minute = time_change('23:59')
    for p in parking:
        # 출차를 안했으면 출차 시간 23:59 으로 계산
        if p[1][0] != -1:
            p[1][1] += minute - p[1][0]
            p[1][0] = -1
        # 주차 요금 계산
        answer.append(parking_cal(fees[0], fees[1], fees[2], fees[3], p[1][1]))
    
    return answer