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
    parking = [-1] * 10000      # 차량 입차, 출차 체크용 리스트
    total = [0] * 10000         # 토탈 시간 저장용 리스트
    
    # 입차, 출차 처리
    for record in records:
        # 시간, 차량 번호, (입차 or 출차)
        time, number, state = record.split()
        number = int(number)
        # 시간을 분으로 환산
        minute = time_change(time)
        # 입차면 parking 리스트에 시간 추가
        if state == 'IN':
            parking[number] = minute
        # 출차면 parking 리스트에서 제거 후 total 리스트에 누적
        else:
            total[number] += minute - parking[number]
            parking[number] = -1
    
    # 요금 계산
    minute = time_change('23:59')
    for i in range(10000):
        # 출차를 안했으면 출차 시간 23:59 으로 계산
        if parking[i] != -1:
            total[i] += minute - parking[i]
            parking[i] = -1
        # 주차 요금 계산
        if total[i] > 0:
            answer.append(parking_cal(fees[0], fees[1], fees[2], fees[3], total[i]))
    
    return answer