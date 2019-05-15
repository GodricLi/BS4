# _*_ coding=utf-8 _*_


a = "start"
b = [1, 2, 3]


def test(x, y):
    x = "d"
    print(x)
    y[0]=0
    print(y)


test(a,b)
print(a,b)
