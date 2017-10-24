# 1, 7, 19, 37, 61
# 6, 12, 18, 24 # 6의 배수로 늘어난다

num = int(input())
i = 1
x = 1

while x <= num:
    x += 6 * i
    i += 1

    if num == 1:
        i = 1
    elif num <= 7:
        i = 2

print(i)
