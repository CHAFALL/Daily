# n : 버스 운행 횟수
# t : 버스간 간격
# m : 버스 하나 당 수용가능한 인원 수
def solution(n, t, m, timetable):
    answer = ''
    sortedTimes = []
    N = len(timetable)

    for time in timetable:
        # 시각과 분 분리
        hour, minute = time.split(':')
        # 분으로 환산
        totalMinute = int(hour) * 60 + int(minute)
        sortedTimes.append(totalMinute)

    sortedTimes.sort() # 오름차순 정렬

    # 버스 시간표 만들기 (9 * 60 + 배차 간격)
    busTime = [540 + t * i for i in range(n)]

    i = 0 # 기다린 순서에 대한 인덱스
    for tm in busTime:
        cnt = 0
        # 버스가 왔을 때 탑승 여부 파악
        while cnt < m and i < N:
            if sortedTimes[i] <= tm:
                cnt += 1
                i += 1
            else:
                break

        # 자리 오버했다면 그 사람보다 1분 일찍 도착하자!
        if cnt >= m:
            answer = sortedTimes[i - 1] - 1
        else:
            answer = tm

    # 분 단위를 "HH:MM" 형식으로 변환
    hour = answer // 60
    minute = answer % 60
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))