def solution(cacheSize, cities):
    # 캐시크기 = 페이지수
    answer = 0  # answer = time
    ref = 1 # 참조페이지는 계속 1씩 상승하고 나머지값이 결국 참조 페이지가 된다
    pages = []

    for city in cities:
        # 대문자로 통일한다
        city = city.upper()
        # 새로운 도시가 들어가면 miss = 5
        # 있는 도시가 또 들어가면 hit = 1
        # hit, miss 날 때마다 answer에 더하기
        ref += 1

        # 일단 꽉 차 있는지 확인
        if cacheSize == 0:
            answer += 5
        elif len(pages) < cacheSize:
            # 꽉차있지 않다면 배열에 넣고 miss
            pages.append(city)
            answer += 5
        elif len(pages) == cacheSize:
            # 꽉 차 있다면 배열안에 city 있는지 확인
            if city in pages:
                # 있다면 hit
                answer += 1
            else:
                # 없다면 miss하고 참조페이지 위치에 넣기
                answer += 5
                pages[ref%cacheSize] = city


    print(answer, pages)
    return answer

solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork",
             "LA", "SanFrancisco", "Seoul", "Rome",
             "Paris", "Jeju", "NewYork", "Rome"])