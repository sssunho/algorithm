# 테스트케이스 개수 입력 받기
cnt = input()

# 입력받은 개수만큼 input 받아서 배열에 저장하기
caselist = []
for _ in range(int(cnt)):
    case = input()
    caselist.append(case)

# 배열에서 하나씩 꺼내서 split('X')로 나누기
for _case in caselist:
    case = _case.split('X')

    # 나눈 결과의 배열 값을 하나씩 꺼내서 등차수열 합 구하기
    total = 0
    for c in case:
        n = len(c)
        
        # 배열값의 길이가 1이상이면 실행한다
        if n > 0:
            nn = n * (n + 1) // 2
            # 모든 배열의 값 합치기
            total += nn
    print(total)


