# 전에 풀었던 imos법과 시간을 초로 통일하는 것을 이용하면 될 듯

# 시간을 초단위로 변환
def time_to_sec(time):
    sec = int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])
    return sec

# 초단위를 다시 시간대로 변환
def sec_to_time(sec):
    hour, sec = divmod(sec, 3600)
    minute, sec = divmod(sec, 60)
    return f"{hour:02d}:{minute:02d}:{sec:02d}"

def solution(play_time, adv_time, logs):

    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    secs = [0] * (play_sec + 1)  # IMOS법은 뒤에 하나가 더 필요

    # 누적합 배열 생성 (시작점 +1, 끝점 -1 부여)
    for log in logs:
        start, end = time_to_sec(log[:8]), time_to_sec(log[9:])
        secs[start] += 1
        secs[end] -= 1

    # 휩쓸기 (최종 누적 시간 만들기)
    for i in range(play_sec):
        secs[i + 1] += secs[i]

    # 최적의 시간 찾기 (0초 부터 시작)
    # 초기화
    now = sum(secs[:adv_sec])
    max_acc_secs = now  # 최대 누적 초
    optimum_start_index = 0  # 최적의 시작 위치
    for i in range(1, play_sec - adv_sec + 2):
        now += secs[i + adv_sec - 1] - secs[i - 1] # 맨 뒤 값은 추가하고 맨 앞 값은 제외
        # 더 나은 최적의 시간을 찾았으면
        if max_acc_secs < now:
            max_acc_secs, optimum_start_index = now, i

    return sec_to_time(optimum_start_index)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

