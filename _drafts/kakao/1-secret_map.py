def solution(n, arr1, arr2):
    answer = []

    # arr의 각 요소 x를 2진수로 바꾼다
    # arr1과 arr2의 숫자의 길이가 다르면? 2진수로 바꿀 때 무조건 n의 길이로 채워준다
    arr11 = [format(int(bin(x)[2:]), '0={}'.format(n)) for x in arr1]
    arr22 = [format(int(bin(x)[2:]), '0={}'.format(n)) for x in arr2]

    for i in range(n):
        # arr1, 2에서 각각의 요소를 꺼내 비교한다
        #: 각각 배열 하나씩 꺼낸다
        a = arr11[i]
        b = arr22[i]

        # 자릿수를 비교하며 둘중에 하나라도 1이면 #을 추가 아니면 0 추가
        ans = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
