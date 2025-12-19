from functools import reduce
def Square(x):
    i = int(x)
    return x**2

def Cube(x):
    return x**3

def Double(x):
    return 2*x

def to_str(x):
    return str(x)

def digits(x):
    return len(x)


def Compose(x):
    return digits(to_str(Double(Square(x))))

def Build(*func):
    return reduce(lambda f, g: lambda x:f(g(x)), func)
#---------------------------------

p1 = Build(digits, to_str, Double, Square)
p2 = Build(Double, Square)

# res = Compose(10)
res = p1(10)
res = p2(10)
print(res, type(res))

