
def minimize():
    current = yield
    while True:
        value = yield current
        print("current = yield")
        current = min(value, current)

it = minimize()
next(it)

print(it.send(10))
print("aaa")
print(it.send(9))
print("bbb")
print(it.send(20))
print(it.send(9))
