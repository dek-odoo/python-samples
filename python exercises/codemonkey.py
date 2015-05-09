def f(a, b, c):
    print a, b, c
x = [1, 2, 3]
f(*x)
f(*(1, 2, 3))
