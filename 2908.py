nums = [list(x) for x in input().split()]
a = ''
b = ''

for j in range(2, -1, -1):
    a += nums[0][j]
    b += nums[1][j]

if a > b:
    print(a)
else:
    print(b)
