# 단어를 배열로 받는다.
word = list(input())

# a~z의 개수만큼 -1로 만들어진 딕셔너리를 만든다.
alist = {}
for alphabet in range(ord('a'), ord('z')+1):
    # range를 쓰면 z전까지만 출력되서..+1을 해줬습니다.
    alist[alphabet] = -1

# 배열에서 알파벳을 하나씩 꺼내서 index()로 위치값을 알아낸다.
# dict안에서 알파벳의 value값을 위치값으로 바꿔준다.
for w in word:
    # 알파벳이 두번째 이상으로 등장하는 경우는 그냥 재끼도록한다.
    if alist[ord(w)] == -1:
        alist[ord(w)] = word.index(w)

# dict의 values를 출력한다.
cnt = list(alist.values())
result = ''
for c in cnt:
    result += str(c) + ' '
print(result)
