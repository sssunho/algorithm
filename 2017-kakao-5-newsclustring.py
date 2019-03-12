def solution(str1, str2):
    answer = 0

    # str1, str2를 두 글자씩 끊는다
    # 문자가 아닌 다른 것이 들어있으면 버린다
    # 다 대문자로 처리한다
    import re
    p = re.compile('[a-zA-Z]{2}')
    str1_multiset = [(str1[i - 1] + str1[i]).upper() for i in range(1, len(str1)) if p.search(str1[i - 1] + str1[i])]
    str2_multiset = [(str2[i - 1] + str2[i]).upper() for i in range(1, len(str2)) if p.search(str2[i - 1] + str2[i])]

    if not str1_multiset and not str2_multiset:
        return 65536

    # 유사도 = int(교집합 개수/ 합집합 개수 * 65536)
    set1 = set(str1_multiset)
    set2 = set(str2_multiset)
    answer = len(set1 & set2) / len(set1 | set2) * 65536
    return answer

# solution('E=M*C^2', 'e=m*c^2')
# FR, RA, AN, NC, CE
# FR, RE, EN, NC, CH

solution('aa1+aa2', 'AAAA12')
# ['AA', 'A1', '1+', '+A', 'AA', 'A2']
# ['AA', 'AA', 'AA', 'A1', '12']

# solution('handshake', 'shake hands')
# solution('FRANCE', 'french')
# 16384