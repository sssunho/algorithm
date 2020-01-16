# cryptogram = "browoanoommnaon"
cryptogram = "zyelleyz"


def solution(cryptogram):
    answer = ''

    while True:
        for i in range(97, 123):
            cnt = cryptogram.count(chr(i))
            if cnt > 1:
                cryptogram = cryptogram.replace(chr(i)*2, '')

        c = 0
        for a in cryptogram:
            if cryptogram.count(a) > 1:
                c += 1
        if c == 0:
            break

    return cryptogram


print(solution(cryptogram))

