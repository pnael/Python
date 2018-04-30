import math

p = 23
a = 5


def multiples(a, p):
    r = []
    for i in range(1, p):
        r += [i * a]
    return r


m = multiples(a, p)
r = map(lambda x: x % p, m)
print(list(r).sort())
