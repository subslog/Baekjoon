import bisect

def time_change(time: str) -> int:
    """시간을 string -> int 형으로 변환하는 함수"""
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def solution(n, t, m, timetable):
    answer = ''
    # 크루들을 태울 버스
    buses = [[] for _ in range(n)]
    # 버스가 오는 시간
    arrival_time = [time_change('09:00')]
    for i in range(n - 1):
        arrival_time.append(arrival_time[-1] + t)
    # 크루들이 도착한 시간을 정렬한다.
    timetable = list(map(time_change, timetable))
    timetable.sort()
    # 시간에 맞게 크루들이 버스를 탄다.
    for time in timetable:
        idx = bisect.bisect_left(arrival_time, time)
        # 탑승 가능한 시간이 없으면 건너뛴다.
        if idx == n:
            continue
        # 정원을 초과하지 않은 시간에 탄다.
        while idx < n:
            if len(buses[idx]) < m:
                buses[idx].append(time)
                break
            idx += 1
    # 마지막 버스에 자리가 있으면 마지막 버스를 시간에 맞춰 탄다.
    if len(buses[-1]) < m:
        late_time = arrival_time[-1]
    # 자리가 없으면 제일 늦게 탈 수 있는 시간을 찾는다.
    else:
        late_time = time_change('00:00')
        for i in range(n):
            for bus in buses[i]:
                late_time = max(late_time, bus - 1)

    answer = str(late_time // 60).zfill(2) + ':' + str(late_time % 60).zfill(2)
                
    return answer