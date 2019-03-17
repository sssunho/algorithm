totalTicket = 2000
logs = [
    "woni request 09:12:29",
    "brown request 09:23:11",
    "brown leave 09:23:44",
    "jason request 09:33:51",
    "jun request 09:33:56",
    "cu request 09:34:02"
]


import datetime


import datetime


def solution(totalTicket, logs):
    answer = []
    finish_time = 0.01

    for log in logs:
        log = log.split()

        ltime = log[2].split(':')
        lm = int(ltime[1])
        ls = int(ltime[2]) * 0.01
        ltime = lm + ls

        if log[1] == 'leave':
            answer.remove(log[0])
        elif ltime < finish_time:
            continue
        else:
            finish_time = ltime + 1
            answer.append(log[0])

    answer.sort()
    return answer


# def solution(totalTicket, logs):
#     answer = []
#     start_time = datetime.datetime.now()
#     start_time = start_time.replace(hour=9, minute=0, second=0)
#     temp_time = datetime.datetime.now()
#
#     for n, log in enumerate(logs):
#         log = log.split()
#         t = log[2].split(':')
#
#         answer.append(log[0])
#         if log[1] == 'leave':
#             answer.remove(log[0])
#
#         finish_time = start_time + datetime.timedelta(minutes=1)
#         temp_time = temp_time.replace(hour=int(t[0]), minute=int(t[1]), second=int(t[2]))
#         if temp_time <= finish_time:
#             start_time = start_time.replace(hour=t[0], minute=t[1], second=t[2])
#             answer.remove(log[0])
#
#     return answer


print(solution(totalTicket, logs))
