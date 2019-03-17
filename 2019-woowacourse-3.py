word = "I love you"


def solution(word):
    answer = ''

    a1 = [chr(i) for i in range(65, 91)]
    a2 = [chr(i) for i in range(97, 123)]
    b1 = list(reversed(a1))
    b2 = list(reversed(a2))

    asc = a1 + a2
    des = b1 + b2

    for n, i in enumerate(word):
        if i == ' ':
            answer += i
            continue

        # 오름차순에서 위치 찾기
        a = asc.index(i)
        # 내림차순 문자로 대치
        answer += des[a]

    return answer


print(solution(word))

