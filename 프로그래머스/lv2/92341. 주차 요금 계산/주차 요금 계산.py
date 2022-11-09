import math

def parking_time(start: str, end: str) -> int:
    """주차 시간을 분으로 반환하는 함수"""
    # 주차 (분)
    s_h, s_m = start.split(':')
    start_m = int(s_h) * 60 + int(s_m)
    # 출차 (분)
    e_h, e_m = end.split(':')
    end_m = int(e_h) * 60 + int(e_m)

    return end_m - start_m

def solution(fees, records):
    answer = []

    parking = dict()    # 주차 차량
    settlement = dict() # 주차 시간

    # 주차 요금 정산
    for record in records:
        # 시각, 차량번호, 내역
        time, number, history = record.split()
        # 주차 처리
        if history == 'IN':
            parking[number] = time
            # 주차 정산 시간에 차가 없으면 추가
            if number not in settlement: settlement[number] = 0
        # 출차 처리
        else:
            # 주차 시간
            settlement[number] += parking_time(parking.pop(number), time)
    # 출차하지 않은 차 출차 처리
    for exit in parking:
        settlement[exit] += parking_time(parking[exit], '23:59')
    # 차량 번호 오름차순으로 주차비 정산
    for total in sorted(settlement):
        # 기본 요금
        fee = fees[1]
        # 잔여 시간 = 주차 시간 - 기본 시간
        fee_time = settlement[total] - fees[0]
        # 단위 요금 정산 (잔여 시간이 마이너스면 추가 요금이 없다.)
        fee += max(0, math.ceil(fee_time / fees[2]) * fees[3])
        answer.append(fee)

    return answer