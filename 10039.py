# 5명의 점수 받아서 배열에 저장하기
scorelist = []
for _ in range(5):
    score = input()
    scorelist.append(int(score))

# 40점 이하 점수는 40점으로 바꾸기
total = 0
for score in scorelist:
    if score < 40:
        score = 40

    total += score

# 평균내기
print(int(total/5))
