# 음 입력받기
num = input()

# 입력받은 숫자를 split()한다
numlist = num.split()

# input()으로 받은 값은 str임을 잊지말자!

flag = True
for i, num in enumerate(numlist):
    # 1~8 순서라면 ascending
    # 순차적으로 1씩 늘어나는지 비교하다가 1이 아니면 flag=False로 바꾸기
    if int(num) != (i+1):
        flag = False

if flag == True:
    print('ascending')
# 8~1 순서라면 descending
# 순차적으로 1씩 줄어드는지 비교하다가 1이 아니면 flag=False로 바꾸기
elif numlist == ['8', '7', '6', '5', '4', '3', '2', '1']:
    print('descending')
# 섞여있다면 mixed
# 위에 둘다가 아니면 mixed! flag=False로 바꾸기
else:
    print('mixed')

