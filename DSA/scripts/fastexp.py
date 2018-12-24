def fstexp(a: float, b: int):
    x = a
    y = 1
    z = b
    while z > 0:
        r = z % 2
        z = int(z / 2)
        if r == 1:
            y = x * y
        x = x * x
    return y

assert fstexp(2.0, 0) == 1.0
assert fstexp(52859151.521521, 0) == 1.0
assert fstexp(2.0, 1) == 2.0
assert fstexp(2.0, 2) == 4.0