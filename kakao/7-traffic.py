def solution(lines):
    answer = 0
    temp = 0

    # lines 배열을 하나씩 꺼내서 공백으로 split()
    for line in lines:
        log = line.split()
        print('log', log)

        slog = float(log[1].split(':')[2])
        s = float(log[2][:-1])

        plz = {}
        plza = []
        for i in range(int(slog), int(slog+s)):
            plza.append(i)
            print(i)

        for i in range(int(slog), int(slog+s)):
            if plza.count(i) > temp:
                temp = plza.count(i)
    print(temp)
    answer = temp
    return answer + 1

solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
# 2