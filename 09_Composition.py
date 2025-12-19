def Square(x):
    return x**2

def to_str(x):
    return str(x)

def digits(x):
    return len(x)

res = digits(to_str(Square(10)))
print(res, type(res))

