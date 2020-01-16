pobi = [97, 98]
crong = [197, 198]
# pobi = [99, 102]
# crong = [211, 212]


def solution(pobi, crong):
    if pobi[0]%2 != 1 or pobi[0]+1 != pobi[1] or crong[0]%2 != 1 or crong[0]+1 != crong[1]:
        return -1

    a = []
    for n, i in enumerate(pobi + crong):
        i = str(i)
        r1 = 0
        for j in i:
            r1 += int(j)
        a.append(r1)

        r2 = 1
        for j in i:
            r2 = r2 * int(j)
        a.append(r2)

    p = a[:4]
    c = a[4:]
    p.sort(reverse=True)
    c.sort(reverse=True)

    if p[0] > c[0]:
        return 1
    elif p[0] < c[0]:
        return 2
    elif p[0] == c[0]:
        return 0
    else:
        return -1

print(solution(pobi, crong))