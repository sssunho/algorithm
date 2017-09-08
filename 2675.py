# 테스트케이스 개수 입력받기
cnt = input()

# 반복횟수와 문자열을 받는다
for _ in range(int(cnt)):
    case = input()
    case = case.split()
    
    # 입력받은 문자열의 문자를 입력받은 횟수만큼 반복해서 출력한다
    text = ''
    for c in case[1]:
        text += c*int(case[0])
    print(text)

