def polynomial(x, *a):
    y = 0.0
    for i in range(len(a) - 1, -1, -1):
        y = x * y + a[i]
    return y
