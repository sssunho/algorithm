def solution(number):
    answer = 0
    samyookgu = ['3', '6', '9']

    for i in range(number+1):
        i = str(i)
        for j in i:
            print(j)
            if j in samyookgu:
                answer += 1

    return answer


print(solution(13))
