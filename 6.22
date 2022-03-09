# Nam Doan
# 1847037

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())


def func1(x, y):
    return a * x + b * y - c


def func2(x, y):
    return d * x + e * y - f


finalx = 100
finaly = 100
for x in range(-10, 11):
    for y in range(-10, 11):
        if func1(x, y) == func2(x, y) and func1(x, y) == 0:
            finalx = x
            finaly = y
if finalx != 100:
    print(finalx, finaly)
else:
    print('No solution')
